# What is a test?
In programming, a test refers to a piece of code that can be run to verify the
behavior of a program. For example, if you write a function, and you want to be
sure that it works for various inputs and outputs, you can write a test for this
function.

Tests themselves are code. At larger companies, every piece of submitted code
needs to submitted with a corresponding test. A general rule of thumb is that,
if you change a line of your code so that the behavior is wrong, a test
somewhere should fail, so that such a mistake can be caught.

Tests are an important part of many companies' infrastructure for development.
Generally, humans are not manually running these tests, though you may manually
run it before sending a PR or while working on the test. In a process called
**continuous integration** (CI), these tests will automatically run after every
pull request is proposed. This means that generally, if your code and pull
request are not passing the tests, it cannot be merged in.

There are many types of tests: unit tests, integration tests, screenshot tests,
and so on. In a later section, we will talk about some of these types of tests.
Most commonly, we will refer to unit tests, which are the most frequent type of
tests.
