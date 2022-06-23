# Backend frameworks with TypeScript

We have been working with the Express framework and have understood the use of TypeScript syntax in it. However, there are open-source frameworks that are built directly using TypeScript even though Express is still one of the most popular frameworks and is actually even the foundation of newly built frameworks. The objectives of this lesson are:

1. Looking at other frameworks that use TypeScript inherently
2. Understanding Nest.js and TypeORM frameworks

## Backend frameworks using TypeScript

In a previous lesson, we had mentioned [frameworks built on top of Express.js](https://expressjs.com/en/resources/frameworks.html). Some of these frameworks are powered exclusively by TypeScript.

1. [FoalTS](https://foalts.org/): Considered to be the elegant NodeJS framework, it provides a set of ready-to-use components so you don't have to reinvent the wheel every time. In one single place, you have a complete environment to build web applications. This includes a CLI, testing tools, frontend utilities, scripts, advanced authentication, ORM, deployment environments, GraphQL and Swagger API, AWS utilities, and more. The framework is entirely written in TypeScript. The language brings you optional static type-checking along with the latest ECMAScript features. This allows you to detect the silliest errors during compilation and improve the quality of your code. It also offers you autocompletion and a well-documented API.

2. [NestJS](https://nestjs.com/): Described as a progressive Node.js framework, uses modern JavaScript, is built with TypeScript (preserves compatibility with pure JavaScript), and combines elements of OOP (Object Oriented Programming), FP (Functional Programming), and FRP (Functional Reactive Programming) all of which helps for building efficient, scalable Node.js server-side applications. Nest aims to provide an application architecture out of the box which allows for the effortless creation of highly testable, scalable, loosely coupled, and easily maintainable applications. The architecture is heavily inspired by AngularJS.

3. [Expressive Tea](https://expressive-tea.io/): For building module-oriented, clean, fast, and descriptive server-side applications with TypeScript and Express out of the box. It is a flexible framework but also gives freedom to the developer to build their own architectures by providing descriptive decorators, a plugin engine, shareable modules, and modern Javascript.

4. [Prisma](https://www.prisma.io/): Described as a next-generation Node.js and TypeScript ORM, it helps app developers build faster and make fewer errors with an open source database toolkit for PostgreSQL, MySQL, SQL Server, SQLite, MongoDB, and CockroachDB.

5. [TypeORM](https://typeorm.io/): Can run in NodeJS, Browser, Cordova, PhoneGap, Ionic, React Native, NativeScript, Expo, and Electron platforms and can be used with TypeScript and JavaScript (ES5, ES6, ES7, ES8). Its goal is to always support the latest JavaScript features and provide additional features that help you to develop any kind of application that uses databases - from small applications with a few tables to large-scale enterprise applications with multiple databases.

6. [RxJS](https://rxjs.dev/): A Reactive Extensions Library for JavaScript, useful for reactive programming using Observables, to make it easier to compose asynchronous or callback-based code.

7. [AdonisJS](https://adonisjs.com/): A fully featured web framework for Node.js, it includes everything you need to create a fully functional web app or an API server and does not require wasting hours downloading and assembling hundreds of packages.

## NestJS

[Here](https://www.youtube.com/watch?v=0M8AYU_hPas&ab_channel=TraversyMedia) is a 100-second video on NestJS by Fireship for a quick overview.

NestJS is a Node.js framework that's intended for use with TypeScript to build efficient and scalable server-side applications. This is a web application that mainly relies on strong HTTP server frameworks like Express or Fastify. Nest is a new Node.js framework that not only imitates but also corrects the flaws of previous Node.js frameworks.

### Few of the great features of NestJS

1. Nest.js was created to help developers create Monoliths and Microservices.
2. It's simple to use, quick to learn, and easy to apply.
3. It leverages TypeScript.
4. Powerful Command Line Interface (CLI) to boost productivity and ease of development.
5. Support for dozens of nest-specific modules that help you easily integrate with common technologies and concepts like TypeORM, Mongoose, GraphQL, Logging, Validation, Caching, WebSockets, and much more.
6. Easy unit-testing applications.
7. Great documentation.
8. Built for large-scale enterprise applications.

### Core Components of NestJS

1. **Controllers** are responsible for handling incoming requests and responding to the application's client-side.
2. **Modules** are used to structure code and separate functionality into logical, reusable chunks.
3. **Providers or services** which abstract complexity and logic away from the user. It's possible to inject the service into controllers or other services.

[Here](https://www.freecodecamp.org/news/build-web-apis-with-nestjs-beginners-guide/) is a freeCodeCamp tutorial on how to build APIs with NestJS, Postgres, and Sequelize.

## TypeORM

[Here](https://javascript.plainenglish.io/creating-a-rest-api-with-jwt-authentication-and-role-based-authorization-using-typescript-fbfa3cab22a4#:~:text=Why%20TypeORM%3F,model%20class%20to%20make%20validations.) is an article mentioning a strong reason why you should learn and use TypeORM.

TypeORM leverages TypeScript to write database integration code and is compatible with MySQL / MariaDB / Postgres / SQLite / Microsoft SQL Server / Oracle / sql.js / MongoDB. You can switch between those databases without having to rewrite your code.

### Few of the great features of TypeORM

1. Supports DataMapper and ActiveRecord patterns
2. Entities and columns and Entity manager
3. Database-specific column types
4. Repositories and custom repositories.
5. Clean object-relational model and Associations (relations)
6. Eager and lazy relations. Uni-directional, bi-directional and self-referenced relations.
7. Supports multiple inheritance patterns.
8. Cascades, Indices, and Transactions.
9. Migrations and automatic migrations generation.
10. Connection pooling and Replication.
11. Using multiple database instances.
12. Working with multiple database types and Cross-database and cross-schema queries.
13. Elegant syntax, flexible and powerful QueryBuilder.
14. Left and inner joins.
15. Proper pagination for queries using joins.
16. Query caching.
17. Streaming raw results and Logging.
18. Listeners and subscribers (hooks).
19. Supports closure table pattern.
20. Schema declaration in models or separate configuration files.
21. Connection configuration in json / xml / yml / env formats.
22. Produced code is performant, flexible, clean, and maintainable.
23. Follows all possible best practices.

With TypeORM your models look like this:

```typescript
import { Entity, PrimaryGeneratedColumn, Column } from "typeorm";

@Entity()
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  firstName: string;

  @Column()
  lastName: string;

  @Column()
  age: number;
}
```

[Here](https://orkhan.gitbook.io/typeorm/docs/example-with-express) is a tutorial on using TypeORM with Express.

## Conclusion

When it comes to Node.js with TypeScript, there is much more beyond Express. While Express is still very popular and widely used in the industry, it is great to be flexible and adapt to working with a new framework if you're asked to in your career as a developer. It is also interesting to study how these frameworks were built and what is the problem they are trying to solve. Although sometimes it can feel like there is a JS framework for literally everything under the sun, take it one step at a time and identify just one or two frameworks to invest your time in learning. We recommend NestJS after you've mastered ExpressJS.

---

## References

- https://nodejs.dev/learn/nodejs-with-typescript
- https://enlear.academy/why-you-should-use-nestjs-as-your-backend-framework-bd1ff1acce5d
