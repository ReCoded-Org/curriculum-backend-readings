# Advanced Types
In this module, we will cover some advanced types in TypeScript.

## Enums
Enumerated types (also known as enums or enumerations) are a feature of TypeScript that is not present
explicitly in JavaScript. Enumerations are useful to represent a set of fixed
constants, and they are usually preferable to [magic
strings](https://en.wikipedia.org/wiki/Magic_string) in order to achieve this.

For example, we may want to use an enum to represent the possible types of
subscriptions in an application, given that our hypothetical app only supports
four possible types of plans. If we need to support more later, then we can add
to the enum.

```typescript
enum SubscriptionType {
  ONE_MONTH,
  TWO_MONTH,
  THREE_MONTH,
  ONE_YEAR
}
```

They are useful anywhere we have a fixed set of items that need to be
represented:
```typescript
enum Theme {
  DARK,
  LIGHT,
  GREY
}
```

And they can often be combined with switch-cases:
```typescript
function getPrimaryColor(userTheme: Theme) {
  switch (userTheme) {
    case Theme.DARK:
      return "black";
      return "white";
    case Theme.GREY:
      return "grey";
    // Fall back to light theme in case of unsupported theme,
    // perhaps caused by developer error of forgetting to support the
    // enum in this function.
    case Theme.LIGHT:
    default:
      return "blue";
  }
}
```

## Intersection types
Previously, we discussed union types, such as `string | undefined`, meaning that
a value could be either of type `string` or type `undefined`. However, an
intersection type instead *combines* all of the given types.


```typescript
 
## `void`
The `void` type is used to represent the absence of any return type. Usually,
providing the return type is optional, so you will not have to explicitly write
it out. `console.log()` is an example of a well-known function with a `void`
return type: the return type is never used. 

For example, a function that does only logging might have a return type of of
`void`: 

```typescript
function warnUser(): void {
  console.log("This is my warning message");
}
```

## Utility types

### Partials
The `Partial<T>` type takes a type `T` but makes all of its properties optional. That
is, none of the types will be required on the resulting type.

```typescript
// Note how the fields are required in this type.
interface FullName {
  firstName: string;
  lastName: string;
}

const optionalLastName: Partial<FullName> = { firstName: "Foo" };
```

In contrast, the `Required<T>` type takes a type `T`, but all types must be
provided.

```typescript
interface Person {
  firstName: string;
  // Note the optional field.
  lastName?: string;
}

const needsLastName: Required<Person> = { firstName: "Foo" };
```

This gives an error:
```
Property 'lastName' is missing in type '{ firstName: string; }' but required in
type 'Required<Person>'.
```

TypeScript provides a number of similar utility types that derive from another
type, such as `Readonly` (makes a type read-only, disallowing assignment), `Pick`
(taking only certain fields), and so on. The full list of [utility
types is available in the documentation](https://www.typescriptlang.org/docs/handbook/utility-types.html).
