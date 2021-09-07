# Properties of a good test
As mentioned previously, simply writing a test is not the same as writing a good
test. In this section, we'll examine some properties of what makes a good test.

## Size: Focused tests
A well-written test should not test too many things at once. In general, test
cases should be well-isolated and have a [single
responsibility](https://en.wikipedia.org/wiki/Single-responsibility_principle)
or intention.

Consider the previous example of the `absolute()` function. Suppose the test
instead looked like this:

```javascript
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

```javascript
describe('absolute', () => {
    it('should return positive number if input positive', () => {
        const result = absolute(1);
        expect(result).toBe(1);
    });
    it('should return positive number if input negative', () => {
        const result = absolute(-1);
        expect(result).toBe(1);
    });
    it('should return zero if input is zero', () => {
        const result = absolute(0);
        expect(result).toBe(0);
    });
});
```

## Redundancy: avoid overlapping test cases
As a related topic, you usually want to avoid test cases that overlap too much
with existing test cases. For example, consider the following test case for the
above. Is it useful, or is it redundant, overlapping with one of the test cases
above?

```javascript
it('should return positive number if input is large and negative', () => {
    const result = absolute(-100);
    expect(result).toBe(100);
});
```

This case is redundant. Testing `absolute(-1)` and `absolute(-100)` is not very
useful; the two test cases overlap. We want to avoid this.

It is often asked how much overlap is okay. Inevitably, some test cases will
overlap with each other. There is no correct answer here: just know that some
overlap is okay, but you want to do your best to avoid redundancy by selecting
test cases that are representative of the cases of your function.

In the
programmer's mindset, usually there are a set of possible scenarios to consider.
For example, in the case of the `absolute()` function, there are three distinct
scenarios that define the behavior: positive, negative, and zero. Whether the
negative number is large or not makes no difference.

## Thoroughness
In this module, it was mentioned several times that good test coverage means
that, if the code is behaving incorrectly, even in one line or in one
if-condition, some line will fail.

A common problem with tests is that some case is missing. Perhaps when certain
arguments are passed to your function, it behaves differently. A good suite of
tests will make sure to cover these cases.

## Organization: Arrange-Act-Assert
Tests generally follow approximately the same pattern, and this has been
crystallized in a commonly adopted idea called ["Arrange Act
Assert."](https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/)

1. **Arrange**: Many tests require some type of setup; the setup should come
   initially.
2. **Act**: In the act step, the actual behavior being tested should be invoked,
   such as a function call, an API call, a component render, etc.
3. **Assert**: Finally, to ensure correctness, assert the expected outcomes.
   This was seen earlier using the `expect` function. Expect and assert, in this
   context, are synonymous.

## Additional readings
This [StackOverflow
question](https://stackoverflow.com/questions/61400/what-makes-a-good-unit-test)
gives some interesting insights into what are considered good properties of a
unit test.

Google has a good resource called *Testing on the Toilet*. On the back of the
door in every toilet stall at Google, you can find a one-page flyer that
describes some aspect of testing (that's how important testing is!). These are
publicized. Some good ones for junior developers are included below:

- [Keep tests focused](https://testing.googleblog.com/2018/06/testing-on-toilet-keep-tests-focused.html)
- [DAMP](https://www.googblogs.com/testing-on-the-toilet-tests-too-dry-make-them-damp/). Don't overuse functions in test code, focus on readability.
- [Just say no to end-to-end tests](https://testing.googleblog.com/2015/04/just-say-no-to-more-end-to-end-tests.html). Avoid overusing tests that connect too many parts of your system.

