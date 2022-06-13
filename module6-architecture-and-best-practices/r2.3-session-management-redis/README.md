# Session Management with Redis

Remember session-based authentication from module 4? Remember working with express-session library? Well sessions are back again in this module in the context of production ready applications. The objectives of this lesson are:
1. Understanding session management in production environments
2. Exploring a session management example with Node.js and Redis

## Why do we need session management?

We've read about this while learning about authentication, but just to refresh your memory - The classic Hypertext Transfer Protocol (HTTP) is a stateless tool. This means every request that is sent from a single client is interpreted by the Web server independently and is not related to any other request. There is no inbuilt mechanism for the server to remember a specific user from different multiple requests, which also makes it impossible for the server to know if each request originated from the same user.

Session tracking enables you to track a user's progress over multiple servlets or HTML pages, which, by nature, are stateless. A session is defined as a series of related browser requests that come from the same client during a certain time period. Session tracking ties together a series of browser requests — think of these requests as pages — that may have some meaning as a whole, such as a shopping cart application.

There are few types of session storing techniques:
- Memory (single-server, non-replicated persistent storage)
- File system persistence
- JDBC persistence
- Cookie-based session persistence
- In-memory replication

In this reading, we will talk about the first: Memory (single-server, non-replicated persistent storage)

## How are session stores handled in production environments?

We can use the [express-session](https://www.npmjs.com/package/express-session) middleware to manage sessions in Node.js. The session is stored in the Express server itself. The default server-side session storage, MemoryStore, is purposely not designed for a production environment. It will leak memory under most conditions, does not scale past a single process, and is meant for debugging and developing. To manage multiple sessions for multiple users we have to create a global map and put each session object to it. Global variables in Node.js are memory consuming and can prove to be terrible security holes in production level projects.

This can be solved by using an external Session Store. We have to store every session in the store so that each one will belong to only a single user. One popular session store is built using Redis. You can also take a look at other [compatible session stores](https://www.npmjs.com/package/express-session#compatible-session-stores).

Let's look at the setup code for express-session with Redis as external session store.
```js
const express = require('express');
const session = require('express-session');
const redis = require('redis');
const connectRedis = require('connect-redis');
var bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// enable this if you run behind a proxy (e.g. nginx)
app.set('trust proxy', 1);

//Configure redis client
const redisClient = redis.createClient({
    host: 'localhost',
    port: 6379
})
redisClient.on('error', function (err) {
    console.log('Could not establish a connection with redis. ' + err);
});
redisClient.on('connect', function (err) {
    console.log('Connected to redis successfully');
});

const RedisStore = connectRedis(session);

//Configure session middleware
app.use(session({
    store: new RedisStore({ client: redisClient }),
    secret: 'secret$%^134',
    resave: false,
    saveUninitialized: false,
    cookie: {
        secure: false, // if true only transmit cookie over https
        httpOnly: false, // if true prevent client side JS from reading the cookie 
        maxAge: 1000 * 60 * 10 // session max age in miliseconds
    }
}));
```

The main difference between our previous session based applications is that this time we have connected to Redis and passed it as a store to our session config options. To add support of Redis you have to use Redis client and connect-redis. Create express-session and pass it to connect-redis object as parameter to initialize. Then in session middleware, pass the Redis store information such as host, port and other required parameters.

After this, session data will be accessible on `req.session` on every authenticated request. You can save data on the session as you wish.
```js
const session = req.session;
const { username, email, id } = req.body
session.username = username;
session.email = email;
session.id = id;
```

And to terminate a session: `req.session.destroy()`

Here's what basically happens in the user interaction flow:
1. User logs in to the application by entering their username and the password.
2. After processing the login request, the server generates a unique random number, known as the session ID, which is also stored on the Redis store.
3. The session ID is sent back to the user in the cookie header of the response data. For Node.js, this cookie header is named connect.sid.
4. Next time user comes to the application, the cookie is passed back to the server in the header with the session ID.
5. Then server checks for the particular session ID in the Redis store. If the session exists in the store user will be redirected to the home page without going to the login page.
6. User can stay on the page until the session expires.

Sessions can be terminated in bulk just by clearing the session store.

## Conclusion

Using Redis to store sessions is not only beneficial in production environments but also helps to improve the performance of the system. If you're using session-based authentication in your applications, during the production deployment phase it would be recommended to setup a Redis connection and use Redis as a session store to override the default MemoryStore.

---

## References
- https://medium.com/swlh/session-management-in-nodejs-using-redis-as-session-store-64186112aa9
- https://codeforgeek.com/using-redis-to-handle-session-in-node-js/
- https://jankleinert.com/blog/2019/07/11/nodejs-session-management-using-express-sessions-and-redis-part-1.html