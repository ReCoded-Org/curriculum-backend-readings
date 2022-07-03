# Types of tests

There are many many different types of software testing. The objectives of this lesson are:

1. Familiarize ourselves with common types of testing
2. Understand the concept of building test cases

## Manual and automated testing

At a high level, we need to make the distinction between manual and automated tests. Manual testing is done in person, by clicking through the application or interacting with the software and APIs with the appropriate tooling. This is very expensive as it requires someone to set up an environment and execute the tests themselves, and it can be prone to human error as the tester might make typos or omit steps in the test script.

Automated tests, on the other hand, are performed by a machine that executes a test script that has been written in advance. These tests can vary a lot in complexity, from checking a single function to making sure that performing a sequence of complex actions in the UI leads to the same results. It's much more robust and reliable than manual tests – but the quality of your automated tests depends on how well your test scripts have been written. Automated testing is a key component of continuous integration and continuous delivery and it's a great way to scale your QA process as you add new features to your application.

## Unit tests

The examples we've seen so far are examples of **unit tests**. As the name
suggests, unit tests test a small unit of code, such as a function or a
component. Unit tests are very low level, close to the source of your application. They consist of testing individual methods and functions of the classes, components or modules in your codebase. Unit tests are in general quite cheap to automate and can be run very quickly by a continuous integration server.

## Integration tests

Multiple parts of a system can be tested in integration tests. An example of this would be a test that starts a frontend and a backend, and tests that the frontend registration form works and inserts something in a database. Notice how this would be much different from a unit test, for example, that simply tests whether a registration form properly sends a fetch request to the correct URL (without actually triggering anything in the backend).

Integration tests verify that different modules or services used by your application work well together. These types of tests are more expensive to run as they require multiple parts of the application to be up and running.

## End-to-end tests

End-to-end testing replicates a user behavior in a complete application environment. While it's tempting to write only end-to-end tests, thinking that it would be
convenient to test all parts at once, these are much harder to maintain, as you need to set up a backend, a database, and a frontend in a test environment and have them all work together. There are also more places where the test could go wrong, which violates our principle of keeping tests isolated. Later, we will discuss the frequency at which different tests can be written.

Note that integration tests may also be referred to as end-to-end tests, or vice-versa. In general, the line between the categories of tests are arbitrary and blurred. That is, people may use different terms to refer to the same types of tests, as there is not
necessarily an "official naming" for tests.

## Functional tests

Functional tests focus on the business requirements of an application. They only verify the output of an action and do not check the intermediate states of the system when performing that action.

There is sometimes a confusion between integration tests and functional tests as they both require multiple components to interact with each other. The difference is that an integration test may simply verify that you can query the database while a functional test would expect to get a specific value from the database as defined by the product requirements.

## Regression tests

Every time a new module is added leads to changes in the program. This type of testing makes sure that the whole component works properly even after adding components to the complete program.

## Smoke tests

Smoke tests are basic tests that check basic functionality of the application. They are meant to be quick to execute, and their goal is to give you the assurance that the major features of your system are working as expected. For example, if you have a todo list app, this app may simply login users and try to create a list, even if your app has much more functionality than this straightforward flow.

The name "smoke test" comes from the idea that, if you have some type
of hardware and there is smoke, you should probably immediately shut it off
without testing anything -- it hasn't even passed the basics. Smoke tests often
run before more expensive tests can be run or before releasing a product as a "sanity test."

## Performance tests

Performance tests check the behaviors of the system when it is under significant load. These tests are non-functional and are aimed to understand the reliability, stability, and availability of the platform. For instance, it can be observing response times when executing a high number of requests, or seeing how the system behaves with a significant load of data.

## Stress tests

This is another type of non-functional test in which, we give unfavorable conditions to the system and check how it performs in those conditions. It helps us improve the system in the face of such possible unfavorable scenarios.

## Acceptance testing

Acceptance tests are formal tests executed to verify if a system satisfies its business requirements. They require the entire application to be up and running and focus on replicating user behaviors. These can also be manual tests, where first a round of alpha testing is conducted by an internal team and then a round of beta testing with a limited number of users for testing in a real-time environment.

---

## What is the frequency of these tests?

In the ideal testing environment, unit tests will be the most frequent type of
testing. As tests increase in granularity -- that is, they include larger pieces of your system -- you want these tests to be less frequent. The smaller tests should be tested individually. In case there is a problem, it becomes easier to isolate issues if they are associated with small tests.

![](../assets/test-pyramid.png)

There is a [test pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) that is frequently cited when discussing testing. While the components of the test
pyramid may vary based on the author of the diagram, the important thing is that
the fastest and smallest test (unit tests) should be by far the most frequent.
As tests take longer to run and integrate more parts of the system, there should
be fewer.

![](../assets/pyramid2.jpeg" width="70%)

---

## Test Cases

A test is only as strong as the number of test cases it covers. A test case represents a single scenario of the Given-When-Then principle applied to a functionality. It is very rare that a functionality would have only one test case.

Usually the first test case is called the **happy path** test case. Consider the example of a login form. Given the user enters the correct username and password, when they click the login button then the system should successfully login the user and take them to their dashboard. This is the most ideal scenario for the application which indicates that it is working as expected in the user requirements.

Sometimes there can be more than one ideal test case. Remember our example of the `absolute` function? We were testing for 3 scenarios: positive input, negative input and zero input. All these are valid cases that must be handled by the function correctly.

And now what about the other less than ideal scenarios? These are also very much possible to take place in the actual user behaviour with the application. For example, what if the user forgot to enter a username and directly hit the login button? Or what if the user misspelled their password? Or what if the user has not signed up in the first place and is entering a username not present in our database? The signup form must handle all these **edge cases**. Usually these test cases involve asserting for an appropriate error message to the user.

We can think of edge cases for our `absolute` function as well. What if the input is a string or character? In that case, our function must inform the user that it can only handle inputs that are numbers.

When we run the tests for a piece of functionality, we can see which test cases have passed and which have failed. This helps us debug the specific areas of the codebase and fix issues.

---

## References

- https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing
- https://www.geeksforgeeks.org/types-software-testing/
