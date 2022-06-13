# Testing in JavaScript
Now that we have understood why testing is required, its different types and the testing mindset, let's move into implementing automated tests in JavaScript, or Node.js to be more specific. The objectives of this lesson are:
1. Getting familiar with different JavaScript testing frameworks
2. Understanding the usage of Jest

## Testing Libraries in JavaScript
There are a number of testing libraries in JavaScript. The differences between them are not major. Similar to many other things that you will learn, if you know one of them, you will understand the general concepts of the others.

Feel free to explore some of these frameworks below.

### Jest
[Jest](https://jestjs.io/docs/getting-started) is currently one of the most popular testing frameworks since it works for both frontend and backend tests. It was initially developed for writing tests for React but now it can work not only with Node but also Babel, TypeScript, React, Angular and Vue! Using Jest, it is very quick and easy to setup unit tests, and Jest also provided great features for mocking and an interactive CLI. It has a many other associated libraries like [jest-in-case](https://www.npmjs.com/package/jest-in-case) and [@testing-library/jest-dom](https://www.npmjs.com/package/@testing-library/jest-dom).

We will be using Jest through the rest of this module.

### Mocha
[Mocha](https://mochajs.org/#getting-started) is probably the most popular testing framework for Node.js. It is great for testing both synchronous and asynchronous code as well as following the BDD principle as each test usually represents an expected behaviour of the application. Mocha is often paired with an assertion library like [Chai](https://www.chaijs.com/) which has a wide range of assertion statements to be used in testing the outputs. [Mocha Steps](https://www.npmjs.com/package/mocha-steps) is an add-on library to run tests sequentially. 

We have used Mocha and Chai in all the assignments of previous modules. Please read though [this article](https://blog.logrocket.com/a-quick-and-complete-guide-to-mocha-testing-d0e0ea09f09d/) to learn about Mocha in detail. Even though we will carry on with Jest in this module, you must spend some time learning about Mocha as well.

### Supertest
[Supertest](https://www.npmjs.com/package/supertest) is another amazing assertion library that helps perform HTTP assertions such as checking for the response status code or response body. It is extremely useful in testing REST APIs, and we have used it in previous assignments' tests as well. It can be paired with Jest and Mocha.

### Jasmine
[Jasmine](https://jasmine.github.io/pages/getting_started.html) is another popular BDD testing framework.

### Cypress
[Cypress](https://www.cypress.io/) is an amazing testing framework that helps perform end-to-end testing on a frontend.

Again: most of the concepts you will learn are agnostic to the framework being
used. For example, with the properties of good tests that we discussed, it does
not matter if you are using Jest, Mocha, Jasmine, or if you are not even using
JavaScript. Try not to focus too much on learning a specific framework but
instead understanding how it executes the ideas of testing.

## Understanding Jest

To [get started with Jest](https://jestjs.io/docs/getting-started), you must first install it as a dev dependency, that is if it hasn't already been installed and listed in your project's `package.json` file.

```bash
npm install --save-dev jest
```

And then in your `package.json` file, create a new npm script which runs Jest:

```js
{
  ...
  "scripts": {
    ...
    "test": "jest"
  },
  ...
}
```

Sometimes you may need to create a configuration file called `jest.config.js`. You can read more about configuring Jest [here](https://jestjs.io/docs/configuration). For our assignments, we will not require a separate configuration.

### Test files structure

Usually a test file is associated with a source file by following the same name. For example, let's say we have a file called `user.js` which holds functions to perform certain user operations. When writing units tests for these functions, we'll create a test file called `user.test.js`. The extension `.test.js` helps Jest identify this as a test file, and the same name of `user` helps us associate which source file the tests are associated with.

It's not just the file naming, but also the file location which is important. Let's say the above mentioned file is actually a model file and has the location `src/models/user.js` then the test can be saved in the same folder as `src/models/user.test.js`. This way the test file is always available next to the source file.
```
src
  |- models
    |- user.js
    |- user.test.js
```

However, the `models` folder may have more than one source file. Let's say it has a `user.js` and a `blogpost.js` and a `comment.js`. In such cases, it is recommended to create a folder with the name `__tests__` inside `models` which houses all test files.
So folder structure would look like:
```
src
  |- models
    |- blogpost.js
    |- comment.js
    |- user.js
    |- __tests__
      |- blogpost.test.js
      |- comment.test.js
      |- user.test.js
```
Even in this case the test files are located near the source files.

In some cases, developers maintain a global tests folder with all the test files such as `src/__tests__`. This works when there are limited test files, but for a growing codebase it is better to follow the above folder structure.

## Test code

Here is the basic syntax of test code in Jest.
```js
describe("My Test Suite", () => {
  test("My Test Case", () => {
    const actualOutput = myFunction(inputs);
    expect(actualOutput).toEqual(expectedOutput);
  });
});
```
The `describe` function is used to hold a collection of test cases, and is also called a test suite. We add a descriptive text as the first argument which will be logged when we run our tests.

Each test case is executed using the `test` function where we pass a descriptive text again and then the test operations are carried out inside the callback function. The general convention for test case descriptions are:
- Starts with the word "should" followed by the conditions and expected result
OR
- Starts with a verb in present tense followed by the conditions and expected result

For example, let's say we are testing our user model. Then our descriptions may look something like:
```js
describe("User Model", () => {
  test("should create new user with first name and last name", () => {
    ...
  });
  test("should not create new user if first name is missing", () => {
    ...
  });
});
```
Another way would be:
```js
describe("User Model", () => {
  test("creates new user with first name and last name", () => {
    ...
  });
  test("does not create new user if first name is missing", () => {
    ...
  });
});
```
It is better to stick to one type of sentence structure throughout the test files, as these statements will be logged when the tests are executed.

Coming back to the test operations which take place within each test case, the most basic operation is to compare the output of the function being tested with an expected output. In order to do this we use the `expect` function with `matchers` such as `toBe`, `not.toBe` or `toEqual`. You can use many different matchers based on what you wish to test, such as matchers for thruthines, numbers, strings, arrays and objects, etc. Refer the [Jest documentation](https://jestjs.io/docs/using-matchers) to learn more about matchers. You can have as many expect calls required within your test cases.

Jest also works with asynchronous code and you can read about handling promises and asyn/await based code [here](https://jestjs.io/docs/asynchronous).

If you remember the Arrange-Act-Assert principle, you may sometimes need to arrange a few configurations or execute a few initial steps before running your tests. This is also called setup and can be done using the `beforeAll()` or `beforeEach()` functions. Similarly, you can also teardown your initial configurations after your tests finish running. Read more about setup and teardown [here](https://jestjs.io/docs/setup-teardown).

Now that you have a basic understanding of how to use Jest, let's look at some examples of testing using Jest. These are the cases you will also be practicing in your assignments for this module.