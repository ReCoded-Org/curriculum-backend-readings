# Testing Philosophy
Let's discuss some aspects of testing philosophy. The objectives of this lesson are:
1. Understanding the philosophy and mindset of testing
2. Familiarizing ourselves with the concepts of TDD and BDD
3. Learning the properties of a good test

## Mindset of Testing
In real life, you may perhaps work at companies that do almost no testing (this is not good, but it is the reality). This is especially true in smaller companies. You may work at a company that chooses only to test certain components or write certain types of tests. Finally, as mentioned previously, at some companies, especially bigger ones, you
may be required to write tests so that every line of code is covered by a test.

Simply writing a test is not sufficient: there are also good and bad ways to
write tests. In the sections ahead, we'll consider some additional factors about
the testing process and the quality of tests. However, how is the mindset of testing different from the mindset of development? In fact, is it different at all?

Many companies do have a quality assurance or QA team that is responsible for testing a product or application manually as it is getting developed. And then there are developers who are responsible specifically for writing automated tests. These professionals are expected to have a strong analytical mind with critical thinking skills. They are also expected to have empathy for the end users and test the application from their perspective in different scenarios. Wait a minute, isn't all this also expected from developers building the application? Yes, but more often than not there is a difference between a developer and a tester. Developers want to make the application work but testers want to make the application break. No, that does not make testers just a bunch of terrible people, although the programming meme world is full of developers complaining against them. By consistently and curiously looking for faults or failures in the application, testers help to ensure the application can be made as free of errors as possible, which at the end of the day ensures the users are able to use the application efficiently.

<img src="../assets/developer-tester.jpeg">

More recently with the arrival of many different testing frameworks, the distinction between development and QA has been removed, as companies started to see the value of developers who can also write good tests. Developers are now expected to look at all scenarios and test cases of the functionality they're building and write tests to validate the correctness of their code. This brings us to the concept of the test-driven development which is gaining more popularity.

## Test-driven Development

**Test-driven development** (TDD) is a process where developers write the tests first,
**before** writing the code. As we saw in the last lesson, the tests alone can
be sufficient for specifying the behavior of the function.

Even to modify existing code, a test would be written first under this
philosophy. For example, if you had an `if` statement in your code already, but
you wanted to add an `else` branch, under TDD, you would first write a test for
that `else` branch, and then write the actual code. As mentioned before, at the
highest levels of testing, a mistake in any line of code should be caught, and
TDD facilitates this.

### Why TDD?

Firstly, TDD requires the developer to first think about the behavior of the tested code and how it will be used, rather than rushing head-first into writing the code. Perhaps you may have experienced writing code and realizing later that the code you wrote was not quite what you needed. When you think carefully first about the behavior of the code as in TDD, this situation is often avoided.

Secondly, as developers must write tests with every code, TDD requires developers
to write tests and puts developers in the habit of writing tests, which is
generally healthy for the robustness of a codebase. If TDD was not present,
depending on the company, developers may be less strict about writing tests.

### Is TDD used in the real world?
Many companies do adopt TDD, although in practice, this is still a minority of
companies. TDD is far from a perfect philosophy: it does not guarantee good test
coverage and it may even encourage developers to write sloppier tests so that
they can simply start coding faster.

However, as with all things in life, understanding the perspective of TDD is still extremely useful. TDD is on the very rigorous end of the role of testing in
development. In reality, you will probably end up somewhere in between --
perhaps sometimes you will think about the tests first, or you will think in
your head about what will be tested, even though you may not be required to
actually write the tests as you would in TDD.

The reason that understanding or trying test-driven development is helpful is
because even if you do not work at a company that adopts test-driven
development, it will encourage you to think about success and failure cases
while you write your code. **This is a crucial part of the programmer's
mindset.** As you become a more experienced programmer, you will try to predict
issues; test-driven development aids greatly with this mindset, since it
encourages you to write the test and think about these scenarios before writing
the code.

[Behaviour-driven development](https://en.wikipedia.org/wiki/Behavior-driven_development) or BDD is a concept that emerged from TDD. In BDD, tests are more user-focused and based on the system's behavior. [Mocha](https://mochajs.org/) is a popular JavaScript framework for writing behaviour-driven tests. You've seen it in practice in the tests for your assignments. BDD usually follows the "Given-When-Then" formula.

_Given_ a certain scenario

_When_ an action takes place

_Then_ this should be the outcome

For example:

_Given_ the user has not entered any data on the form

_When_ they click the submit button

_Then_ proper validation messages should be shown

## Properties of a good test
As mentioned previously, simply writing a test is not the same as writing a good
test. In this section, we'll examine some properties of what makes a good test.

### Size: Focused tests
A well-written test should not test too many things at once. In general, test
cases should be well-isolated and have a [single responsibility](https://en.wikipedia.org/wiki/Single-responsibility_principle) or intention.

Consider the previous example of the `absolute()` function. Suppose the test
instead looked like this:
```js
describe('absolute', () => {
    it('should correctly handle inputs', () => {
        const result1 = absolute(1);
        expect(result0).toBe(1);
        const result1 = absolute(-1);
        expect(result1).toBe(1);
        const result2 = absolute(0);
        expect(result2).toBe(0);
    });
});
```

Now compare this to the original. Which one do you find more readable and
organized? While this is a simple example, separating the cases for clarity
becomes especially important with more complex functions.
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

### Redundancy: Avoid overlapping test cases
As a related topic, you usually want to avoid test cases that overlap too much
with existing test cases. For example, consider the following test case for the
`absolute` function. Is it useful, or is it redundant, overlapping with one of the test cases above?

```js
it('should return positive number if input is large and negative', () => {
    const result = absolute(-100);
    expect(result).toBe(100);
});
```

This case is redundant. Testing `absolute(-1)` and `absolute(-100)` separately is not very useful; the two test cases overlap. We want to avoid this.

It is often asked how much overlap is okay. Inevitably, some test cases will
overlap with each other. There is no correct answer here: just know that some
overlap is okay, but you want to do your best to avoid redundancy by selecting
test cases that are representative of the cases of your function.

In the programmer's mindset, usually there are a set of possible scenarios to consider.
For example, in the case of the `absolute()` function, there are three distinct
scenarios that define the behavior: positive, negative, and zero. Whether the
negative number is large or not makes no difference.

### Thoroughness
In this module, it was mentioned several times that good test coverage means
that, if the code is behaving incorrectly, even in one line or in one
if-condition, some test will fail.

A common problem with tests is that some case is missing. Perhaps when certain
arguments are passed to your function, it behaves differently. A good suite of
tests will make sure to cover all the different possible cases.

### Organization: Arrange-Act-Assert
Tests generally follow approximately the same pattern, and this has been
crystallized in a commonly adopted idea called ["Arrange Act Assert."](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)
1. **Arrange**: Many tests require some type of intial setup before the tests can be executed. Does the test require any inputs or special settings? Does it need to prep a database? Does it need to log into a web app? Handle all of these operations at the start of the test in the Arrange step.
2. **Act**: In the Act step, the actual behavior being tested should be invoked, such as a function call, a REST API call, an interaction with a web page, a component render, etc.
3. **Assert**: Finally, to ensure correctness, Assert the expected outcomes after the Act step sends a result or response. This was seen earlier using the `expect` function. The terms expect and assert, in this context, are synonymous. Assertions are what ultimately determine if the test passes or fails.

_Given-When-Then_ is essentially the same formula as _Arrange-Act-Assert_.

## Additional Readings
1. You can read more about the testing mindset on [this forum](https://club.ministryoftesting.com/t/what-does-testing-mindset-mean-to-you-whats-your-tester-mindset/26422).
2. You can read more about the advantages and disadvantages of TDD [here](https://www.geeksforgeeks.org/advantages-and-disadvantages-of-test-driven-development-tdd/).
3. This [StackOverflow question](https://stackoverflow.com/questions/61400/what-makes-a-good-unit-test) gives some interesting insights into what are considered good properties of a unit test.

Google has a good resource called *Testing on the Toilet*. On the back of the
door in every toilet stall at Google, you can find a one-page flyer that
describes some aspect of testing (that's how important testing is!). These are
publicized. Some good ones for junior developers are included below:
- [Keep tests focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html)
- [DAMP](https://www.googblogs.com/testing-on-the-toilet-tests-too-dry-make-them-damp/). Don't overuse functions in test code, focus on readability.
- [Just say no to end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html). Avoid overusing tests that connect too many parts of your system.

Finally, take a look at [this comprehensive list](https://github.com/goldbergyoni/javascript-testing-best-practices) of best practices for testing in JavaScript and Node.js. Don't worry about memorizing all of this, expose yourself to these ideas and concepts first and then put them into practice in your assignments and projects. You'll find yourself remembering them easily soon.