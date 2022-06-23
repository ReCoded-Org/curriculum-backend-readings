# TypeScript with Node and Express

We took some time to understand the TypeScript syntax and how it makes our code better, so let us come back to the backend and how TypeScript can be used in backend code. We have been learning to build backend servers using Node.js and Express.js where we've used JavaScript syntax thus far. So how can we use TypeScript code in an Express server and how do we ensure it is getting compiled correctly? That is what we will learn now. The objectives of this lesson are:

1. Setting up TypeScript with Node and Express
2. Viewing practical usage of TypeScript in backend codebases
3. Understanding extended types in Express

## Setting up

We'll be walking through a workflow for setting up TypeScript with Node and Express. Firstly, make sure TypeScript is installed globally on your machine.

```bash
npm i -g typescript
```

Then we create a new project folder and initialize the `package.json` file just like we do for our regular Node Express projects.

```bash
mkdir node-express-typescript
cd node-express-typescript/
npm init --yes
```

We will also set up the `tsconfig.json` file.

```
tsc --init
```

On this file the main configurations required are:

```json
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "./dist",
    "srcDir": "./src",
    "strict": true,
    "moduleResolution": "node"
  }
}
```

Now we'll create our source folder with an `app.ts` file.

```bash
mkdir src
cd src
touch app.ts
```

Next, we install Express and a few dev dependencies for TypeScript.

```bash
npm i express
npm i -D nodemon typescript ts-node @types/node @types/express
```

We will add a few scripts to our `package.json` file.

```json
{
  "scripts": {
    "start": "node dist/app.js",
    "dev": "nodemon src/app.ts",
    "build": "tsc -p ."
  }
}
```

And now we are ready to build an Express application with TypeScript and incorporate custom types for Node and Express.

## Building Express application with TypeScript

Let's start out by building a simple Express server, which has been the first step in all our projects so far. We add these lines to the `app.ts` file.

```js
import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("Express TypeScript Server");
});

app.listen(5000, () => console.log("Server running"));
```

Now if we run `npm run dev` we should see our Express server running in watch mode.

Now let's add in some meaningful types in our Express server code. We'll use the custom Express types - Application, Request, Response, and NextFunction.

```typescript
import express, { Application, Request, Response, NextFunction } from "express";

const app: Application = express();

app.get("/", (req: Request, res: Response, next: NextFunction) => {
  res.send("Express TypeScript Server");
});

app.listen(5000, () => console.log("Server running"));
```

And then we can also have any functions with types that can be called in the handler functions for our endpoints.

```typescript
const add = (x: number, y: number): number => x + y;
```

You can use Interfaces, Object types, Classes, or any other Types from TypeScript.

You can anytime look at the compiled JS files in the dist folder and see what your TypeScript code gets compiled to.

And when you're ready to deploy the JS code to the server, you can run `npm start` on the server.

## Conclusion

TypeScript can make work on your backend code a little bit easier by helping you easily spot type errors and avoid running into unexpected code execution at runtime. If you're working with a team, it also makes the codebase very readable and enforces guidelines for defining types on all variables and functions. We hope you'll try to use TypeScript in some of your Express projects and share your experience of working with static typing. We are now approaching the end of this module, so in the next lesson, we'll be looking a bit beyond Express.js at other frameworks which already incorporate TypeScript.

---

## References

- https://blog.logrocket.com/how-to-set-up-node-typescript-express/
- https://www.valentinog.com/blog/typescript/#dipping-our-toes-into-typescript-types
- https://dev.to/macmacky/get-better-with-typescript-using-express-3ik6
- https://www.youtube.com/watch?v=zRo2tvQpus8&t=623s&ab_channel=TraversyMedia
