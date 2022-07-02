# Express.js Best Practices

In the previous lesson, we learned about best practices for Node.js. However, Node applications are almost always built using a framework such as Express.js and there are recommended best practices for this framework as well. So let's dive in. The objectives of this lesson are:

1. Solidifying our understanding of the Express.js framework
2. Understanding the essential best practices that improve the security, performance, and reliability of Express.js applications

## Have I understood Express.js correctly?

We've been writing Express.js applications for 5 modules and 20+ assignments now, so the answer should be Yes. No?

We have learned a lot about Express.js and how to build REST APIs and web applications using the framework, but there might still be some open questions, unclear concepts, or unknown facts for us. So here's the chance to solidify our understanding of the most popular Node framework. You may also revisit the lesson titled "Introduction to Express.js" from module 1 before continuing with this lesson.

### What is Express.js and why do we use it?

While Node.js is great at what it does, there are still a number of tasks that you can't execute without external dependencies. Issues will crop up in an isolated Node.js application if you want to integrate specific handling for different HTTP requests or separately handle requests from different URL paths, create dynamic responses by using a template or serve static files. At this step, you either write the entire cumbersome code for yourself or use a framework that does the job for you without reinventing the wheel!

As described on the [Express website home page](https://expressjs.com/), Express is a fast, unopinionated, minimalist web framework for Node.js. Almost every Node.js tutorial on the web involves installing and setting up Express.js as one of the first few steps. We use Express.js because it makes the process of creating a server simple with built-in methods and that's why it is widely used and is the de facto framework for Node.

### Fast, Unopinionated, and Minimalist

The Express framework delivers high performance and fast delivery. It acts as a layer of an additional and cool set of features built on top of Node.js. It follows the philosophy of 'Less is more.' The minimalistic nature is efficient yet beautiful because it doesn't come in the way of a developer's expression. It provides simple and flexible features like routing, handling HTTP requests and responses, middleware, templating, and debugging.

But other than being highly efficient, Express is unopinionated. It doesn't come with a pre-defined set of rules which you have to follow. There are minimal restrictions; developers have the freedom to augment their possibilities and write code using varied components together. The point is that this is an unopinionated framework that sets you free. No stereotypes, expectations, or judgments, at Express you express uninhibited! With Express you can structure your app any way you want; add middleware packages or connect to any type of databases like MySQL, MongoDB, or PostgreSQL; pick and use the view engine that you like the most such as pug, ejs, handlebars, mustache and many more.

More often than not, all other frameworks provide a robust set of features but are way too complicated for beginners. Even before the first line is coded, there is a plethora of functions and boilerplate code that burden the developer unnecessarily. When you have a specific need to fulfill you can pick another framework that best suits your needs. But did you know that [other popular frameworks](https://expressjs.com/en/resources/frameworks.html) are actually built with Express?

## How can I make sure to follow all best practices of Express.js?

You must be thinking that you've grown comfortable with writing Express applications but there must be more to learn. As we make our applications production ready to receive end-user traffic, what are the little things to take care of that help make our application from good to great?

### Best Practices for Performance and Reliability

Let's start with **things to do in your code**.

1. **Use gzip compression**
   Gzip compressing can greatly decrease the size of the response body and hence increase the speed of a web app. Use the compression middleware for gzip compression in your Express app. For example:

   ```js
   const compression = require("compression");
   const express = require("express");
   const app = express();
   app.use(compression());
   ```

   For a high-traffic website in production, the best way to put compression in place is to implement it at a reverse proxy level. In that case, you do not need to use compression middleware.

2. **Don't use synchronous functions**
   Synchronous functions and methods tie up the executing process until they return. A single call to a synchronous function might return in a few microseconds or milliseconds, however, on high-traffic websites, these calls add up and reduce the performance of the app. Avoid their use in production.

   Although Node and many modules provide synchronous and asynchronous versions of their functions, always use the asynchronous version in production. The only time when a synchronous function can be justified is upon initial startup.

   You can use the [--trace-sync-io](https://nodejs.org/api/cli.html#--trace-sync-io) command-line flag to print a warning and a stack trace whenever your application uses a synchronous API. Of course, you wouldn't want to use this in production, but rather to ensure that your code is ready for production.

3. **Do logging correctly**
   In general, there are two reasons for logging from your app: For debugging and for logging app activity (essentially, everything else). Using `console.log()` or `console.error()` to print log messages to the terminal is common practice in development. But these functions are synchronous when the destination is a terminal or a file, so they are not suitable for production unless you pipe the output to another program.

   If you're logging for purposes of debugging, then instead of using `console.log()`, use a special debugging module like `debug`. This module enables you to use the DEBUG environment variable to control what debug messages are sent to `console.error()`, if any. To keep your app purely asynchronous, you'd still want to pipe `console.error()` to another program. But then, you're not really going to debug in production, are you?

   If you're logging app activity (for example, tracking traffic or API calls), instead of using `console.log()`, use a logging library like [Winston](https://www.npmjs.com/package/winston) or [Bunyan](https://www.npmjs.com/package/bunyan).

4. **Handle exceptions properly**
   Node apps crash when they encounter an uncaught exception. Not handling exceptions and taking appropriate actions will make your Express app crash and go offline. We will talk about ways to ensure your app automatically restarts below, and fortunately, Express apps typically have a short startup time. Nevertheless, you want to avoid crashing in the first place and to do that, you need to handle exceptions properly. To ensure you handle all exceptions, use the following techniques: Use try-catch and Use promises.

   One thing you should not do is to listen for the `uncaughtException` event, emitted when an exception bubbles all the way back to the event loop. Adding an event listener for `uncaughtException` will change the default behavior of the process that is encountering an exception; the process will continue to run despite the exception. This might sound like a good way of preventing your app from crashing, but continuing to run the app after an uncaught exception is a dangerous practice and is not recommended, because the state of the process becomes unreliable and unpredictable. Additionally, using `uncaughtException` is officially recognized as [crude](https://nodejs.org/api/process.html#process_event_uncaughtexception). So listening for `uncaughtException` is just a bad idea. This is why it is recommended to use things like multiple processes and supervisors: crashing and restarting is often the most reliable way to recover from an error. It is also not recommended to use [domains](https://nodejs.org/api/domain.html) as it generally doesn't solve the problem and is a deprecated module.

And now let's talk a little DevOps, that is, **things to do in your environment/setup**.

1. **Set NODE_ENV to "production"**
   The NODE_ENV environment variable specifies the environment in which an application is running (usually, development or production). One of the simplest things you can do to improve performance is to set NODE_ENV to "production." This makes Express:

   - Cache view templates.
   - Cache CSS files generated from CSS extensions.
   - Generate less verbose error messages.

   [Tests](https://www.dynatrace.com/news/blog/the-drastic-effects-of-omitting-node-env-in-your-express-js-applications/) indicate that just doing this can improve app performance by a factor of three!

   If you need to write environment-specific code, you can check the value of NODE_ENV with `process.env.NODE_ENV`. Be aware that checking the value of any environment variable incurs a performance penalty, and so should be done sparingly. In development, you typically set environment variables in your interactive shell, for example by using export or your `.bash_profile` file. But in general, you shouldn't do that on a production server; instead, use your OS's init system (systemd or Upstart).

2. **Ensure your app automatically restarts**
   In production, you don't want your application to be offline, ever. This means you need to make sure it restarts both if the app crashes and if the server itself crashes. Although you hope that neither of those events occurs, realistically you must account for both eventualities by:

   - Using a process manager to restart the app (and Node) when it crashes.
   - Using the init system provided by your OS to restart the process manager when the OS crashes. It's also possible to use the init system without a process manager.

   Node applications crash if they encounter an uncaught exception. The foremost thing you need to do is to ensure your app is well-tested and handles all exceptions. But as a fail-safe, put a mechanism in place to ensure that if and when your app crashes, it will automatically restart.

3. **Use a process manager**
   In development, you started your app simply from the command line with `node server.js` or something similar. But doing this in production is a recipe for disaster. If the app crashes, it will be offline until you restart it. To ensure your app restarts if it crashes, use a process manager. A process manager is a "container" for applications that facilitates deployment, provides high availability, and enables you to manage the application at runtime.

   In addition to restarting your app when it crashes, a process manager can enable you to:

   - Gain insights into runtime performance and resource consumption.
   - Modify settings dynamically to improve performance.
   - Control clustering.

   The most popular process managers for Node are as follows:

   - [StrongLoop Process Manager](https://strong-pm.io/)
   - [PM2](https://pm2.keymetrics.io/)
   - [Forever](https://www.npmjs.com/package/forever)

4. **Run your app in a cluster**
   In a multi-core system, you can increase the performance of a Node app by many times by launching a cluster of processes. A cluster runs multiple instances of the app, ideally one instance on each CPU core, thereby distributing the load and tasks among the instances. Apart from performance advantages, failure isolation is another reason to run a cluster of app processes. In clustered apps, worker processes can crash individually without affecting the rest of the processes.

   IMPORTANT: Since the app instances run as separate processes, they do not share the same memory space. That is, objects are local to each instance of the app. Therefore, you cannot maintain the state in the application code. However, you can use an in-memory datastore like Redis to store session-related data and state. This caveat applies to essentially all forms of horizontal scaling, whether clustering with multiple processes or multiple physical servers.

   Clustering can be set up using the NodeJS cluster module or one of the process managers mentioned above.

5. **Cache request results**
   Another strategy to improve the performance in production is to cache the result of requests so that your app does not repeat the operation to serve the same request repeatedly. Use a caching server like [Varnish](https://varnish-cache.org/) or [Nginx](https://www.nginx.com/resources/wiki/start/topics/examples/reverseproxycachingexample/) to greatly improve the speed and performance of your app.

6. **Use a load balancer**
   No matter how optimized an app is, a single instance can handle only a limited amount of load and traffic. One way to scale an app is to run multiple instances of it and distribute the traffic via a load balancer. Setting up a load balancer can improve your app's performance and speed, and enable it to scale more than is possible with a single instance.

   A load balancer is usually a reverse proxy that orchestrates traffic to and from multiple application instances and servers. You can easily set up a load balancer for your app by using [Nginx](http://nginx.org/en/docs/http/load_balancing.html) or [HAProxy](https://www.digitalocean.com/community/tutorials/an-introduction-to-haproxy-and-load-balancing-concepts).

   With load balancing, you might have to ensure that requests that are associated with a particular session ID connect to the process that originated them. This is known as session affinity, or sticky sessions, and may be addressed by the suggestion above to use a data store such as Redis for session data depending on your application.

7. **Use a reverse proxy**
   A reverse proxy sits in front of a web app and performs supporting operations on the requests, apart from directing requests to the app. It can handle error pages, compression, caching, serving files, and load balancing among other things.

   Handing over tasks that do not require knowledge of the application state to a reverse proxy frees up Express to perform specialized application tasks. For this reason, it is recommended to run Express behind a reverse proxy like [Nginx](https://www.nginx.com/) or [HAProxy](http://www.haproxy.org/) in production.

### Best Practices for security

1. **Don't use deprecated or vulnerable versions of Express**
   Express 2.x and 3.x are no longer maintained. Security and performance issues in these versions won't be fixed. Do not use them! Also, ensure you are not using any of the vulnerable Express versions listed on the [Security updates page](https://expressjs.com/en/advanced/security-updates.html). If you are, update to one of the stable releases, preferably the latest.

2. **Use TLS**
   If your app deals with or transmits sensitive data, use Transport Layer Security (TLS) to secure the connection and the data. This technology encrypts data before it is sent from the client to the server, thus preventing some common and easy hacks. Although Ajax and POST requests might not be visibly obvious and seem "hidden" in browsers, their network traffic is vulnerable to [packet sniffing](https://en.wikipedia.org/wiki/Packet_analyzer) and [man-in-the-middle attacks](https://en.wikipedia.org/wiki/Man-in-the-middle_attack).

   You may be familiar with Secure Socket Layer (SSL) encryption. TLS is simply the next progression of SSL. In other words, if you were using SSL before, consider upgrading to TLS. In general, we recommend Nginx to handle TLS. Also, a handy tool to get a free TLS certificate is [Let's Encrypt](https://letsencrypt.org/about/), a free, automated, and open certificate authority (CA) provided by the Internet Security Research Group (ISRG).

3. **Use Helmet**
   [Helmet](https://helmetjs.github.io/) can help protect your app from some well-known web vulnerabilities by setting HTTP headers appropriately. It is a collection of several smaller middleware functions that set security-related HTTP response headers. Some examples include:

   - `helmet.contentSecurityPolicy` which sets the Content-Security-Policy header. This helps prevent cross-site scripting attacks among many other things.
   - `helmet.hsts` which sets the Strict-Transport-Security header. This helps enforce secure (HTTPS) connections to the server.
   - `helmet.frameguard` which sets the X-Frame-Options header. This provides clickjacking protection.

   If you don't want to use Helmet, then at least disable the X-Powered-By header. Attackers can use this header (which is enabled by default) to detect apps running Express and then launch specifically-targeted attacks. So, the best practice is to turn off the header with the `app.disable()` method:

   ```js
   app.disable("x-powered-by");
   ```

4. **Use cookies securely**
   To ensure cookies don't open your app to exploits, don't use the default session cookie name and set cookie security options appropriately. There are two main middleware cookie session modules:

   - [express-session](https://www.npmjs.com/package/express-session) that replaces `express.session` middleware built-in to Express 3.x.
   - [cookie-session](https://www.npmjs.com/package/cookie-session) that replaces `express.cookieSession` middleware built-in to Express 3.x.

   The main difference between these two modules is how they save cookie session data. The express-session middleware stores session data on the server; it only saves the session ID in the cookie itself, not session data. By default, it uses in-memory storage and is not designed for a production environment. In production, you'll need to set up a scalable session store; see the [list of compatible session stores](https://github.com/expressjs/session#compatible-session-stores).

   In contrast, cookie-session middleware implements cookie-backed storage: it serializes the entire session to the cookie, rather than just a session key. Only use it when session data is relatively small and easily encoded as primitive values (rather than objects). Although browsers are supposed to support at least 4096 bytes per cookie, to ensure you don't exceed the limit, don't exceed a size of 4093 bytes per domain. Also, be aware that the cookie data will be visible to the client, so if there is any reason to keep it secure or obscure, then express-session may be a better choice.

   **Don't use the default session cookie name** : Using the default session cookie name can open your app to attacks. The security issue posed is similar to X-Powered-By: a potential attacker can use it to fingerprint the server and target attacks accordingly.

   **Set cookie security options** :

   - `secure`: Ensures the browser only sends the cookie over HTTPS.
   - `httpOnly`: Ensures the cookie is sent only over HTTP(S), not client JavaScript, helping to protect against cross-site scripting attacks.
   - `domain`: indicates the domain of the cookie; use it to compare against the domain of the server in which the URL is being requested. If they match, then check the path attribute next.
   - `path`: indicates the path of the cookie; use it to compare against the request path. If this and the domain match, then send the cookie in the request.
   - `expires`: use to set an expiration date for persistent cookies.

5. **Prevent brute-force attacks against authorization**
   Make sure login endpoints are protected to make private data more secure. A simple and powerful technique is to block authorization attempts using two metrics:

   - The first is the number of consecutive failed attempts by the same user name and IP address.
   - The second is the number of failed attempts from an IP address over some long period of time. For example, block an IP address if it makes 100 failed attempts in one day.

   [rate-limiter-flexible](https://github.com/animir/node-rate-limiter-flexible) package provides tools to make this technique easy and fast.

6. **Ensure your dependencies are secure**
   Using npm to manage your application's dependencies is powerful and convenient. But the packages that you use may contain critical security vulnerabilities that could also affect your application. The security of your app is only as strong as the "weakest link" in your dependencies. Since npm@6, npm automatically reviews every install request. Also, you can use `npm audit` to analyze your dependency tree.

7. **Avoid other known vulnerabilities**
   Keep an eye out for [Node Security Project](https://github.com/advisories) or [Snyk](https://security.snyk.io/) advisories that may affect Express or other modules that your app uses. In general, these databases are excellent resources for knowledge and tools about Node security. Finally, Express apps - like any other web apps - can be vulnerable to a variety of web-based attacks. Familiarize yourself with known web vulnerabilities and take precautions to avoid them.

**Additional considerations**

Here are some further recommendations from the excellent [Node.js Security Checklist](https://blog.risingstack.com/node-js-security-checklist/). Refer to that blog post for all the details on these recommendations:

- Use `csurf` middleware to protect against cross-site request forgery (CSRF).
- Always filter and sanitize user input to protect against cross-site scripting (XSS) and command injection attacks.
- Defend against SQL injection attacks by using parameterized queries or prepared statements.
- Use the open-source _sqlmap tool_ to detect SQL injection vulnerabilities in your app.
- Use the `nmap` and `sslyze` tools to test the configuration of your SSL ciphers, keys, and renegotiation as well as the validity of your certificate.
- Use `safe-regex` to ensure your regular expressions are not susceptible to regular expression denial of service attacks.

Here are some further readings on best practices for performance, reliability, and security:

1. https://expressjs.com/en/advanced/healthcheck-graceful-shutdown.html
2. https://expressjs.com/en/advanced/pm.html
3. https://expressjs.com/en/resources/glossary.html
4. https://blog.logrocket.com/node-js-best-practices-and-performance-analytics-in-2021/

---

## References

- https://www.konfinity.com/what-is-express-in-nodejs
- https://tamalweb.com/why-expressjs-in-nodejs#express-js-is-minimal-and-unopinionated
- https://expressjs.com/en/advanced/best-practice-performance.html
- https://expressjs.com/en/advanced/best-practice-security.html
