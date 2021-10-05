# Beginners guide to Node.js and NPM
We will be working in the Node.js and NPM environment throughout this bootcamp. The objectives of this lesson are:
1. Understanding the Node.js framework
2. Advantages of Node.js and why this course is focussed on Node.js

## Introduction to Node.js
Is it a programming language? Is it a library? No, it's Node.js. In simple words, Node.js is nothing but JavaScript running on the server-side, and it's awesome.

<img src="https://drive.google.com/uc?export=view&id=1oaHgcGKcrKbW6G-gFsncV95WhVmc40M7">

But to be specific, Node.js is an open-source, cross-platform, backend JavaScript runtime environment that runs on the V8 engine and executes JavaScript code outside a web browser.

And here is what a common Hello World code in Node.js would look like:

```js
const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
  res.statusCode = 200
  res.setHeader('Content-Type', 'text/plain')
  res.end('Hello World\n')
})

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`)
})
```

Using the http module, one of many useful Node.js libraries, an HTTP server is created. The server is set to listen on a specified hostname and port. When the server is ready, the callback function is called, in this case informing us that the server is running. Whenever a new request is received from a client, the request event is called, providing two objects: a request and a response. The first provides details of the request, although not used in this example, and the second is used to return data to the client.

You will learn more about the keywords mentioned in this code block throughout this module.

### Some brief history first
Node.js is only 12 years old, not a long time in tech. In comparison, JavaScript itself is more than 20 years old, and we know that it is what runs in our browsers. JavaScript was created at Netscape, which also tried to create LiveWire, an attempt at server-side JavaScript. Unfortunately, it wasn't very successful and server-side JavaScript did not grow in popularity until the introduction of Node.js in 2009.

One key factor that led to the rise of Node.js was the timing. Just a few years earlier, JavaScript had started to be considered as a more serious language, thanks to "Web 2.0" applications (such as Flickr, Gmail, etc.) that showed the world what a modern experience on the web could be like. JavaScript engines also became considerably better as many browsers competed to offer users the best performance. Development teams behind major browsers worked hard to offer better support for JavaScript and find ways to make JavaScript run faster. The engine that Node.js uses under the hood, V8 (also known as Chrome V8 for being the open-source JavaScript engine of The Chromium Project), improved significantly due to this competition.

When Ryan Dahl wrote Node.js, one of his motivations was the limited possibilities of the most popular web server in 2009, Apache HTTP Server, to handle a lot of concurrent connections and the most common way of creating code which either blocked the entire process or implied multiple execution stacks in the case of simultaneous connections. A Node.js app runs in a single process, without creating a new thread for every request. Node.js provides a set of asynchronous I/O primitives in its standard library that prevent JavaScript code from blocking and generally, libraries in Node.js are written using non-blocking paradigms, making blocking behavior the exception rather than the norm.

### Features of Node.js
Firstly, though `.js` is the standard filename extension for JavaScript code, the name "Node.js" doesn't refer to a particular file in this context and is merely the name of the product. It can also be written as "NodeJS" or simply "Node".

1. **Speed**: Having been built on Google Chrome's V8 JavaScript engine, Node.js is extremely fast for code execution.
2. **Rich libraries**: Node Package Manager (NPM) has more than 50,000 bundles or libraries, so whatever functionality is required for an application can be easily imported from NPM.
3. **Asynchronous programming**: All APIs of Node.js library are asynchronous (i.e., non-blocking), so a Node.js based server does not wait for the API to return data. The server calls the API, and in the event that no data is returned, the server moves to the next API. The Events module of Node.js helps the server get a response from the previous API call. This also helps with the speed of Node.js.
4. **Single-threaded**: Node.js makes use of a single-threaded model with event looping. As a result, it can provide service to a much larger number of concurrent connections than traditional servers like Apache HTTP Server.
5. **Highly scalable**: Node.js server responds in a non-blocking way, making it highly scalable in contrast with traditional servers, which create limited threads to handle requests.

Node.js is written with C, C++ and JavaScript and uses libuv underhood to handle asynchronous events. Libuv is an abstraction layer for network and file system functionality on the OS.

<img src="https://drive.google.com/uc?export=view&id=18ys74BkK9tzQ6u8avgVw9seweoXY6GnA" width="60%">

### NPM and Packages in Node.js
One of the major factors of Node's success is npm - its popular package manager, which allows JavaScript developers to share useful packages quickly and easily. NPM – or "Node Package Manager" – is the default package manager for JavaScript's runtime Node.js. NPM consists of two main parts:
- a CLI (command-line interface) tool for publishing and downloading packages, and
- an online repository that hosts JavaScript packages</br>

A package is nothing but a directory that contains a bunch of code modules. Some popular npm packages are [lodash](https://lodash.com/) and [moment](https://momentjs.com/). Node.js has a wide community that develop good packages for everybody to use.

When we have a remote package in our project, it is called as a dependency since our project depends on it. We need to keep track of our dependencies or at least list them down somewhere. We list all our dependencies inside a `package.json` file which is a JSON file that contains some information about our project and dependencies it needs. This file is essential for NPM.

Node.js also ships with a collection of [built-in packages](https://nodejs.org/api/index.html) called as Node Standard Library. These packages are essential to perform low-level operations like File System I/O and Networking. We do not have to install them using NPM.

### How much JavaScript should I know to use Node.js?
As a beginner, it can be difficult to understand where does JavaScript end, and where Node.js begins, and vice versa. However, when you're writing code for a Node.js application you are writing JavaScript. So, it is important to grasp the fundamentals of JavaScript syntax such as:
- Lexical Structure
- Expressions
- Types
- Classes
- Variables
- Functions
- `this`
- Arrow Functions
- Loops
- Scopes
- Arrays
- Objects
- Array and Object methods
- Template Literals
- Semicolons
- Strict Mode
- ECMAScript 6 or ES6

Also, as asynchronous programming is the core of Node.js it is important to understand concepts like:
- [Asynchronous programming and callbacks](https://nodejs.dev/learn/javascript-asynchronous-programming-and-callbacks)
- [Timers](https://nodejs.dev/learn/discover-javascript-timers)
- [Promises](https://nodejs.dev/learn/understanding-javascript-promises)
- [Async and Await](https://nodejs.dev/learn/modern-asynchronous-javascript-with-async-and-await)
- [Closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures)
- [The Event Loop](https://nodejs.dev/learn/the-nodejs-event-loop)

If you're interested to dive deeper into understanding Node.js, [here](https://nodejs.dev/learn/introduction-to-nodejs) is a learning path that you can follow.

## Why are we teaching Node.js in this bootcamp?
From the previous lesson or previous experience, you might already be familar with other server-side languages like Python, PHP, Ruby or Java. So why did we choose to teach Node.js?

1. **Popularity**: Node.js has been consistently growing in popularity since it's introduction. As per the [Stackoverflow developer survey of 2021](https://insights.stackoverflow.com/survey/2021), JavaScript is the most popular language for 9 years in a row and Node.js has moved up to be the 6th most popular technology. Many companies that we have got in touch with have expressed interest in hiring more Node.js developers.
2. **Modern tech stack choice**: With the web being focussed more towards real-time user interaction, and serving web apps over websites, Node.js with its features is becoming the go-to choice for many tech companies.
3. **JavaScript everywhere**: Even if you use another language on the backend, you will still be using JavaScript on the frontend. Following a "JavaScript everywhere" paradigm, that is both on the frontend and backend, Node.js has a lower learning curve. A JavaScript developer today is ready to become a fullstack developer.
4. **Community**: Node.js and NPM has a great community with a vast and rich collection of packages and resources to learn and debug issues.
5. **Language agnostic approach**: Even though the assignments and code alongs in this course will be using Node.js, we will shed enough light on the core concepts of backend so that students can take a language agnostic approach and move to a different tech stack if required with ease. We believe that you must be proficient in programming, and not just a particular programming language.

Now that you have enough context on Node.js, let's prepare our coding environments on our computers. Coming up next is your first assignment of this course which will walk you through setting up your Node.js environment.

---
## References
- https://medium.com/jspoint/introduction-to-node-js-a-beginners-guide-to-node-js-and-npm-eca9c408f9fe
- https://en.wikipedia.org/wiki/Node.js
- https://www.simplilearn.com/tutorials/nodejs-tutorial/what-is-nodejs
- https://www.freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners/
- https://nodejs.dev/learn/introduction-to-nodejs
- https://medium.com/jspoint/how-javascript-works-in-browser-and-node-ab7d0d09ac2f
- https://www.geeksforgeeks.org/top-8-reasons-to-learn-nodejs-in-2020/