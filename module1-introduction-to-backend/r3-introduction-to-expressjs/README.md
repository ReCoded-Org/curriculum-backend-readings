# Introduction to Express.js
Express is the most popular Node web framework, and is the underlying library for a number of other popular Node web frameworks. The objectives of this lesson are:
1. Getting familiar with Express.js
2. Getting ready to build a backend application using Node and Express

## Why Express?

Express was created in 2010, just a year after Node was introduced. It provides mechanisms to:
- Write handlers for requests with different HTTP verbs at different URL paths (routes).
- Integrate with "view" rendering engines in order to generate responses by inserting data into templates.
- Set common web application settings like the port to use for connecting, and the location of templates that are used for rendering the response.
- Add additional request processing "middleware" at any point within the request handling pipeline.

While Express itself is fairly minimalist, developers have created compatible middleware packages to address almost any web development problem. There are libraries to work with cookies, sessions, user logins, URL parameters, POST data, security headers, and many more. You can find a list of middleware packages maintained by the Express team at [Express Middleware](https://expressjs.com/en/resources/middleware.html). You can also check out some of the other [popular Node web frameworks](https://expressjs.com/en/resources/frameworks.html) built using Express.

## Hello World in Express

This probably looks quite similar to the Hello World example of plain Node.js.

```
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}!`)
});
```

The first two lines `require()` (import) the express module and create an Express application. This object, which is traditionally named app, has methods for routing HTTP requests, configuring middleware, rendering HTML views, registering a template engine, and modifying application settings that control how the application behaves (e.g. the environment mode, whether route definitions are case sensitive, etc.)

The middle part of the code (the three lines starting with `app.get`) shows a route definition. The `app.get()` method specifies a callback function that will be invoked whenever there is an HTTP GET request with a path ('/') relative to the site root. The callback function takes a request and a response object as arguments, and calls `send()` on the response to return the string "Hello World!"

The final block starts up the server on a specified port ('3000') and prints a log comment to the console. With the server running, you could go to localhost:3000 in your browser to see the example response returned.

Now that we have learned all about HTTP requests and responses and RESTful APIs, let's start building our own REST API server using Node.js and Express.js in the next two assignments.

## Express with Node

Although it is very much possible to write a vanilla Node.js server, as shown in [this MDN article](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Node_server_without_framework), it is rarely done so. You will always find the use of a framework like Express with Node to build server-side applications. This is because Node.js uses the HTTP module for network I/O, but you would still have to write a lot of boilerplate code to handle things like routes, cookies, sessions, etc. Express abstracts these away by providing simple functions for routing and middleware for cookies and sessions while still allowing the flexibility to customize the application architecture as desired by the developer.

---
## References
- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/Introduction