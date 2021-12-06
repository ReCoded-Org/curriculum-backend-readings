# Introduction to testing

We are now moving into the advanced concepts of backend web development. However, at this point of the bootcamp these concepts should not be completely unfamiliar to you either. You have seen what tests look like and how they're executed in all your previous assignments. Now it's time to understand them in detail. The objectives of this lesson are:
1. Understanding tests and their importance
2. Getting familiar with the syntax of test code

## What is a test?

In programming, a test refers to a piece of code that can be run to verify the
behavior of a program. For example, if you write a function, and you want to be
sure that it works for various inputs and outputs, you can write a test for this
function.

Tests themselves are also code. At larger companies, every piece of submitted code
needs to submitted with a corresponding test. A general rule of thumb is that,
if by mistake you change a line of your code so that the behavior is wrong, a test
somewhere should fail, so that such a mistake can be caught.

Tests are an important part of many companies' infrastructure for development.
Generally, humans are not manually running these tests, though you may manually
run some tests before sending a pull request or while working on the test itself. In a process called **continuous integration** (CI), these tests will usually automatically run after every pull request is proposed. This means that generally, if your code and pull request are not passing the tests, it cannot be merged in until fixed.

There are many types of tests: unit tests, integration tests, smoke tests,
and so on. In a later section, we will talk about some of these types of tests.
Most commonly, we will refer to unit tests, which are the most frequent type of
tests.

## Why is testing important?

You may think it is sufficient simply to manually test your code.

There are a few reasons testing is very important when it comes to a growing
codebase. You should not imagine the situation where you are working on a
project with one or two people, but a situation where you are working with a
larger team and with a codebase that the company will use even long after you leave. You
may not be at the company five years later, or you may at times forget what the code does
in six months. This is where tests come in to make developers' lives easier as it mainly helps to catch bugs in time and hold us accountable towards high quality error-free code.

### Correctness
Most obviously, a test is used to verify the correctness of the code. If you
have ever changed your code then had to test three or more cases manually, then
you are familiar with the fact that it is quite cumbersome to repeatedly check
manually. Not only that, it's very easy to forget to check some case when a
human is doing it by hand.

In contrast, when you write a test, you simply need to run a command in order to
initiate the tests again, rather than repeating some steps to ensure that your
code is working.

If you work at a company with a practice of code reviews, consider the perspective of the
person reviewing your code: How do they know your code doesn't have bugs? How do
they know it works correctly? If your code is submitted along with tests, the
reviewer can be aware of exactly what you have or haven't verified about your
code.

### Ease of change
Have you ever felt scared to change code, because you weren't sure if it would still work for all the cases after you changed it? With a good test suite, this fear generally
doesn't exist. Even if the code is rewritten but the same tests pass, indicating
that the new code has the same behavior, one can feel a lot more secure about
rewriting the code.

Having good tests allows code to be changed in a more robust fashion. When the
same tests pass, a developer can be more sure (perhaps not completely sure,
depending on the tests) that changing the code did not break anything.
Additionally, it allows people who are not familiar with the code (say, your
teammates who work on related code, or someone who is responsible for your code
five years later) to more easily work with the code.

### Documentation
A well-written test suite serves as documentation. Again, imagine you have just
joined a company, and you don't know what a function or file does. In fact, if you want to understand what a piece of code does, it's often more productive to go read the
tests first, rather than the code itself. You must have done this while working on your assignments from previous modules.

In the next section, we'll look at an example of a test, which will help illustrate how the tests themselves can be used to document the code.

## Example code

Let's now take a look at some example code for tests. Even if you don't know much about testing frameworks, you'll find that tests are actually quite readable anyway.

Let's take a look at this example from [Jest](https://jestjs.io), one of the most popular testing frameworks in JavaScript. Most testing frameworks work in approximately the same fashion, simply using different syntax.

```js
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
  });
```

What does this test do? -- To start off, consider what a function called `sum`
should do. Even though we can't see the implementation, this is an example of
how simply reading the test can tell you how the function should behave.

In this test, when the sum function is given the arguments `sum(1, 2)`, we call
a function `expect` and assert the result `toBe` `3`. Even above that, there is
a descriptive string (anything can be written there), that tells us that the test checks for `adds 1 + 2 to equal 3`. Again, even though we have no idea how sum is written internally (although in this case, writing such a function should be quite trivial), **only from reading the test**, the behavior of the function is documented in some fashion.

Let's continue reading some tests, without even looking at the implementation of the tested functions for illustrative purposes.

In this example, let's look at the function `absolute`. You may be able to guess
what the function does from the name, but if not, read the code below, and try
to figure out what it does.

```js
describe('absolute', () => {
    it('should return positive number if input is positive', () => {
        const result = absolute(1);
        expect(result).toBe(1);
    });
    it('should return positive number if input is negative', () => {
        const result = absolute(-1);
        expect(result).toBe(1);
    });
    it('should return zero if input is zero', () => {
        const result = absolute(0);
        expect(result).toBe(0);
    });
});
```

In this example, the `describe` function is used to group together a related set
of tests. Note how the code almost reads like a written description of the
behavior of the test.

Finally, let's read one more example of a slightly more complex test. Let's look at a pice of code from the tests of the Express.js Meme API assignment. Hope you haven't forgotten it yet! Even if you have or if you don't understand the specific syntax or function calls, the important part is to try to read the test and see how it helps us understand the behavior of the functionality being tested.

```js
describe("GET /memes/filter", () => {
    it("responds with empty array for non-matching genre", (done) => {
        const genre = "random";
        const expectedOutput = [];
        request(app)
        .get("/memes/filter?genre=" + genre)
        .set("Accept", "application/json")
        .expect("Content-Type", /json/)
        .expect(200, (err, res) => {
            if (err) return done(err);
            expect(res.body).to.be.an("array");
            expect(res.body).to.deep.equal(expectedOutput);
            done();
        });
    });

    it("responds with error message when invalid parameter is passed", (done) => {
        const genre = "";
        const expectedOutput = "invalid query parameter";
        request(app)
        .get("/memes/filter?genre=" + genre)
        .set("Accept", "application/json")
        .expect("Content-Type", /json/)
        .expect(400, (err, res) => {
            if (err) return done(err);
            expect(res.body).to.equal(expectedOutput);
            done();
        });
    });
});
```

Try to answer the following questions about the above example:
* Which piece of functionality is being tested here?
* How many scenarios are being tested?
* What is the expected output in each scenario?

By reading the tests in this section, you should have a more concrete understanding of what tests may look like, how they verify correctness, and how they help others understand the behavior of a function. In the next lesson, we will understand a little more about the philosophy and mindset of testing.
