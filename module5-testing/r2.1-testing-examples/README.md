# Testing Examples
When it comes to backend applications, which are the areas of the code that can be and should be tested? The objectives of this lesson are:
1. Understanding the different parts of backend code that should be tested
2. Understanding the different types of testing use cases

## Pure Functions

A **pure function** is a function which:
- Given the same input, always returns the same output.
- Produces no side effects.

Let's take a look at an example:
```js
function calculateTax( productPrice ) {
    return productPrice * 0.05 + productPrice;
}
```
This is pure function because the output will always be the same for an input, it is not affected by any external factors and neither does it create any other side affects such as calling another API or another function.

However, if this same function were to be written as:
```js
var tax = getCurrentTaxRate();
function calculateTax( productPrice ) {
    return productPrice * (tax / 100) + productPrice;
}
```
Now this is no longer a pure function, because the value of tax is dependent on another function and subject to change over a period of time. So the output can vary for the same input.

This might be a simplistic example, however in backend applications you often end up writing helper functions or util functions that are meant to be reused in the code and perform a very specific operation. Such functions which are isolated in the codebase and written as pure functions are most easy to test for and should be tested for to ensure it's working correctly given that many other functions depend on it.

## Controllers and API Routes

We have learned in the MVC architecture controllers are functions that interact between the views and the models of our application. To be more specific, controllers are the callback functions passed to our REST API routes indicating what operation needs to be performed for a given route. Controllers do a lot of the heavy lifting work to ensure our APIs are working correctly, so naturally they must be tested.

Let's take an example of a books controller function:
```js
async function getBook(req, res) {
    const book = await booksDB.readById(req.bookId)
    res.json({book})
}
```

We are only looking at the controller for now, and don't need to concern ourselves with the corresponding API route. We can write different unit tests for all the controller functions, but specifically for this function:
- Test for valid book ID and book found
- Test for valid book ID and book not found
- Test for invalid book ID
- Test for empty book ID
and maybe a few more test cases.

This way we are just testing one unit of the code, which is the `getBook` controller function. However, this function makes use of a database `booksDB` so it is actually not a pure function or even a unit test. To test this function, we will also have to test the connection and interaction with the database. To make this strictly a unit test, we can mock the database function and simply test the controller logic. We'll read about mocking in the next lesson.

Now, let's look at the full picture with the API route:
```js
app.get("/api/books/:id", booksController.getBook)
```

After unit testing the controller, we may want to test the API call itself. In that case, we would write a test that executes the API call first and then runs assertions on the API response. This is where the `supertest` library comes in which helps run assertions on HTTP requests and responses. Revisit some of the previous assignments, and take a look at the tests for API routes using `supertest`.

What is the difference between testing the controller and testing the route? When you're testing the controller, you can simply check the logic of the operation. When you're testing the API route, you can not only check logic but also API expectations like request parameters and headers, response body format and headers, tokens and headers related to authentication, etc.

## Middleware

As the name suggests, middleware is a piece of code that executes between the input and output of a request-response lifecycle. These can be helper functions or external libraries that perform an operation on your API request before the actual controller starts operating on it.

In practice, an Express application is essentially a series of middleware function calls. In Express, middleware functions are functions that have access to the request object (req), the response object (res), and the next middleware function in the application’s request-response cycle.

Middleware functions can perform the following tasks:
- Execute any code.
- Make changes to the request and the response objects.
- End the request-response cycle.
- Call the next middleware function in the stack.

In larger backend codebases, it is quite likely that you might write some custom middleware for your APIs. And these middleware will act on each and every request your server receives, and that's why it's very important to test your middleware thoroughly.

Let's take a simple example:
```js
const express = require('express')
const app = express()

const myTimeLogger = function (req, res, next) {
  console.log('Time:', Date.now())
  next()
}

app.use(myTimeLogger)

app.get("/", function (req, res, next) {
  res.json({message: "Hello"})
})
```

Here we have a simple middlware function passed to our Express app. It does one simple operation and that is log the current time each time a request is received by our Express app. This operation is executed and then the control is passed on to the `next` middleware in the app or the first route handler of the app which in this case is the GET handler for `/` route.

**Note**: Even our route handlers work like a set of middleware, passing the control from one handler to another till the matching handler performs an operation and returns the response. Once a response is sent, it ends the request-response lifecycle. But if `next()` is called then the control is passed to the next middleware.

When we test our custom middlware functions, we can pass different types of requests with varying inputs to ensure the middleware works correctly in all cases.

## What not to test in backend

The quick answer is: Any code that is not written by us or our team.

In our Node.js applications, we use a lot of different npm packages and sometimes might even make API calls to third party APIs whose services we have integrated with. It can get tempting to test these as well because they make up crucial aspects of our code, however since these packages or APIs are written by another developer or company, it is upto them to ensure their code is well-tested. We must interest ourselves only with testing the code that we write for our specific applications.

For our code that integrates with a package or third-party API, it is better to mock the external code in our unit tests. This means following the principle of "Assuming that the external code provides required inputs, how does our code work?"

This does not mean we blindly believe in external packages and APIs. It's always recommended to check reviews, number of downloads and star ratings on a package or API we want to use, to get an idea of how reliable the service is. We may even encounter bugs that should be reported to the specific developer or company using their feedback or issue tracking system. However, writing tests takes effort and time, which should be focussed only on our specific code.

In the next lesson, we will look into mocking and how it is useful for writing unit tests.