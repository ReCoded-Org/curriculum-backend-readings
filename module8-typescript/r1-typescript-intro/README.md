# TypeScript

In this module, we'll learn about [TypeScript](https://www.typescriptlang.org/),
a superset of the JavaScript programming language developed by Microsoft. You may be
familiar with the basic concept of types from JavaScript or another programming
language. In TypeScript, these types are more strongly enforced. For example,
you cannot add together a number and a string (`1 + "foo"`) as you would in
JavaScript. We'll examine the benefits of this throughout this module.

For example, in the following code in TypeScript, notice that the `user.name`
field does not exist (only `user.firstName`, `user.lastName`).

```typescript
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

You can declare them just as you would in JavaScript. However, in TypeScript,
you may *optionally* add a type. In most cases, however, TypeScript can infer
the type correctly.


```typescript
// TypeScript infers the type.
const age = 36;
const isInBootcamp = true;
const name = "Foo Bar";

// However, if you would like, you can explicitly write the types
// after the variable names. In most cases, this is not necessary,
// but it may be helpful if you are getting an error message.
const age: number = 36;
const isInBootcamp: boolean = true;
const name: string = "Foo Bar";
```

What does it mean when TypeScript is type-safe? Let's try adding together a
number and a string in both JavaScript and TypeScript:

```typescript
// JavaScript: prints "1foo"
console.log(1 + "foo");

// TypeScript: gives an error
console.log(1 + "foo");
```


### Arrays

The syntax for arrays in TypeScript is again no different than JavaScript.
However, typing becomes more important here. To declare an array of some type,
we use the notation `string[]`, `number[]`, and so on. You can also use the
syntax `Array<string>`, `Array<number>`, and so on. There is no difference. Note
that this is the syntax for referring to the **type** of the variable, 

We'll go through a few examples.

#### Inferred array types
TypeScript will infer the type of an array if it is declared with some value
initially. For example, we have an array of numbers below; TypeScript is smart
enough to figure out that `a` has type `number[]`. 

```typescript
const a = [1, 2, 3];
a.push("somestring");
```

This gives an error, which tells us that we can't push a string to the parameter
(of the `push` function) that expects type `number`. TypeScript has inferred
that this is an array of numbers.

```
Argument of type 'string' is not assignable to parameter of type 'number'.
```

#### Limits of inference
If there is no initial value, TypeScript is, unfortunately, not smart enough to
figure out the type of an array. For example:

```typescript
// No type is declared on the array. TypeScript doesn't know
// what type the members are. This code passes, and anything
// can be pushed into the array (not very helpful for type safety).
const a = [];
a.push("somestring");
a.push(5);
a.push({})
```

TypeScript believes that the members of the array can be any type (formally:
type `any`, which will be discussed later).

If you plan on declaring an empty array, this is an instance where you would
want to explicitly specify the type in order to receive type-safety:

```typescript
// This will give an error if you try to push a string to the array this time.
const a: number[] = [];
a.push(5);
```

#### Having arrays with multiple types
What if you did, for some reason, want to have an array that contains both
strings and numbers? (Note: this is discouraged, in practice you usually would
not want to mix the types of members of an array like this).

Here, we briefly look at [union
types](https://www.typescriptlang.org/docs/handbook/unions-and-intersections.html).
A union type is simply a type that could be one of many types. If a variable
could contain both a string and a number, we use the syntax `number | string`.
The `|` can be thought of as similar to a boolean "or" (`||`).

The following example shows an array that could contain both strings and
numbers:

```typescript
// No errors. 
const a: (number | string)[] = [];
a.push("somestring");
a.push(5);
```

### Functions

#### Writing functions
In TypeScript, you can also use both the `function` keyword or arrow functions,
but you must add types to the parameters.

```typescript
// Function keyword
function add(x: number, y: number): number {
  return x + y;
}

// Arrow function
const add = (x: number, y: number): number => {
  return x + y;
};

```

Note the addition of three number types: the two parameters `x`, `y`, and the
return type `number`. You may omit the return type sometimes if TypeScript is
able to infer it, but it's also good practice to keep it in so that readers of
your functions, such as your teammates, can immediately know at a glance what
type should be returned from the function.

It should be noted that in TypeScript every parameter is required unless
specified by adding a `?` after the parameter. In JavaScript, if a function has
three declared parameters, you can choose not to provide them, and they will
take the value of `undefined`. This is not the case in TypeScript.
In the example below, the second parameter, `lastName`, is optional. This is
because it is written as `lastName?: string`. Note that this is equivalent to
declaring it as `lastName: string | undefined` (the question mark is equivalent
syntax).

```typescript
// Return both the first name and last name if the last name is provided,
// otherwise return only the first name.
function makeName(firstName: string, lastName?: string) {
  if (lastName) {
    return firstName + " " + lastName;
  } else { 
    return firstName;
  }
}
```

#### Types of function values
We learned how to write types on a function, but it's very common in JavaScript
to pass functions as values. For example, using `map`, `reduce`, or any type of
callback, a function accepts another function as a parameter. Let's look at ohw
to write the type of such a function.

Consider a function that takes another function that operates on numbers
(consider this a version of `map`, that, for the sake of example, only works on
numbers).

```typescript
// Takes a list of numbers and adds five to every number.
function mapNumbers(nums: number[], fn: (x: number) => number) {
  return nums.map(fn);
}
```

Note the syntax here to declare a function type. You must add the parameter
names, even in the types. The parameter `fn` has the type `(x: number) =>
number`. It takes one parameter `x` of type `number`, and it returns a `number`
as a result.

### Avoiding `any`
In TypeScript, there exists a type called `any`, which represents any type.
Beginners of TypeScript are often tempted to use `any` type, but it is highly
discouraged. It is possible in almost all cases to write code without `any`. Do not use `any` as a
crutch in order to skip past type errors: doing so is often a sign that
something else is wrong with the code (and `any` is simply being used to ignore
the fundamental issue).

When the keyword `any` is used, TypeScript no longer performs typechecking,
since it has no information about the type. This means that we no longer have
the benefits of the type-checker.

Here is an example of typing something as `any`, demonstrating how we can start
introducing errors in our code that were previously prevented:

```
const a: any = [1, 2, 3, 4, 5];
const invalidAddition = a + 5;  // Adding a list to a number?
const functionDoesntExist = a.someInvalidFunction(); // This also compiles!
```

Some valid usages of `any` might be: facilitating migration of code from
JavaScript to TypeScript, leveraging third-party code without types, working
with input of completely unknown structure.


