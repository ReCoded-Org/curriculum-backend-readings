# Advanced Types

We have learnt quite a bit about Types so far, but when it comes to large scale projects there are some more advanced types that help us write more robust code which will dive into now. The objectives of this lesson are:

1. Viewing practical usage examples of advanced Types
2. Understanding when to use advanced Types

## Interfaces

An interface declaration is another way to name an object type. Interfaces can be used interchangeably with type aliases and simple object types.

```typescript
interface Point {
  x: number;
  y: number;
}

function printCoord(pt: Point) {
  console.log("The coordinate's x value is " + pt.x);
  console.log("The coordinate's y value is " + pt.y);
}

printCoord({ x: 100, y: 100 });
```

Just like when we used a type alias above, the example works just as if we had used an anonymous object type. TypeScript is only concerned with the structure of the value we passed to `printCoord` - it only cares that it has the expected properties.

You can also define properties in an interface to be optional using `?` or non-editable by specifying `readonly`.

```typescript
interface UserInterface {
  readonly id: number;
  name: string;
  age?: number;
}

const user1: UserInterface = {
  id: 1,
  name: "John",
};
```

Interfaces can be used with functions as well.

```typescript
interface MathFunc {
  (x: number, y: number): number;
}

const add: MathFunc = (x: number, y: number): number => x + y;
const sub: MathFunc = (x: number, y: number): number => x - y;
```

## Classes

TypeScript offers full support for the class keyword introduced in ES2015. As with other JavaScript language features, TypeScript adds type annotations and other syntax to allow you to express relationships between classes and other types. Just like any other OOP language, classes have members or fields and a constructor function used to instantiate the objects of this class with initial field values. Classes can also have member functions.

```typescript
// Class with constructor
class Person {
  id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  greet(message: string) {
    console.log(message + this.name);
  }
}

const alice = new Person(1, "Alice Green");
alice.greet("Hello");
```

You can use an `implements` clause to check that a class satisfies a particular interface.

```typescript
interface PersonInterface {
  id: number;
  name: string;
  register(): string;
}

class Person implements PersonInterface {
  id: number;
  name: string;

  constructor(id: number, name: string) {
    this.id = id;
    this.name = name;
  }

  register() {
    console.log(`${this.name} is now registered`);
  }
}

const alice = new Person(1, "Alice Green");
const mike = new Person(2, "Mike Jordan");

alice.register();
mike.register();
```

Classes may extend from a base class. A derived class has all the properties and methods of its base class, and also define additional members.

```typescript
class Employee extends Person {
  position: string; // additional member of this subclass

  constructor(id: number, name: string, position: string) {
    super(id, name);
    this.position = position;
  }
}

const emp = new Employee(3, "Shawn", "Developer");
emp.register();
```

A field of a class can be one of the following: `public`, `private`, `protected`, or
`readonly`.

- `public`: This field can be read to and written as normal.
- `private`: Only accessible by the instance of the class. For example, this variable cannot be accessed by any code other than the functions in the class.
- `protected`: Similar to `private`, but subclasses can access the field.
- `readonly`: This field can only be read, but it can never be assigned or have its value changed (similar to `const`).

By default all class members are `public` but you can apply other data modifiers like `private` and `protected` to control member visibility. Protected members are only visible to subclasses of the class they're declared in. Private is like Protected, but doesn't allow access to the member even from subclasses.

In general, it is considered good practice in coding to use the minimal visibility required. For example, if you never plan to write to the field, you should start with `readonly`. If you find that you need to write to the field, but only in the code in the class, you should use `private`. Usage of `protected` is rare. In most cases, well-structured code will have most instance variables of a class as `private`.

We've tried to cover the basics about Classes here. You can read a lot more in detail [on the TypeScript handbook](https://www.typescriptlang.org/docs/handbook/2/classes.html).

## Generics

Generics allow us to create reusable and flexible components which can work over a variety of types rather than a single one. This allows users to consume these components and use their own types.

```typescript
// Without generics
function getArray(items: any[]): any[] {
  return new Array().concat(items);
}

let numArray = getArray([1, 2, 3, 4]);
let strArray = getArray(["alice", "dave", "mike"]);

// With generics
function getArray<T>(items: T[]): T[] {
  return new Array().concat(items);
}

let numArray = getArray<number>([1, 2, 3, 4]);
let strArray = getArray<string>(["alice", "dave", "mike"]);
```

The drawback of using `any[]` is that something like `numArray.push('hello')` would not throw an error, but when you use generics it acts like a placeholder with types defined and applied when creating variables from the generic.

You can read more about generics and considerations for using this feature of TypeScript [on the TypeScript handbook](https://www.typescriptlang.org/docs/handbook/2/generics.html).

## Decorators

With the introduction of Classes in TypeScript and ES6, there now exist certain scenarios that require additional features to support annotating or modifying classes and class members. Decorators provide a way to add both annotations and a meta-programming syntax for class declarations and members. Decorators are a stage 2 proposal for JavaScript and are available as an experimental feature of TypeScript.

A Decorator is a special kind of declaration that can be attached to a class declaration, method, accessor, property, or parameter. Decorators use the form `@expression`, where `expression` must evaluate to a function that will be called at runtime with information about the decorated declaration. For example, given the decorator `@sealed` we might write the `sealed` function as follows:

```typescript
function sealed(target) {
  // do something with 'target' ...
}
```

You can read more about Decorators in detail [on the TypeScript handbook](https://www.typescriptlang.org/docs/handbook/decorators.html). You will most likely not use this in everyday projects as it is a very experimental feature, so we have only paraphrased the basics from the handbook and made you aware of the existence of this advanced type.

## Conclusion

Now we have taken a look at basic everyday types as well as complex advanced types. Were you able to visualize how these types being applied could help in reducing bugs in our code? Slowly you will start to get the hang of TypeScript with more practice. Let us now explore how the TypeScript compiler works in the next lesson.

---

## References

- https://www.youtube.com/watch?v=BCg4U1FzODs&ab_channel=TraversyMedia
- https://www.typescriptlang.org/docs/handbook/2/classes.html
- https://www.typescriptlang.org/docs/handbook/2/everyday-types.html#interfaces
- https://www.typescriptlang.org/docs/handbook/2/generics.html
- https://www.typescriptlang.org/docs/handbook/decorators.html
- https://gist.github.com/bradtraversy/f80a4cd87e7034bea5264f7d8c431b4e
