# Introduction to TypeScript

Now that you have been working with JavaScript for some time, you must have heard of TypeScript which is described in short as JavaScript with syntax for Types. It is very popularly used in the tech industry these days for both frontend and backend development. Before we learn more about backend, we will familiarize ourseleves with TypeScript and how it can be used in backend code through this module. The objectives of this lesson are:
1. Understanding how and why TypeScript was created
2. Analyzing the pros and cons of using TypeScript in our projects

## Story of TypeScript
As per the [2021 Stackoverflow Developer Survey](https://insights.stackoverflow.com/survey/2021#technology-most-popular-technologies), JavaScript completed its ninth year in a row as the most commonly used programming language. However, it is not the [most loved programming language](https://insights.stackoverflow.com/survey/2021#most-popular-technologies-language) because TypeScript ranks 3rd in this list compared to JavaScript at the rank 15th. TypeScript is also the 2nd most wanted language followed by JavaScript.

TypeScript is a young programming language with its story going back only to 2012. It was launched for public use in October 2012, as the version 0.8 of the language. It was a result of two years of development at Microsoft, with Anders Hejlsberg, the lead architect of C#, as well as the creator of Delphi and Turbo Pascal working on the project too. This team at Microsoft wanted to do something like [Dart](https://dart.dev/) but they took a different approach. Instead of reinventing the language with a completely new syntax, they just amended the JavaScript syntax. Not only that, but they also made this new syntax optional. This is how TypeScript was born.

That means any JavaScript program is a valid TypeScript program. Due to this reason, TypeScript is also called the **superset of JavaScript**. You might have heard somebody saying TypeScript is just **JavaScript with types**.

You may be familiar with the basic concept of types from JavaScript or another programming language. In TypeScript, these types are more strongly enforced. For example, you cannot add together a number and a string (`1 + "foo"`) as you would in JavaScript. We'll examine the benefits of this throughout this module.

For example, in the following TypeScript code, notice that the `user.name` field does not exist (only `user.firstName`, `user.lastName`).

```typescript
const user = {
  firstName: "Angela",
  lastName: "Davis",
  role: "Professor",
}
 
console.log(user.name)
```

Actually, TypeScript won't even allow you to run this code: you'll get an error.

```bash
Property 'name' does not exist on type '{ firstName: string; lastName: string; role: string; }'.
```

We'll learn to understand such error messages and write type-safe code using TypeScript, in addition to understanding why TypeScript has become so popular. While following along in this module, you can play around with some of the code by using the [TypeScript playground](https://www.typescriptlang.org/play).

## Pros and Cons of TypeScript
As mentioned previously, TypeScript is a superset of JavaScript. This means that:
1. It offers additional features to JavaScript such as static typing.
2. Using types is completely optional.
3. It compiles down to regular JavaScript.
4. It can be used for frontend JS as well as backend with Node.js.
5. It includes most features from ES6.
6. Types from third party libraries can be added with type defintions.

In case you're wondering, what do we mean by "types"? In programming languages, a type system is a logical system comprising a set of rules that assigns a property called a type to the various constructs of a computer program, such as variables, expressions, functions or modules.

Let's imagine a JS program running in the browser (or on Node.js). Being a dynamically typed language, JavaScript will not throw any errors when data type changes for the same variable. At first, the data type of the variable `x` could be a `number`, then a `string` when the value `'hello'` is assigned to it and then a `boolean` when `true` is assigned to it. So all these types are determined at the runtime.

What TypeScript did was to provide a compiler that can process a program and throw errors if it detects something odd with the program. This compiler is also called a transpiler since it outputs the cleaner JavaScript program. To use this compiler, we should right the code in a `.ts` file instead of a `.js`, of course after installing TypeScript (using npm).

What TypeScript expects are the Type Annotations. A Type Annotation is an indication of the data type of a value. For example, the variable `x` can be annotated with `:string`. This annotation provides the data type of variable `x` to the TypeScript compiler. When the TypeScript compiler sees this, it assumes that `x` will be a string during the lifetime of this program. So, if we assign an initial value of `1` which is a number, it is not going to be valid and it will complain about it in the compilation error messages. Once we fix all the issues, TypeScript will generate the output file `sameFileName.js` that is safe to run wherever we want. TypeScript keeps the original filename of the source file and only replaces the extension. The goal of TypeScript is to catch mistakes in a program before it goes to production and causes problems at the runtime. Its goal is not to provide tools to amend or modify the original source code (business logic) such that can it perform well at the runtime in all the situations.

### Dynamic vs Static Typing
In dynamically typed languages, the types are associated with run-time values and not named explicitly in your code. For example, JavaScript, Python, Ruby, PHP.

JavaScript is a **dynamically typed** and **interpreted** programming language. In general, both of these mean that little preprocessing is done before running JavaScript code. When we say JavaScript is dynamically typed, it means that JavaScript variables have types, such as string, boolean, number, but these are determined at the time that the code is run -- not beforehand. As an interpreted progamming language, the source code is not preprocessed, and code is interpreted, or executed, from human-readable code to things that the machine understands at the time that it runs. You may have noticed that there is an error with types in your JavaScript code -- say you tried to add an array and a number together -- this error will not be caught until the time that the code is run. This is a consequence of being both dynamically typed and interpreted; we are allowed to add together two types that don't make sense (what does it mean to add a list to a number?) and the error only appears if we run the code. 

In statically typed languages, you explicitly assign types to variables, function paramters, return values, etc. For example, Java, C, C++, Rust, Go.

TypeScript is a **compiled** and **statically typed** language. In a statically typed language, the types of a variable are known at the time that the code is written, not just when the code runs. In a compiled language, code needs to go through another program, called the compiler, before it can be run. While many languages compile, or "translate", from human readable code to machine code, TypeScript actually compiles to JavaScript, though it's not very readable.

You can read more about some of the tradeoffs between static and dynamic types [in this article](https://instil.co/blog/static-vs-dynamic-types/).

### Advantages of TypeScript
1. Makes your code more robust. All your variables can be defined with types.
2. Helps you easily spot bugs. Research says that 15% of commonly occuring bugs can be caught at compile time itself by TypeScript.
3. Improves predictability. If you've defined a variable to a string, it will stay a string.
4. Enhances readability. If you're working with multiple developers, TypeScript makes your code more expressive and self-explanatory and enforces a guideline to be followed by the team.
5. Growing popularity. As we discussed above, TypeScript is growing in popularity in the industry so it is a marketable skill to add to your resume.

### Disadvantages of TypeScript
1. More code to write. Sometimes you need the work to be done fast, but TS would involve more code than plain JS for many cases which can add to development time.
2. More to learn. If you've been coding with JS for a while, it would take time to learn TS and sometimes this is what holds some companies back from refactoring their codebases because they cannot dedicate time for learning.
3. Required compilation. TypeScript needs to be transpiled into JavaScript in the end to be understood by browsers and servers. Luckily most popular frameworks today have TS compilation easily configurable.
4. Not true static typing. Because TypeScript is compiled down to regular JavaScript, some developers criticize that it is not a true statically typed language as JavaScript is dynamically typed. So in a way it gives a false sense of type safety.

Looking at these advantages and disadvantages, and also if you've been doing some reading online by yourself you will find that there are different opinions about TypeScript. Some developers claim that any JS code should be written in TypeScript and TypeScript only, while some believe it is actually not that beneficial. And then there are some in between who are flexible and open to the ideas of with or without TypeScript.

Generally speaking it is best not to form any unshakable opinions about a language or framework in an ever evolving and improving industry. It is always good to learn a new skill, language or framework. So understand the benefits of TypeScript and be prepared to write TypeScript if the company you work for decides to adopt it in their tech stack.

## TypeScript in frontend and backend

We've learned quite a bit about TypeScript and why it makes JavaScript even better. Let's understand this in action with frontend and backend code. TypeScript is compatible with most modern frontend frameworks like React or Next.js. If you're familiar with JSX in React, to use TypeScript you would create a `.tsx` file instead. Let's look at an example of a `Header.tsx` file.

```js
export interface Props {
  title: string
  color?: string
}

const Header = (props: Props) => {
  return
    <header>
      <h1 style ={{ color: props.color ? props.color : 'blue}}>
        {props.title}
      </h1>
    </header>
}
```

Here we have created a Header component that takes in two props `title` and `color`. We have defined the prop types using TypeScript and indicated that the `title` should have type string and the `color` is an optional prop but should also have type string.

So now when we want to have a Header component on a page:

```js
<Header />
<Header title='Hello World' />
<Header title='Hello World' color='red' />
```

The first case will give us an error within our IDE stating that the prop title is missing. The second case will be compiled and executed to display a header with the words 'Hello World' in blue since we provided blue color as the default when prop color is not provided. And you can predict what happens in the third case too.

Typescript is also very compatible on the backend, you can have `.ts` files in your Node Express projects or use a backend framework like NestJS which has Typescript incorporated in. We will learn more about this framework in an upcoming lesson, let's take a look at another Typescript example useful for backend.

```js
type User = {
  name: string;
  age: number;
};

function isAdult(user: User): boolean {
  return user.age >= 18;
}

const justine: User = {
  name: 'Justine',
  age: 23,
};

const isJustineAnAdult: boolean = isAdult(justine);
```

First part with `type` keyword is responsible for declaring our custom type of objects representing users. Later we utilize this newly created type to create function `isAdult` that accepts one argument of type `User` and returns `boolean`. After this we create `justine`, our example data that can be used for calling previously defined function. Finally, we create new variable with information whether `justine` is an adult or not. So now if by mistake we had set the `age` on `justine` to something other than a `number`, Typescript would flag the issue and prevent us from shipping code that could work unexpectedly.

There are additional things about this example that you should know. Firstly, if we would not comply with declared types, TypeScript would alarm us that something is wrong and prevent misuse. Secondly, not everything must be typed explicitly - TypeScript is very smart and can deduce types for us. For example, variable `isJustineAnAdult` would be of type `boolean` even if we didn't type it explicitly or `justine` would be valid argument for our function even if we didn't declare this variable as of `User` type.

So looking at these above code examples, here are some strong advantages of TypeScript in both frontend and backend.

### Reducing bugs
Have you ever made any of these mistakes in JavaScript and had to spend a nontrivial amount of time to fix them?

* Called a function with the wrong number of arguments: `twoArgFunction(x)`
* Called a function with too many arguments: `oneArgFunction(x, y)`
* Tried to get the index of a non-array type: `someString[5]`
* Indexed an array with the wrong type, rather than a number: `someArray["foo"]`
* Had a variable be `null` or `undefined` when you thought that it wasn't
* `undefined is not a function`

With TypeScript, these bugs (and many more) are easily caught at compile-time with a useful error message. Static typing is often considered advantageous for scaling codebases. When working in a large product (or even a small one), it saves everyone time and development effort if as many mistakes can be caught *before* the code is run, not afterwards. Compiled and typed languages certainly are not guaranteed to be bug-free, but in general, by the time you run the code, you will have fewer bugs than interpreted languages. In a post-mortem analysis by Airbnb from their attempt to migrate their whole codebase to TypeScript, they estimated that [38% of their bugs were preventable by TypeScript](https://youtu.be/P-J9Eg7hJwE?t=711).

### Autocomplete
In addition to the benefits of using types to help reduce the number of bugs, static types also allow for stronger auto-complete in editors, since, for example, the allowable function calls and variable names that can be typed in a certain place will be known even before the code will run. 

### Refactoring
Having types makes refactoring code much easier. For example, if you are renaming a function, editors can use statically known information about types to rename all instances of that function in a single click. This is not possible with JavaScript; in the absence of type information, the editor cannot know ahead of time whether two function calls named `myFunction()` are really the exact same function, or whether they are two different functions in different files that happen to have the same name. This is only one example, but in general, TypeScript allows you to refactor code with less risk of breaking things.

## Conclusion
Typescript is growing in popularity everyday in the industry. It brings some significant benefits and improvements to the development process, but also comes with a few concerns that need to be considered before deciding to use the language. In any case, it makes JavaScript even more powerful through static typing and is a marketable skill to add to any develoepr's resume. It is used both on frontend and backend and helps developers write cleaner and less error prone code as it detects issues much before runtime. We shared some syntax examples in this lesson, but now let's take a deeper dive into the different Type Annotations of TypeScript and their uses in the next lesson.

---

## References
- https://www.cleverism.com/skills-and-tools/typescript
- https://medium.com/jspoint/typescript-a-beginners-guide-6956fe8bcf9e
- https://tsh.io/blog/why-use-typescript
- https://nodejs.dev/learn/nodejs-with-typescript
- https://dev.to/hiro9108/javascript-vs-typescript-why-we-should-learn-typescript-4d5o
- https://www.youtube.com/watch?v=BCg4U1FzODs&ab_channel=TraversyMedia