# Logging

Logging helps developers know what it is that their code is actually doing, and can help developers save hours of debugging work. And there's much more to logging than the classic console.log(). The objectives of this lesson are:

1. Understanding best practices and methods of logging
2. Getting familiar with tools for logging

## Start with console.log

We use console.log all the time to debug and test our code. But what is lesser known is that there are [more console methods](https://developer.mozilla.org/en-US/docs/Web/API/console) for different logging levels:

```js
console.error("This is an error log!");
console.info("This is an information log.");
console.warn("This is a warning log.");
console.debug("This is a debug level log.");
```

However, console.log can sometimes cause a negligible decrease in performance. To avoid negatively impacting performance, it is recommended to switch to a logging library for production-level projects.

## Move to a logging library

Logging libraries help developers create and manage log events, which can increase the overall efficiency and functionality of your application. Some of the most popular logging libraries for Node are [Winston](https://www.npmjs.com/package/winston), [Pino](https://www.npmjs.com/package/pino), [Bunyan](https://www.npmjs.com/package/bunyan), and [Log4js](https://www.npmjs.com/package/log4js).

While you should almost always use a standard `console.log`, a logging library can be more functional and help avoid decreases in app performance.

### Winston

Logs displayed in the console are lost if the console or application is restarted. So, if you want to store your error log in a remote location or separate database, Winston might be the best choice because it supports multiple modes of transport. Below is an example of how to set up a logging library using Winston:

```js
const winston = require("winston");
const config = require("./config");

const enumerateErrorFormat = winston.format((info) => {
  if (info instanceof Error) {
    Object.assign(info, { message: info.stack });
  }
  return info;
});

const logger = winston.createLogger({
  level: config.env === "development" ? "debug" : "info",
  format: winston.format.combine(
    enumerateErrorFormat(),
    config.env === "development"
      ? winston.format.colorize()
      : winston.format.uncolorize(),
    winston.format.splat(),
    winston.format.printf(({ level, message }) => `${level}: ${message}`)
  ),
  transports: [
    new winston.transports.Console({
      stderrLevels: ["error"],
    }),
  ],
});

module.exports = logger;
```

### Pino

This logging library is very popular for its low overhead and minimalism. It uses fewer resources for logging by using a worker thread for processing.

```js
const pino = require("pino");

// Create a logging instance
const logger = pino({
  level: process.env.NODE_ENV === "production" ? "info" : "debug",
});

logger.info("Application started!");
```

### Bunyan

Bunyan is another fast JSON logging library that supports multiple modes of transport and uses a CLI for filtering the logs. It has a refined method that produces what they should do. It even has a feature called log snooping, which helps in debugging failures in production. Other cool features of Bunyan are a stream system for controlling where logs are located, support for environments aside from Node.js, and that JSON objects are serialized by default.

```js
const bunyan = require('bunyan');
const log = bunyan.createLogger({name: 'myapp'});
log.info('My App');


{"name":"myapp","hostname":"banana.local","pid":40161,"level":30,"msg":"My App","time":"2022-04-04T18:24:23.851Z","v":0}
```

### Log HTTP requests in Node with Morgan

Another best practice is to log your HTTP requests in your Node.js application. One of the most used tools to accomplish this is Morgan, which gets the server logs and systematizes them to make them more readable.

To use Morgan, simply set the format string:

```js
const morgan = require("morgan");
app.use(morgan("dev"));
```

For reference, the predefined format string is:

```js
morgan("tiny");
```

The output is basically a log of each HTTP request received by the server including data points like the request method, path, and response code.

### Configure Winston with Morgan

If you choose to use the Winston library, then you can easily configure it with Morgan:

```js
const morgan = require("morgan");
const config = require("./config");
const logger = require("./logger");

morgan.token("message", (req, res) => res.locals.errorMessage || "");

const getIpFormat = () =>
  config.env === "production" ? ":remote-addr - " : "";
const successResponseFormat = `${getIpFormat()}:method :url :status - :response-time ms`;
const errorResponseFormat = `${getIpFormat()}:method :url :status - :response-time ms - message: :message`;

const successHandler = morgan(successResponseFormat, {
  skip: (req, res) => res.statusCode >= 400,
  stream: { write: (message) => logger.info(message.trim()) },
});

const errorHandler = morgan(errorResponseFormat, {
  skip: (req, res) => res.statusCode < 400,
  stream: { write: (message) => logger.error(message.trim()) },
});

module.exports = {
  successHandler,
  errorHandler,
};
```

## Define log levels

Before embarking on a build with your development team, it is very important to define your log levels in order to differentiate between log events. Managing log events in an orderly and consistent manner makes it easier to get the necessary information at a glance.

There are several log levels and it is important to know them and their uses. The developer should be able to see a detailed event and determine if it should be fixed immediately. Each log level gives a rough direction about the importance and urgency of the message:

1. **Fatal**: catastrophic situations your application cannot recover. Logging at this level usually signifies the end of the program.
2. **Error**: important events that will cause the program execution to fail.
3. **Warn**: crucial events that should be noticed to prevent failure.
4. **Info**: important events that detail a completed task.
5. **Debug**: mostly used by developers for troubleshooting.
6. **Trace**: captures every possible detail about an application's behavior during development.

## Use logs with a log management system

Depending on how big your application is, it may be helpful to pull the logs out of your application and manage them separately using a log management system. Log management systems allow you to track and analyze logs as they happen in real-time, which in turn can help improve your code.

You may not use this for small personal projects, but on a production application catering to a high scale of users, you will almost always see the use of a log management system. Some popular options are [LogRocket](https://logrocket.com/), [Sentry](https://sentry.io/welcome/), [Loggly](https://www.loggly.com/) and [Logstash](https://www.elastic.co/logstash/).

## Some good logging habits

1. **Use a Node.js Logging Library.** There are three major concerns in choosing a suitable logging library: recording, formatting, and storing messages. You need to make sure that your library of choice addresses all three concerns in a satisfactory manner. Another critical consideration for selecting a logging library is performance. Since the logger will be used a lot throughout the codebase, it can harm your application's runtime performance. Therefore, you should also investigate the performance characteristics of a library, and see how it compares to alternatives.
2. **Use the Correct Log Levels.** They provide a way to differentiate between the types of events in a system and add context to how important each event is. If you correctly utilize log levels in your application, it will be easy to distinguish between critical events that need to be immediately addressed versus purely informative events.
3. **Use Structured Logging.** When defining how your log messages look, the priority should be to make your log entries easy to read for both humans and machines. JSON is a universal favorite for structured log entries because it is ubiquitous and easily readable by humans. It is also highly machine-readable and easily converted to other formats, even when working with other programming languages.
4. **Write Descriptive Messages.** Log entries should adequately describe the events that they represent. Each message should be unique to the situation and should clearly explain the event that occurred at that point. In the event of an emergency, your log entries may be the only source of information to help you understand what happened, so it's important to get this aspect of logging right!
5. **Add the Right Amount of Context to Your Logs.** Besides writing a descriptive log message, you also need to include the right amount of context in the log entry. Context makes it possible to quickly reconstruct the actions leading up to an event. Add basic information to the log, such as the timestamp of the event and the method where it occurred (or a stack trace, in the case of errors). You should also add data points relevant to the flow of the operation that triggered the event.
6. **Avoid Logging Sensitive Information.** Sensitive information includes social security numbers, addresses, passwords, credit card details, access tokens, and similar data types. Since log messages are often stored in plain text, such data will be exposed if the logs fall into the wrong hands.
7. **Log for Auditing and Profiling Reasons.** We primarily use logs to diagnose issues and find the root cause of bugs. However, logs can also prove invaluable when auditing or profiling a system, or perhaps to generate interesting statistics about system behavior. For example, you can log details of what users are doing on the system (like user sign-ins, the resources they created or accessed, etc.).
8. **Automatically Log Uncaught Exceptions and Unhandled Promise Rejections.** When you encounter an uncaught exception or unhandled promise rejection, it is always considered good practice to crash the program. Use a process manager like PM2 to automatically restart the process and restore the program to a clean state. To understand why such an event has occurred, it's also necessary to log the details of the exception or promise rejection before exiting.
9. **Centralize and Monitor Your Logs.** Once you have implemented logging in your Node.js server, the system will rapidly create new log entries. Depending on how much traffic your application receives, this can yield gigabytes of data in a relatively short space of time. You can prevent your log files from getting too big by employing a log rotation solution that also handles cleaning up old logs. Or you can utilize a log management solution that lets you centralize, filter, and gather insights from all your logs in one place and parse or visualize them in various ways.

## Conclusion

Logging is an essential practice for developers to monitor the health of their applications. To get it right, you must choose a good logging tool, employ logging best practices and be intentional about what and why you are logging. When there are emergency situations, such as server crashes on a high-traffic day you will find yourself thanking your past self for setting up logs that help navigate the difficult situation. In the next assignment, we'll take a look at setting up cron jobs and logging into our servers.

---

## References

- https://blog.logrocket.com/node-js-logging-best-practices-essential-guide/
- https://blog.appsignal.com/2021/09/01/best-practices-for-logging-in-nodejs.html
