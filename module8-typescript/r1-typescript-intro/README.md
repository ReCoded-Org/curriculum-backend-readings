# TypeScript

In this module, we'll learn about [TypeScript](https://www.typescriptlang.org/),
a superset of the JavaScript programming language developed by Microsoft. You may be
familiar with the basic concept of types from JavaScript or another programming
language. In TypeScript, these types are more strongly enforced. For example,
you cannot add together a number and a string (`1 + "foo"`) as you would in
JavaScript. We'll examine the benefits of this throughout this module.

For example, in the following code in TypeScript, notice that the `user.name`
field does not exist (only `user.firstName`, `user.lastName`).

```
const user = {
  firstName: "Angela",
  lastName: "Davis",
  role: "Professor",
}
 
console.log(user.name)
```

Actually, TypeScript won't even allow you to run this code: you'll get an error.

```
Property 'name' does not exist on type '{ firstName: string; lastName: string;
role: string; }'.
```

We'll learn to understand such error messages and write type-safe code using
TypeScript, in addition to understanding why TypeScript has become so popular.


While following along in this module, you can play around with some of the code by using the
[TypeScript playground](https://www.typescriptlang.org/play). You can also
install the TypeScript compiler locally by running `npm install -g typescript`.

## What is static typing and compilation?
JavaScript is **dynamically typed** and **interpreted** programming language.
In general, both of these mean that little preprocessing is done before running
JavaScript code.

When we say JavaScript is dynamically typed, it means that JavaScript variables have types, such as string, boolean,
number, but these are determined at the time that the code is run -- not
beforehand.

As an interpreted progamming language, the source code is not
preprocessed, and code is interpreted, or executed, from human-readable code to
things that the machine understands at the time that it runs.

You may have noticed that there is an error with types in your JavaScript code
-- say you tried to add an array and a number together -- this error will not be
caught until the time that the code is run. This is a consequence of being both
dynamically typed and interpreted; we are allowed to add together two types that
don't make sense (what does it mean to add a list to a number?) and the error
only appears if we run the code. 

TypeScript is a **compiled** and **statically typed** language. In a statically typed language, the types of a variable are known at the
time that the code is written, not just when the code runs. In a compiled
language, code needs to go through another program, called the compiler,
before it can be run. While many languages compile, or "translate", from human readable code to
machine code, TypeScript actually compiles to JavaScript, though it's not very
readable.

## Why TypeScript?

### Reducing bugs
Have you ever made any of these mistakes in JavaScript and had to spend a
nontrivial amount of time to fix them?

* Called a function with the wrong number of arguments: `twoArgFunction(x)`
* Called a function with too many arguments: `oneArgFunction(x, y)`
* Tried to get the index of a non-array type: `someString[5]`
* Indexed an array with the wrong type, rather than a number: `someArray["foo"]`
* Had a variable be `null` or `undefined` when you thought that it wasn't
* `undefined is not a function`

With TypeScript, these bugs (and many more) are easily caught at compile-time with a useful
error message. In the next section, we'll take a look at some examples of such
error messages and how they can easily help you track issues.

Static typing is often considered advantageous for scaling codebases. When
working in a large product (or even a small one), it saves everyone time and
development effort if as many mistakes can be caught *before* the code is run,
not afterwards. Compiled and typed languages certainly are not guaranteed to be
bug-free, but in general, by the time you run the code, you will have fewer bugs
than interpreted languages. In a post-mortem analysis by Airbnb from their
attempt to migrate their whole codebase to TypeScript, they estimated that [38%
of their bugs were preventable by
TypeScript](https://youtu.be/P-J9Eg7hJwE?t=711).

### Autocomplete
In addition to the benefits of using types to help reduce the number of bugs,
static types also allow for stronger auto-complete in editors, since, for
example, the allowable function calls and variable names that can be typed in a
certain place will be known even before the code will
run. 

### Refactoring
Having types makes refactoring code much easier. For example, if you are
renaming a function, editors can use statically known information about types to
rename all instances of that function in a single click. This is not possible
with JavaScript; in the absence of type information, the editor cannot know
ahead of time whether two function calls named `myFunction()` are really the
exact same function, or whether they are two different functions in different
files that happen to have the same name.

This is only one example, but in general, TypeScript allows you to refactor code
with less risk of breaking things.

### Disadvantages
However, compiling is an extra step in the process, and in large codebases, it
can take some time to compile the code (though speeding up compilers is a focal
point of compiler teams). You can read more about some of the tradeoffs between static and dynamic types
[in this article](https://instil.co/blog/static-vs-dynamic-types/).


## Basic Types

### Primitives
JavaScript has three primitive types -- `string`, `number`, `boolean` -- and they are present in TypeScript as
well.

Below, let's compare some JavaScript and TypeScript declarations of basic
variables.

```
// JavaScript
const graduatingYear = 36;
const isInBootcamp = true;
const name = "Foo Bar";
```

Now in TypeScript, when we declare a variable, ;q


### Arrays

### Functinos


### Avoiding `any`
