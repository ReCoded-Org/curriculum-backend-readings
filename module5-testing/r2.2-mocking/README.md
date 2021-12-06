# Mocking
We've mentioned mocking in the last couple of lessons, but what exactly is mocking and how is it helpful in writing tests? The objectives of this lesson are:
1. Understanding the use of mocking in tests
2. Understanding different ways to implement mocking

## What is mocking?

Sometimes a function, class or component may be hard to test for because:
- The class has dependencies which are hard to provide (e.g. the constructor expects multiple arguments)
- Some functionality of a class may not be accessible from outside (e.g. by using access modifiers like private in TypeScript)
- The function/class/component does far too much that we don't want in our tests

In simple terms, mocking refers to replacing an actual piece of code with a simple piece of code that provides the required inputs by default. Mocking helps us write better tests because:
- They eliminate functionality which we don't really want in the scope of a test.
- Makes tests faster and less flaky by avoiding dependencies (e.g. access to a real database, using a third-party library)
- Makes things easier to test. With mocking, we can easily create the ideal test setup to use in our tests.
- Reduce the setup of our tests. Many libraries expect some setup to be done in order to work. With mocking, we can ignore all this and focus on testing actual functionality instead.
- We don't need to test third-party code as it is probably already tested. In unit tests, we want to focus on the smaller parts of our application that we developed ourselves. Mocking third-party dependencies help to keep tests more focused on our custom logic and less about internal implementation details.

## Monkey patching

Monkey patching is a technique to add, modify, or suppress the default behavior of a piece of code at runtime without changing its original source code. It is a quick and easy way to implement mocking for tests.

Let's look at an example of a controller that depends on a database model.
```js
async function getBook(req, res) {
    const book = await booksDB.readById(req.bookId)
    res.json({book})
}
```
By looking at this code, we can guess that `booksDB` must be an object with one property `readById` whose value is a function:
```js
{
    ...
    readbyId: function(id) {
        ...
    },
    ...
}
```
The other model functions make up the rest of the key-value pairs in this object.

In order to mock the database function, we can simply replace the specific `booksDB` function we are testing for with a determinisitc function.

So, let's say we want to test for the case where booksDB returns `undefined` for some reason. In our test file, we can write:
```js
booksDB.readById = function(id) {
    return undefined
}
```

There we go, now when we execute the test on our controller it will get the value `undefined` when it calls the `booksDB.readById` function. In this way, we can make `readById` return a specific result to be used by our controller in each different test case. Such as returning a specific book or an error message or an incomplete book object.

By using this technique, we are only testing how our controller handles different test cases and not testing the actual database model code which is a third-party.

However, we did mention in the beginning that monkey patching works without changing the original source code, but we modified the code here. To make sure we don't completely modify the code, we can do this:
```js
// Keep track of original readById
const originalReadById = booksDB.readById
// Change temporarily to mock function
booksDB.readById = function(id) {
    return undefined
}
// Run some test with mock readById
...
...
...
// Restore original readById
booksDB.readById = originalReadById
```

This ensures that the code is only temporarily modified to the mock version for the specific scope where it is required, and then it goes back to its original version to be used by other parts of the file.

## Mocking in Jest

Although monkey patching does the job, Jest provides more sophisticated methods for mocking. Going by the same example as above, we can mock the `readById` function using:
```js
// Keep track of original readById
const originalReadById = booksDB.readById
// Change temporarily to mock function
booksDB.readById = jest.fn((id) => undefined)
// Run some test with mock readById
...
...
...
// Restore original readById
booksDB.readById = originalReadById
```

`jest.fn()` creates a new mock function. But we can also use some Jest functions to track the original function and restore it.
```js
// Keep track of original readById
jest.spyOn(booksDB, "readById")
// Change temporarily to mock function
booksDB.readById.mockImplementation((id) => undefined)
// Run some test with mock readById
...
...
...
// Restore original readById
booksDB.readById.mockRestore()
```

The `spyOn`, `mockImplementation` and `mockRestore` functions help to track, implement mocking on and restore a function.

Another advantage of using Jest mock functions, is to run assertions on the function calls:
```js
// The mock function was called at least once
expect(mockFunc).toHaveBeenCalled();

// The mock function was called at least once with the specified args
expect(mockFunc).toHaveBeenCalledWith(arg1, arg2);

// The last call to the mock function was called with the specified args
expect(mockFunc).toHaveBeenLastCalledWith(arg1, arg2);
```

We can eliminate the actual functionality of third-party functions and focus simply on how, when and with what parameters was the function called. It helps us test our controllers' or services' interaction with the third-party functions.

Using Jest, you can even mock entire modules. There are many different possiblities. Go through the Jest documentation for mocking [here](https://jestjs.io/docs/mock-functions) and [here](https://jestjs.io/docs/mock-function-api).

## Mock Data

Sometimes in our tests we may need large sets of mock data, such as mock names, mock addresses, mock phone numbers or mock credit card numbers depending on our application. It can be difficult to come up with such mock values but it's also not advisable to use too trivial values like "test", "123" or "lorem ipsum".

In such cases, we can use libraries like [faker](https://www.npmjs.com/package/faker) which helps generate different kinds of fake/mock data which looks like real data.

Some examples are:
```js
var faker = require('faker');
var randomName = faker.name.findName(); // Rowan Nikolaus
var randomEmail = faker.internet.email(); // Kassandra.Haley@erich.biz
var randomCard = faker.helpers.createCard(); // random contact card containing many properties
```

It also has localization settings to generate fake data in many different languages.