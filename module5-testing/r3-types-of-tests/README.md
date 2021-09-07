# Types of tests
The examples we've seen so far are examples of **unit tests**. As the name
suggests, unit tests test a small unit of code, such as a function or a
component. However, often times we want tests that do different types of
assertion or test overall parts of the system.

We will discuss briefly some other types of tests without going too far
in-depth. 

## Integration and end-to-end tests
Multiple parts of a system or a whole system can be tested in **integration and end-to-end tests**. An example of this would be a test that starts a frontend and a backend, and tests that the frontend registration form works and inserts something in a database. Notice how this would be much different from a unit test, for example, that simply tests whether a registration form properly sends a fetch request to the correct URL (without actually triggering anything in the backend).

While it's tempting to write only end-to-end tests, thinking that it would be
convenient to test all parts at once, these are much harder to
maintain, as you need to set up a backend, a database, and a frontend in a test
environment and have them all work together. There are also more places where
the test could go wrong, which violates our principle of keeping tests isolated.
Later, we will discuss the frequency at which different tests can be written.

Note that integration tests
 may also be referred to as end-to-end tests, or vice-versa. In general, the
line between the categories of tests are arbitrary and blurred. That is, people
may use different terms to refer to the same types of tests, as there is not
necessarily an "official naming" for tests.

## Screenshot testing
In mobile and web apps, it is common to use **screenshot testing**, sometimes
known as **visual testing**. For example, in JavaScript and web apps, you can
use a [Jest
extension](https://bonitasoft.medium.com/automated-visual-regression-testing-with-typescript-puppeteer-jest-and-jest-image-snapshot-2250348bb334)
to achieve this.

In screenshot testing, there is generally a golden image. The golden image is
the "correct" appearance of the component under test. The first time a test is
run, the golden image will be created, if it doesn't exist. Any subsequent test
will take a screenshot of the component and compare it to the golden image. If
the actual screenshot does not match the expected (golden) screenshot, the test
will fail.

This can be very useful in cases that cannot be asserted in code. For example,
it's difficult to test and assert things about CSS positioning on web. To have
an automated test for this, screenshot testing is a viable option.

## Smoke tests
**Smoke tests** are a type of end-to-end test that tests the most basic cases.
For example, if you have a todo list app, this app may simply login users and
try to create a list, even if your app has much more functionality than this
straightforward flow.

However, the name "smoke test" comes from the idea that, if you have some type
of hardware and there is smoke, you should probably immediately shut it off
without testing anything -- it hasn't even passed the basics. Smoke tests often
run before releasing a product as a "sanity test."

## Frequency
In the ideal testing environment, unit tests . As tests increase in granularity
-- that is, they include larger pieces of your system -- you want these tests to
be less frequent. The smaller tests should tested individually. In case there is
a problem, it becomes easier to isolate if the tests are associated with small
tests.

There is a [test
pyramid](https://martinfowler.com/articles/practical-test-pyramid.html) that is
frequently cited when discussing testing. While the components of the test
pyramid may vary based on the author of the diagram, the important thing is that
the fastest and smallest test (unit tests) should be by far the most frequent.
As tests take longer to run and integrate more parts of the system, there should
be fewer.

![Test pyramid](assets/test-pyramid.png)
