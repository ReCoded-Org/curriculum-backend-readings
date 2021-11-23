# Example code

In this section, we'll take a look at some example code for tests. It's possible
you've never seen a unit test before, but you'll find that they're actually
quite readable, even without knowing the framework.

Let's take a look at this example from
[Jest](https://jestjs.io/docs/getting-started), one of the most popular testing
frameworks in JavaScript. Most testing frameworks work in approximately the same
fashion, simply using different syntax.

```javascript
test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
  });
```

What does this test do? To start off, consider what a function called `sum`
should do. Even though we can't see the implementation, this is an example of
how simply reading the test can tell you how the function should behave.

In this test, when the sum function is given the arguments `sum(1, 2)`, we call
a function `expect` and assert the result `toBe` `3`. Even above that, there is
a written string (anything can be written there), that tells us that `adds 1 + 2
to equal 3`. Again, even though we have no idea how sum is written internally
(although in this case, writing such a function should be quite trivial), **only
from reading the test**, the behavior of the function is documented in some
fashion.

Let's continue reading some tests, without even looking at the
implementation of the tested functions for illustrative purposes.

In this example, let's look at the function `absolute`. You may be able to guess
what the function does from the name, but if not, read the code below, and try
to figure out what it does.

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

In this example, the `describe` function is used to group together a related set
of tests. Note how the code almost reads like a written description of the
behavior of the test.

Finally, let's read one more example of a slightly more complex test, written in
TypeScript. Again, understanding every line is not important, and some
implementations, such as `makeExpressRequest`, have been omitted. But the
important part is to try to read the test and see how it helps us understand the
behavior of a function.

```typescript
describe('makeExpressRequest()', () => {
  it('should return token when cookie token is provided', () => {
    const request = makeExpressRequest('111.222.333', null);
    expect(getToken(request)).toStrictEqual('111.222.333');
  });

  it('should extract token when bearer schema is provided', () => {
    const request = makeExpressRequest(null, 'Bearer xxx.yyy.zzz');
    expect(getToken(request)).toStrictEqual('xxx.yyy.zzz');
  });

  it('should throw error when the both are provided', () => {
    const request = makeExpressRequest('111.222.333', 'Bearer xxx.yyy.zzz');
    const expectToThrow = async () => getToken(request);
    expect.assertions(1);
    return expectToThrow().catch((e) => {
      expect(e).toBeDefined();
    });
  });

  it('should return null if none is provided', () => {
    const request = makeExpressRequest(null, null);
    expect(getToken(request)).toBeNull();
  });
});
```

Try to answer the following questions about the above example:
* What does the first argument to `makeExpressRequest` represent?
* What does the second argument represent?
* Are you supposed to pass in both arguments at once?
* If you pass in the second argument, what does it do to the argument?

By reading the tests in this section, this has given you a more concrete
understanding of what tests may look like, how they verify correctness, and how
they help others understand the behavior of a function.
