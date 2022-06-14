# Everyday Types

Without any further ado, let us now dive into the different Types that we can use in our codebases. The objectives of this lesson are:
1. Viewing practical usage examples of Types
2. Understanding when to use Types

We'll start by reviewing the most basic and common types you might encounter when writing JavaScript or TypeScript code. These will later form the core building blocks of more complex types.

## Type Annotations on Variables
When you declare a variable using `const`, `var`, or `let`, you can optionally add a type annotation to explicitly specify the type of the variable:

```typescript
let myName: string = "Alice";
```

TypeScript doesn't use "types on the left"-style declarations like `int x = 0`; Type annotations will always go after the thing being typed.

In most cases, though, this isn’t needed. Wherever possible, TypeScript tries to automatically infer the types in your code. For example, the type of a variable is inferred based on the type of its initializer:

```typescript
// No type annotation needed -- 'myName' inferred as type 'string'
let myName = "Alice";
```

## Primitives
JavaScript has three primitive types -- `string`, `number`, `boolean` -- and they are present in TypeScript as well. You can declare them just as you would in JavaScript. However, in TypeScript, you may *optionally* add a type. As mentioned previously, in most cases TypeScript can infer the type correctly.


```typescript
// TypeScript infers the type.
const name = "Foo Bar";
const age = 36;
const isInBootcamp = true;

// However, if you would like, you can explicitly write the types
// after the variable names. In most cases, this is not necessary,
// but it may be helpful if you are getting an error message.
const name: string = "Foo Bar";
const age: number = 36;
const isInBootcamp: boolean = true;
```

What does it mean when TypeScript is type-safe? Let's try adding together a number and a string in both JavaScript and TypeScript:

```typescript
// JavaScript: prints "1foo"
console.log(1 + "foo");

// TypeScript: gives an error
console.log(1 + "foo");
```

## Arrays
The syntax for arrays in TypeScript is again no different than JavaScript. However, typing becomes more important here. To declare an array of some type, we use the notation `string[]`, `number[]`, and so on. You can also use the syntax `Array<string>`, `Array<number>`, and so on. There is no difference. Note that this is the syntax for referring to the **type** of the variable, 

We'll go through a few examples.

### Inferred array types
TypeScript will infer the type of an array if it is declared with some value initially. For example, we have an array of numbers below; TypeScript is smart enough to figure out that `ids` has type `number[]`. 

```typescript
const ids = [1, 2, 3];
ids.push("somestring");
```

This gives an error, which tells us that we can't push a string to the parameter (of the `push` function) that expects type `number`. TypeScript has inferred that this is an array of numbers.

```
Argument of type 'string' is not assignable to parameter of type 'number'.
```

### Limits of inference
If there is no initial value, TypeScript is, unfortunately, not smart enough to figure out the type of an array. For example:

```typescript
// No type is declared on the array. TypeScript doesn't know
// what type the members are. This code passes, and anything
// can be pushed into the array (not very helpful for type safety).
const ids = [];
ids.push("somestring");
ids.push(5);
ids.push({})
```

TypeScript believes that the members of the array can be any type (formally: type `any`, which will be discussed later).

If you plan on declaring an empty array, this is an instance where you would want to explicitly specify the type in order to receive type-safety:

```typescript
// This will give an error if you try to push a string to the array this time.
const ids: number[] = [];
ids.push(5);
```

The `number[]` indicates that this will be an array of numbers. Similarly you could have `string[]` or `boolean[]`.

## Any
TypeScript also has a special type, `any`, that you can use whenever you don't want a particular value to cause typechecking errors. It is useful when you don't want to write out a long type just to convince TypeScript that a particular line of code is okay.

```typescript
let x: any = 'Hello';
let arr: any[] = [1, true, 'Hello']
```

When a value is of type `any`, you can access any properties of it (which will in turn be of type `any`), call it like a function, assign it to (or from) a value of any type, or pretty much anything else that’s syntactically legal.

```typescript
let obj: any = { x: 0 };
// None of the following lines of code will throw compiler errors.
// Using `any` disables all further type checking, and it is assumed 
// you know the environment better than TypeScript.
obj.foo();
obj();
obj.bar = 100;
obj = "hello";
const n: number = obj;
```

Beginners of TypeScript are often tempted to use `any` type, but it is highly discouraged. It is possible in almost all cases to write code without `any`. Do not use `any` as a crutch in order to skip past type errors: doing so is often a sign that something else is wrong with the code (and `any` is simply being used to ignore the fundamental issue).

When the keyword `any` is used, TypeScript no longer performs typechecking, since it has no information about the type. This means that we no longer have the benefits of the type-checker.

Here is an example of typing something as `any`, demonstrating how we can start introducing errors in our code that were previously prevented:

```typescript
const a: any = [1, 2, 3, 4, 5];
const invalidAddition = a + 5;  // Adding a list to a number?
const functionDoesntExist = a.someInvalidFunction(); // This also compiles!
```

Some valid usages of `any` might be: facilitating migration of code from JavaScript to TypeScript, leveraging third-party code without types, working with input of completely unknown structure.

## Tuples
Sometimes you may have an array whose elements are of different types. This is usually not encouraged, but it is possible. TypeScript allows type definitions for mixed arrays or tuples. You could even have an array of tuples.

```typescript
// Tuple
let person: [number, string, boolean] = [1, 'Alice', true]
// Tuple Array
let employees: [number, string][]
employees = [
  [1, 'Alice'],
  [2, 'Johnny'],
  [3, 'Davis'],
]
```

If you're wondering how is a tuple different from an `any[]`, tuples have a fixed type for each element even if not the same type for all elements. But when you state an array of `any` there could be as many different elements of different types.

```typescript
// This tuple would give an error because the third element
//is expected to be a boolean but is assigned a string
let employee: [number, string, boolean] = [1, 'Alice', 'Developer']
// These cases are all acceptable because
// the elements be of any type
let manager: any[]
manager = [3, 'Hello', true, 'Angela']
manager = [1, 2, 3]
manager = [false, 'Hello']
```

## Functions
Functions are the primary means of passing data around in JavaScript. TypeScript allows you to specify the types of both the input and output values of functions. In TypeScript, you can also use both the `function` keyword or arrow functions, but you must add types to the parameters. And where required you can add return type annotations too. 

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

Note the addition of three number types: the two parameters `x`, `y`, and the return type `number`. You may omit the return type sometimes if TypeScript is able to infer it, but it's also good practice to keep it in so that readers of your functions, such as your team mates, can immediately know at a glance what type should be returned from the function.

It should be noted that in TypeScript every parameter is required unless specified by adding a `?` after the parameter. In JavaScript, if a function has three declared parameters, you can choose not to provide them, and they will take the value of `undefined`. This is not the case in TypeScript.

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

In the example above, the second parameter, `lastName`, is optional. This is because it is written as `lastName?: string`. Note that this is equivalent to declaring it as `lastName: string | undefined` (the question mark is equivalent syntax).

### Anonymous functions
Anonymous functions are a little bit different from function declarations. When a function appears in a place where TypeScript can determine how it's going to be called, the parameters of that function are automatically given types.

```typescript
// No type annotations here, but TypeScript can spot the bug
const names = ["Alice", "Bob", "Eve"];
 
// Contextual typing for function
names.forEach(function (s) {
  console.log(s.toUppercase());
});
 
// Contextual typing also applies to arrow functions
names.forEach((s) => {
  console.log(s.toUppercase());
});
```

Typescript would flag an error `Property 'toUppercase' does not exist on type 'string'. Did you mean 'toUpperCase'?` in the above example. Even though the parameter `s` didn't have a type annotation, TypeScript used the types of the `forEach` function, along with the inferred type of the array, to determine the type `s` will have. This process is called contextual typing because the context that the function occurred within informs what type it should have.

We learned how to write types on a function, but it's very common in JavaScript to pass functions as values. For example, using `map`, `reduce`, or any type of callback, a function accepts another function as a parameter. Let's look at how to write the type of such a function.

Consider a function that takes another function that operates on numbers (consider this a version of `map`, that, for the sake of example, only works on numbers).

```typescript
// Takes a list of numbers and applies a processor function to each number
function mapNumbers(nums: number[], fn: (x: number): number) {
  return nums.map(fn);
}
```

Note the syntax here to declare a function type. You must add the parameter names, even in the types. The parameter `fn` has the type `(x: number): number`. It takes one parameter `x` of type `number`, and it returns a `number` as a result.

## Unions
A union type is a type formed from two or more other types, representing values that may be any one of those types. We refer to each of these types as the union's members.

```typescript
let id: string | number
// This is valid
id = 22
// This is also valid
id = '22'
```

It's easy to provide a value matching a union type - simply provide a type matching any of the union's members. If you have a value of a union type, how do you work with it? TypeScript will only allow an operation if it is valid for every member of the union. For example, if you have the union `string | number`, you can`t use methods that are only available on `string`:

```typescript
function printId(id: number | string) {
  console.log(id.toUpperCase());
Property 'toUpperCase' does not exist on type 'string | number'.
  Property 'toUpperCase' does not exist on type 'number'.
}
```

The solution is to narrow the union with code, the same as you would in JavaScript without type annotations. Narrowing occurs when TypeScript can deduce a more specific type for a value based on the structure of the code. For example, TypeScript knows that only a `string` value will have a `typeof` value `"string"`:

```typescript
function printId(id: number | string) {
  if (typeof id === "string") {
    // In this branch, id is of type 'string'
    console.log(id.toUpperCase());
  } else {
    // Here, id is of type 'number'
    console.log(id);
  }
}
```

## Objects
Apart from primitives, the most common sort of type you'll encounter is an object type. This refers to any JavaScript value with properties, which is almost all of them! To define an object type, we simply list its properties and their types.

For example, here's a function that takes a point-like object:

```typescript
// The parameter's type annotation is an object type
function printCoord(pt: { x: number; y: number }) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
printCoord({ x: 3, y: 7 });
```

Here, we annotated the parameter with a type with two properties - `x` and `y` - which are both of type `number`. You can use `,` or `;` to separate the properties, and the last separator is optional either way. The type part of each property is also optional. If you don't specify a type, it will be assumed to be `any`.

Object types can also specify that some or all of their properties are optional. To do this, add a `?` after the property name:

```typescript
function printName(obj: { first: string; last?: string }) {
  // ...
}
// Both OK
printName({ first: "Bob" });
printName({ first: "Alice", last: "Alisson" });
```

In JavaScript, if you access a property that doesn't exist, you'll get the value undefined rather than a runtime error. Because of this, when you read from an optional property, you'll have to check for undefined before using it.

```typescript
function printName(obj: { first: string; last?: string }) {
  // Error - might crash if 'obj.last' wasn't provided!
  console.log(obj.last.toUpperCase());

  if (obj.last !== undefined) {
    // OK
    console.log(obj.last.toUpperCase());
  }
 
  // A safe alternative using modern JavaScript syntax:
  console.log(obj.last?.toUpperCase());
}
```

## Type Aliases
We've been using object types and union types by writing them directly in type annotations. This is convenient, but it's common to want to use the same type more than once and refer to it by a single name. A type alias is exactly that - a name for any type. The syntax for a type alias is:

```typescript
type Point = {
  x: number;
  y: number;
};

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}
 
printCoord({ x: 100, y: 100 });
```

## Null and Undefined
JavaScript has two primitive values used to signal absent or uninitialized value: `null` and `undefined`. TypeScript has two corresponding types by the same names. How these types behave depends on whether you have the `strictNullChecks` option on. We'll learn more about how to configure this setting in a later section of this module.

With `strictNullChecks` off, values that might be `null` or `undefined` can still be accessed normally, and the values `null` and `undefined` can be assigned to a property of any type. This is similar to how languages without null checks (e.g. C#, Java) behave. The lack of checking for these values tends to be a major source of bugs; it is always recommended to turn `strictNullChecks` on if it's practical to do so in their codebase.

With `strictNullChecks` on, when a value is `null` or `undefined`, you will need to test for those values before using methods or properties on that value. Just like checking for `undefined` before using an optional property, we can use narrowing to check for values that might be null:

```typescript
function doSomething(x: string | null) {
  if (x === null) {
    // do nothing
  } else {
    console.log("Hello, " + x.toUpperCase());
  }
}
```

TypeScript also has a special syntax for removing `null` and `undefined` from a type without doing any explicit checking. Writing `!` after any expression is effectively a type assertion that the value isn't `null` or `undefined`:

```typescript
function liveDangerously(x?: number | null) {
  // No error
  console.log(x!.toFixed());
}
```

## Enums
Enums are a feature added to JavaScript by TypeScript which allows for describing a value which could be one of a set of possible named constants. Unlike most TypeScript features, this is not a type-level addition to JavaScript but something added to the language and runtime. Because of this, it's a feature which you should know exists, but maybe hold off on using unless you are sure.

```typescript
// Up is initialized with 1
// All of the following members are auto-incremented from that point on
// Up = 1 Down = 2 Left = 3 Right = 4
enum Direction1 {
  Up = 1,
  Down,
  Left,
  Right,
}

// String enum with all string values defined
enum Direction2 {
  Up = 'Up',
  Down = 'Down',
  Left = 'Left',
  Right = 'Right',
}

// Number enum
enum UserResponse {
  No = 0,
  Yes = 1,
}

// heterogeneous enum
enum BooleanLikeHeterogeneousEnum {
  No = 0,
  Yes = "YES",
}
```

## Conclusion
You would mostly find yourself using primitive types, arrays, objects and functions in your everyday code. TypeScript powers all of these elements with static typing and type checking. You have now learned the syntax for type annotations and assertions. You have also learned about how Typescript infers types and applies contextual typing. You can get creative and use Tuples, Unions, Enums, and Any types but of course these require a lot more thought and consideration put in first. You can also create your own type aliases and reuse them wherever required across the codebase. With that, let's prepare ourselves to look at more complex and advanced types in the next lesson.

---

## References
- https://www.typescriptlang.org/docs/handbook/2/everyday-types.html
- https://www.youtube.com/watch?v=BCg4U1FzODs&ab_channel=TraversyMedia
- https://dev.to/hiro9108/javascript-vs-typescript-why-we-should-learn-typescript-4d5o