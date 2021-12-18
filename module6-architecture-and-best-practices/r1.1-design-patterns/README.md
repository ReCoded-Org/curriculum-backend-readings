# Software Design Patterns

Other than good system architecture, another critical aspect of developing robust applications is simply to write efficient and error-resilient code. This is where design patterns come into the picture. In simple words, design patterns are battle-tested and reusable solutions to common software design problems. The objectives of this lesson are:
1. Understanding the use of design patterns
2. Getting familiar with different types of design pattern concepts
3. Preparing to practice design patterns in our own codebases

## What are design patterns?

Here is the longer definition from Wikipedia: In software engineering, a software design pattern is a general, reusable solution to a commonly occurring problem within a given context in software design. It is not a finished design that can be transformed directly into source or machine code. Rather, it is a description or template for how to solve a problem that can be used in many different situations. Design patterns are formalized best practices that the programmer can use to solve common problems when designing an application or system.

Design patterns can speed up the development process by providing tested, proven development paradigms. Effective software design requires considering issues that may not become visible until later in the implementation. Freshly written code can often have hidden subtle issues that take time to be detected, issues that sometimes can cause major problems down the road. Reusing design patterns helps to prevent such subtle issues, and it also improves code readability for coders and architects who are familiar with the patterns.

## Types of Design Patterns

Design patterns had originally been categorized into 3 sub-classifications based on what kind of problem they solve. **Creational patterns** provide the capability to create objects based on a required criterion and in a controlled way. **Structural patterns** are about organizing different classes and objects to form larger structures and provide new functionality. **Behavioral patterns** are about identifying common communication patterns between objects and realizing these patterns.

You can look at the general definitions of the different design patterns on [this Wikipedia page](https://en.wikipedia.org/wiki/Software_design_pattern).

We recommend the following two learning paths to get an extensive understanding of design patterns in JavaScript and Node.js.
1. [JavaScript Design Patterns by Educative](https://www.educative.io/collection/5429798910296064/5725579815944192)
2. [JavaScript Design Patterns by Dofactory](https://www.dofactory.com/javascript/design-patterns)

Design patterns usually can be used across different programming languages, although some may not be relevant for specific languages. We are listing some of the most popular design patterns for JavaScript below. It is usually hard to understand design patterns without looking at their code examples, so feel free to use this as a checklist to search for more code examples and enhance your learning.

### Creational Patterns

1. **Factory**
The factory pattern wraps a constructor for different types of objects and returns instances of the objects via a simple API. It makes it easy to create different objects by exposing a simple API that return the specified object type.

Simple JavaScript example of using factory pattern : [Creating Laptop and Tablet objects using a Gadget Factory](https://medium.com/@thebabscraig/javascript-design-patterns-part-1-the-factory-pattern-5f135e881192)

2. **Builder**
Builder pattern provides a flexible solution for creating objects. It separates the construction of a complex object from its representation and builds a complex object using simple objects by providing a step by step approach.

Simple JavaScript example of using builder pattern : [Task Builder generating Task objects](https://zetcode.com/javascript/builderpattern/)

3. **Singleton**
A Singleton only allows for a single instantiation, but many instances of the same object. The Singleton restricts clients from creating multiple objects, after the first object created, it will return instances of itself.

Singletons are useful in situations where system-wide actions need to be coordinated from a single central place. An example is a database connection pool. The pool manages the creation, destruction, and lifetime of all database connections for the entire application ensuring that no connections are 'lost'.

Simple JavaScript example of using singleton pattern : [Printer Singleton for managing single printer access from multiple computers](https://www.digitalocean.com/community/conceptual_articles/singleton-design-pattern-in-javascript)

4. **Prototype**
The Prototype Pattern creates new objects, but rather than creating non-initialized objects. It returns objects that are initialized with values it copied from a prototype - or example - object. This is somewhat similar to the concept of Inheritance in object oriented programming. Javascript provides a [prototype syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain) in order to implement this.

Simple JavaScript example of using prototype pattern : [Creating Tesla model objects using prototypes](https://www.digitalocean.com/community/conceptual_articles/prototype-design-pattern-in-javascript)

5. **Dependency Injection**
Dependency injection (DI) is a programming pattern in which a dependency is passed using the parameters instead of instantiating it within the function or class. DI enables creating isolated individual components within application code and makes it easy to switch those dependencies in the future as the requirement changes. Passing parameters as a dependency also allows to easily unit test those components in isolation by injecting their mocked version.

Simple JavaScript example of using DI pattern : [Using Dependency Injection in using third-party library functions](https://dev.to/paularah/dependency-injection-in-javascript-1bfk)

6. **Object Pool**
The Object Pool design pattern is used in order to improve performance. It does that by reducing runtime memory allocation and garbage collection. You can read more about utlizing this design pattern [here](https://egghead.io/blog/object-pool-design-pattern).

### Structural Patterns

1. **Adapter**
The adapter pattern introduces an intermediary piece of code that makes two parts of a system compatible with one another. It also injects an element of lose coupling by keeping the two pieces of code separate. It means that you can write your code however you want without the need to take the other piece of code into consideration. Your adapter code will do the necessary translation and give you what you need and in whatever format you want. When one side of the code changes, you only need to change the adapter for that particular part rather than both sides of the application.

Simple JavaScript example of using Adapter pattern : [Build a shopping cart solution without touching the original shopping cart code](https://www.dottedsquirrel.com/adapter-pattern-javascript/)

2. **Bridge**
The bridge pattern is another ideological abstraction that keeps the boundaries of your code clean and separated. While it has similarities with the adapter pattern, it is not quite the exact same. The bridge pattern can be seen as an extension of the adapter pattern — or commonly known as the double adapter pattern.

This pattern allows two components, a client and a service, to work together with each component having its own interface. Bridge is a high-level architectural pattern and its main goal is to write better code through two levels of abstraction. It facilitates very loose coupling of objects. An example of the Bridge pattern is an application (the client) and a database driver (the service). The application writes to a well-defined database API, for example ODBC, but behind this API you will find that each driver's implementation is totally different for each database vendor (SQL Server, MySQL, Oracle, etc.).

3. **Composite**
The composite pattern is used to structure objects in a tree-like hierarchy. Here, each node of the tree can be composed of either child node(s) or be a leaf (no children objects). This pattern allows the client to work with these components uniformly; that is, a single object can be treated exactly how a group of objects is treated.

This pattern allows the formation of deeply nested structures. If a leaf object receives the request sent by the client, it will handle it. However, if the recipient is composed of children, the request is forwarded to the child components.

Simple JavaScript example of using Composite pattern : [Employee objects structured in composite pattern](https://www.educative.io/collection/page/5429798910296064/5725579815944192/6597912462098432)

4. **Decorator**
The decorator pattern focuses on adding properties, functionalities, and behavior to existing classes dynamically. The additional decoration functionalities aren’t considered essential enough to be a part of the original class definition as they can cause clutter. Hence, the decorator pattern allows modifying the code without changing the original class.

Simple JavaScript example of using Decorator pattern : [Add flavors and toppings to frozen yoghurt object](https://www.educative.io/collection/page/5429798910296064/5725579815944192/5660180910964736)

5. **Facade**
In English, the word "facade" means a deceptive front or appearance. Following this definition, a facade structural pattern provides a simpler interface that hides the complex functionalities of a system. The facade pattern allows you to hide all the messy logic from the client and only display the clear and easy to use interface to them. This allows them to interact with an API easily in a less error-prone way and without accessing the inner workings directly.

Simple JavaScript example of using Facade pattern : [Ordering food at a restaurant](https://www.educative.io/collection/page/5429798910296064/5725579815944192/6046230397321216)

6. **Flyweight**
It is a structural pattern that focuses on the sharing of data amongst related objects. It helps prevent repetitive code, hence, increases efficiency when it comes to data sharing as well as conserving the memory.

It takes the common objects that are used a lot and stores them in an external object (flyweight) for sharing; you could say that it is used for caching purposes. So the same data does not need to have separate copies for each object; instead, it is shared amongst all.

7. **Proxy**
As the name implies, the proxy pattern is a structural pattern that creates a proxy object. It acts as a placeholder for another object, controlling the access to it.

Usually, an object has an interface with several properties/methods that a client can access. However, an object might not be able to deal with the clients’ requests alone due to heavy load or constraints such as dependency on a remote source that might cause delays (e.g., network requests). In these situations, adding a proxy helps in dividing the load with the target object.

### Behavioral Patterns

1. **State**
The State pattern provides state-specific logic to a limited set of objects in which each object represents a particular state.

Say a customer places an online order for a TV. While this order is being processed it can in one of many states: New, Approved, Packed, Pending, Hold, Shipping, Completed, or Canceled. If all goes well the sequence will be New, Approved, Packed, Shipped, and Completed. However, at any point something unpredictable may happen, such as no inventory, breakage, or customer cancelation. If that happens the order needs to be handled appropriately.

Applying the State pattern to this scenario will provide you with 8 State objects, each with its own set of properties (state) and methods (i.e. the rules of acceptable state transitions). State machines are often implemented using the State pattern. These state machines simply have their State objects swapped out with another one when a state transition takes place.

**This reading has more content pending to be published**

---

## References

- https://en.wikipedia.org/wiki/Software_design_pattern
- https://medium.com/geekculture/dependency-injection-in-javascript-2d2e4ad9df49
- https://www.dottedsquirrel.com/bridge-pattern-javascript/