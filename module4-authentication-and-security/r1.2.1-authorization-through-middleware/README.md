# Authorization through middleware

In the previous lesson, we introduced authorization and implemented authentication and authorization guards using if-else statements directly inside the route controllers. This isn't an acceptable approach as the code will be very messy and bug-prone. It is better to define authorization logic outside the controllers, and use middlewares to enforce it.

This lesson objectives are:

- Introduce middleware as a feature in Express.js and many other backend frameworks
- Implement authentication guard
- Implement authorization guard
- Guard certain endpoints with these middlewares

## **Middleware**

Middleware are functions that have access to the [request object](https://expressjs.com/en/4x/api.html#req) (`req`), the [response object](https://expressjs.com/en/4x/api.html#res) (`res`), and the next middleware function in the application’s request-response cycle. The next middleware function is commonly denoted by a variable named `next`.

```js
const loggerMiddleware = (req, res, next) => {
  // you have full access to the request and response objects
  console.log("Request Type:", req.method);
  // end the middleware by calling next()
  next();
};
```

Middleware functions can perform the following tasks:

- Execute any code.
- Make changes to the request and the response objects.
- End the request-response cycle.
- Call the next middleware function in the stack.

If the current middleware function does not end the request-response cycle, it must call `next()` to pass control to the next middleware function. Otherwise, the request will be left hanging.

All the functions we used inside the controllers, or that we passed to the router endpoint, are middleware functions. They were used as the last middleware because we haven't called the `next()` function and ended the cycle by calling `res.render()` or `res.json()`.

An Express application can use the following types of middleware:

- [Application-level middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.application)
- [Router-level middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.router)
- [Error-handling middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.error-handling)
- [Built-in middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.built-in)
- [Third-party middleware](https://expressjs.com/en/guide/using-middleware.html#middleware.third-party)

You can load application-level and router-level middleware with an optional mount path. You can also load a series of middleware functions together, which creates a sub-stack of the middleware system at a mount point. Check out Express documentation regarding [using middleware](https://expressjs.com/en/guide/using-middleware.html).

We've seen middleware in previous lessons when we used the `express-session` and `express-jwt`. They are application-level middleware that we used to create the session object or the user object inside `req` that we subsequently used in the controller. By default, `req` wouldn't contain `session` or `user` however, in the case of `express-session` the following simplified steps were done for _every_ request:

- Read the cookies from `req` and grab the `sessionID`.
- If no `sessionID` is found in the request's cookies:
  - Create a new session and grab its ID.
  - Queue a `Set-Cookie` header with `sessionID` to the next response by modifying `res`.
- Else read the session associated with requests `sessionID` from the session adapter.
- Append the created or read `session` to `req`.
- Call `next()` to let the app continue its req-res cycle.

### **Middleware precedence**

In Express.js middleware are applied in their order of use. Remember that every function that has `req` and `res` is a middleware function. And the middleware stack is established when you use `app.use` or `router.use`.

```js
app.use(session());
app.use(logger());
```

In the code above, the `express-session` middleware will be executed first, then when it calls `next()`, the `logger` middleware will be executed till it calls `next()` as well, and so on.

So it is important whenever you define your middleware that you make sure the required middleware for it are executed before it.

For example, in your `onlyAuthenticated` middleware, you will need to check `req.session.user` (or `req.user` if you use `express-jwt`). Hence, it is important that the session middleware is applied before your middleware. Otherwise, you won't have `session` inside `req`.

### **Middleware mount-path**

Middleware can be scoped as well. It can be for every request, or for specific endpoints, or even specific HTTP methods:

```js
app.use(function (req, res, next) {
  // will be called on every request. Application wide mount path
  next();
});

app.use("/dashboard", function (req, res, next) {
  // will be called on all request to /dashboard
  next();
});

app.get("/user", function (req, res, next) {
  // will be invoked only when a GET requesting /user endpoint
  next();
});
```

You can even enforce the middleware on only specific router instances and controllers:

```js
// ./routes/user.js
const express = require("express");
const router = express.Router();

router.use(function (req, res, next) {
  // will be called on all routes in this file ONLY
  next();
});
```

### **Error-handling middlware**

All the middleware we've seen so far take only **three** arguments, `req`, `res`, and `next`. You can define an error-handling middleware by providing **four** arguments: `err`, `req`, `res`, and `next`. These middleware are important to handle errors that are thrown in your app and provide a safe fallback response to clients without exposing your app's security.

```js
app.use(function (err, req, res, next) {
  console.error(err.stack);
  res.status(500).send("Something broke!");
});
```

Usually, an error logging service like [sentry](https://sentry.io/) is also contacted in this middleware to log and track the error so you get notified when your app has run into an unhandled exception, with the required request-response details that can help the developers reproduce the error to fix it.

> ⚠️ **Warning**: Error-handling middleware always takes **four** arguments. You must provide four arguments to identify it as an error-handling middleware function. Even if you don’t need to use the next object, you must specify it to maintain the signature. Otherwise, the next object will be interpreted as regular middleware and will fail to handle errors.

## **Auth guard middleware**

To implement `onlyAdmins`, `onlyModerators`, and `onlyAuthenticated` middleware, we create a new middleware containing source file:

```js
// ./middlware/index.js

function onlyAuthenticated(req, res, next) {
  if (req.session.user) {
    next(); // user is authenticated
  } else {
    res.status(401).redirect("/login");
  }
}

function onlyAdmins(req, res, next) {
  const user = req.session.user;

  if (user && user.isAdmin) {
    next();
  } else {
    res.status(401).json({ error: "Unauthorized" });
  }
}

function onlyModerators(req, res, next) {
  const user = req.session.user;
  if (user && (user.isAdmin || user.isModerator)) {
    next();
  } else {
    res.status(401).json({ error: "Unauthorized" });
  }
}

module.exports = { onlyAuthenticated, onlyAdmins, onlyModerators };
```

then inside our router, we can guard it by applying the middleware **before** the endpoint handler function:

```js
// ./routes/role.js
const express = require("express");
const router = express.Router();
const { User } = require("../db"); // as exported in the db file
const { onlyAdmins } = require('../middleware');

router.post("/elevate", onlyAdmins, async (req, res) => {
  const { subject_id, role_id } = req.body;

  // check role_id is correct
  const roles = Object.values(User.roles);
  if (!roles.includes(parseInt(role_id, 10))) {
    res.status(400).json({
      error: `role_id is incorrect. Accepted values are: ${roles.join(", ")}`,
    });
    return; // exit
  }

  // check subject to be elevated exists
  // we will query users with defaultScope to exclude password
  const subject = await User.findByPk(subject_id);

  if (!subject) {
    res.status(400).json({
      error: `User with id: ${subject_id} cannot be found.`,
    });
  } else {
    subject.role_id = parseInt(role_id, 10);
    await subject.save(); // save dirty instance to database
    res.status(202).json({ status: "OK" });
  }
}
```

Because we are using the `onlyAdmins` middleware, there is no need to check if the user is logged in or is an admin. The code above won't be executed if the user isn't authorized.

> ⚠️ **Warning**: When you apply a middleware, you simply pass it as a **function**. Above we passed `onlyAdmins` without `()` parentheses. Middleware can be implemented using a configuration function as well, which is a function that takes configuration arguments and returns a middleware function. Read more about it in Express [documentation](https://expressjs.com/en/guide/writing-middleware.html#:~:text=Using%20Express%20middleware.-,Configurable%20middleware,-If%20you%20need).

## **Conclusion**

In this lesson, we learned that everything in Express.js is basically a middleware that gets invoked somewhere. And by using middleware, we can structure our business logic in a clean approach. Middleware can be used for basically everything, and one of their use cases is to enforce authorization.
