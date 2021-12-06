# Test Coverage
The objective of this lesson is to get a general idea about test coverage and its importance.

## What is test coverage?

Test coverage is defined as a metric in that measures the amount of testing performed by a set of tests. It includes gathering information about which parts of the codebase are executed when running the test suite to determine which branches of conditional statements have been taken.

In simple terms, it is a technique to ensure that your tests are testing your code or how much of your code you exercised by running the test.

If you had to manually calculate test coverage, here's a simple example:

If the number of lines of code in a system component is 500 and the number of lines executed across all existing test cases is 50, then your test coverage is: `(50 / 500) * 100 = 10%`

However, depending on the codebase size and structure, the formula can get more complicated.

## Why should we care about test coverage?

1. **Eliminates defects at early stages**: You can identify gaps in requirements, test cases and defects at early stages of your product development life cycle. It saves you from a lot of headaches later.

2. **Better coverage**: Test coverage creates more test cases to ensure superior coverage. This leads to fewer defects and work to do at later stages. Moreover, you get to increase customer satisfaction with a refined product.

3. **Removes redundant cases**: Test coverage is especially useful in identifying and eliminating test cases that don't make much sense in the current project. You can report these cases to remove them and make the overall code lighter.

4. **Discovers uncovered areas**: Test coverage helps you unearth areas of a program that have not been covered by a set of test cases. It helps make your program more robust and error-free.

5. **Superior control**: Test coverage gives you a better control over the resources during the product development lifecycle. You save time by eliminating defects earlier and faster. The saved time allows you to keep a tab of costs. And most importantly, you get to have a firm grip on the scope of the project.

6. **Smoother testing cycles**: You can prevent defect leakage using Test coverage analysis. Test coverage also helps in Regression testing, test case prioritization, test suite augmentation and test suite minimization. All this leads to smoother yet efficient testing cycles.

## What is a good test coverage?

It is absolutely not necessary to have 100% test coverage. Suppose your application has 50 features, and that when you run your tests, they exercise only 37 of those features. In this case, we could say that your tests cover 74% of the application. But if you can argue that the remaining 13 features are not critical, then 74% is still a good test coverage.

It usually depends on the type of application, its functional and non-functional requirements, time and effort and number of developers required to write tests - all together that help a company decide the right amount of test coverage for them.

In fact, sometimes you may even find that checking the test coverage leads to finding less important test cases and that might lead to reducing the test cases to get the right balance.

## How to measure test coverage?

If you're using Jest, you can simply run the command `jest --coverage` to get a tabular report of the code coverage of your project files. [Here](https://medium.com/@blturner3527/code-coverage-and-testing-with-jest-9641b5d0e0bc) is a simple tutorial about the same.

You can also use a tool called [Istanbul](https://istanbul.js.org/) which works with the Mocha framework to generate code coverage reports.

---
## References
- https://www.guru99.com/test-coverage-in-software-testing.html
- https://www.simform.com/blog/test-coverage/