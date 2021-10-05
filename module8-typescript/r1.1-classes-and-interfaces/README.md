# Classes and Interfaces
In TypeScript, classes are similar to JavaScript, with some syntactic
differences and more powerful features. In this module, we will examine classes and discuss interfaces, a
concept of object-oriented programming that does not exist in JavaScript.

This module assumes familiar with the basic ideas of classes and object-oriented
programming.

## Classes

### Class members
Let's take a look at a basic example of a class with some members. Class members will sometimes be referred to as fields or instance variables.
These are all equivalent terminology. In this example, the members are `x`, `y`.

```typescript
class Point {
  x: number;
  y: number;
}
     
const pt = new Point();
pt.x = 0;
pt.y = 0;
```

### Field properties
A field of a class can be one of the following: `public`, `private`, `protected`, or
`readonly`.

- `public`: This field can be read to and written as normal.
- `private`: Only accessible by the instance of the class. For example, this
    variable cannot be accessed by any code other than the functions in the
    class.
- `protected`: Similar to `private`, but subclasses can access the field.
- `readonly`: This field can only be read, but it can never be assigned or have
    its value changed (similar to `const`).

In general, it is considered good practice in coding to use the minimal visibility
required. For example, if you never plan to write to the field, you should start
with `readonly`. If you find that you need to write to the field, but only in
the code in the class, you should use `private`. Usage of `protected` is
rare. In most cases, well-structured code will have most instance variables of a
class as `private`.

Let's take a look at an example of a field with the `readonly` keyword:
```typescript
class File {
  readonly name: string = "untitled";
 
  constructor(otherName?: string) {
    if (otherName !== undefined) {
      this.name = otherName;
    }
  }
 
  err() {
    this.name = "not ok, the field is readonly";
  }
}
```

However, this will give you an error:
```
Cannot assign to 'name' because it is a read-only property.
```

And an example of a field with the `private` keyword, which disallows access
from outside of the class.
```typescript
class Counter {
  private x = 0;

  increment() {
  // This is ok.
    x = x + 1;
  }
}
const ctr = new Counter();

// This code is outside of the class. It is not accessible.
console.log(ctr.x);
```

This code too, results in a useful error: 
```
Property 'x' is private and only accessible within class 'Counter'.
```

### Static members
In some cases, you want to keep information related to the class as a whole,
regardless of a particular instance of a class. TypeScript, like JavaScript,
provides the `static` keyword. these can also use the same modifiers such as
`public`, `private`, etc.

```typescript
class StaticExample {
  static x = 0;
  static printStatic() {
    console.log(StaticExample.x);
  }
}

console.log(StaticExample.x);

// Notice how there is no instantiation with the `new` keyword.
// We are simply accessing the value from the name of the class,
// not an instance of the class.
StaticExample.printStatic();
```

### Inheritance

Like JavaScript, the `extends` keyword can be used to create a subclass of a
class.

```typescript
class RecodedMember {
  getTitle() {
    return "Generic member";
  }
}

class RecodedStudent {
  getTitle() {
    return "Student";
  }
}
 
const member : RecodedMember = new RecodedMember();
console.log(member.getTitle()); // "Generic member"

// Note how, because this is a subclass, we can also use the type of the parent
// class here, if we would like.
const student: RecodedMember = new RecodedStudent();
console.log(student.getTitle()); // "Student"
```

## Interfaces
TypeScript provides a powerful object-oriented concept called interfaces, using
the `interface` keyword. In TypeScript, and interface represents the type of an
object. In some other languages, an interface is similar to a class, but without
its implementation. In TypeScript, it can also be used this way.

You may have heard the word interface elsewhere. The term itself generically
refers to something that we interact with. As a result, it makes sense, for
example, to refer to the interface of an API. We see the interface of an API,
but we do not know its implementation. We simply call the endpoints on the API;
and a "clean interface" is one that hides its implementation from the user.

This concept is more generally called [information
hiding](https://en.wikipedia.org/wiki/Information_hiding), and it applies in
many areas in computer programming. For example,
at the levels of API design, where we talk about endpoints, and for classes,
when we talk about concrete code.

For further information, refer to the [official
documentation](https://www.typescriptlang.org/docs/handbook/2/objects.html).


### Object types
In JavaScript and TypeScript, it is extremely common to organized and pass
around data as objects.

For example:

```typescript
// Takes a point, and returns a new point with its values increased by one.
function shift(point: { x: number, y: number }): { x: number, y: number } {
  return { x: point.x + 1, y: point.y + 1 };
}
```

But what if we have multiple functions that want to use such a type? Already in
the above, we see that it's quite clunky to keep writing out this object type. In this
case, interfaces come in handy.

```typescript
interface Point {
  x: number;
  y: number;
}
 
function shift(point: Point): Point {
  return { x: point.x + 1, y: point.y + 1 };
}
```

You may also achieve the same thing using a type alias, or the `type` keyword.
Note that when using the `type` keyword, an equals sign is required -- a slight
syntactic difference.
```typescript
type Point = {
  x: number;
  y: number;
}

const origin: Point = { x: 0, y: 0 };
```

Similar to parameters, you can specify optional properties that may be
undefined, using a `?`:

```typescript
type Point = {
  x: number;
  y: number;
  // This is an optional property.
  z?: number;
}
```

### Extending interfaces
The power of interfaces is that it defines a high-level idea of a set of fields
or methods. Similar to classes and inheritance, interfaces can be extended in
TypeScript.

```typescript
interface Colorful {
  color: string;
}
 
interface Circle {
  radius: number;
}
 
interface ColorfulCircle extends Colorful, Circle {}
 
const cc: ColorfulCircle = {
  color: "red",
  radius: 42,
};
```

In the example above, we have two iterfaces: `Colorful` and `Circle`. If we want
a `ColorfulCircle`, we do not need to rewrite the fields; instead, we can reuse
the two interfaces, combining them using the `extends` keyword.

## Further reading
This module covers much of the syntax available for classes in TypeScript.
However, there are also many other quality-of-life features available that can
be found in the [official
documentation](https://www.typescriptlang.org/docs/handbook/2/classes.html) for
classes.
