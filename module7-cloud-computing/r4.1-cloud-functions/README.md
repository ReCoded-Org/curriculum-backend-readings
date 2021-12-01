# Cloud Functions

We now understand what is the serverless architecture, in this lesson, we will focus on the cloud functions used in the serverless architecture.

The objectives of this lesson are:

- Getting familiar with google cloud functions.
- Understanding the different types of cloud functions.

## Introduction to Cloud Functions

Cloud Functions are an easy way to run your code in the cloud. With Cloud Functions, there are no servers to provision, manage, patch, or update. Functions automatically scale and are highly available and fault-tolerant. Cloud Functions are great for building serverless backends, doing real-time data processing, and creating intelligent apps.

With Cloud Functions you write simple, single-purpose functions that are attached to events emitted from your cloud infrastructure and services. Your Cloud Function is triggered when an event being watched is fired. Your code executes in a fully managed environment. There is no need to provision any infrastructure or worry about managing any servers.

Cloud Functions can currently be written in Javascript, Python, or Go. In the case of Javascript, they execute in a Node.js environment on Google Cloud Platform. You can take your Cloud Function and run it in any standard Node.js runtime which makes both portability and local testing a breeze.

## Connect and Extend Cloud Services

Cloud Functions provides a connective layer of logic that lets you write code to connect and extend cloud services. Listen and respond to a file upload to Cloud Storage, a log change, or an incoming message on a Cloud Pub/Sub topic. Cloud Functions augments existing cloud services and allows you to address an increasing number of use cases with arbitrary programming logic. Cloud Functions have access to the Google Service Account credential and are thus seamlessly authenticated with the majority of Google Cloud Platform services such as Datastore, Cloud Spanner, Cloud Translation API, Cloud Vision API, as well as many others.

## Events and Triggers

Cloud events are things that happen in your cloud environment. These might be things like changes to data in a database, files added to a storage system, or a new virtual machine instance being created.

Events occur whether or not you choose to respond to them. You create a response to an event with a trigger. A trigger is a declaration that you are interested in a certain event or set of events. Binding a function to a trigger allows you to capture and act on events.

## Types of Cloud Functions

There are two distinct types of Cloud Functions: HTTP functions and event-driven functions. Event-driven functions can be either background functions or CloudEvent functions, depending on which Cloud Functions runtime they are written for.

## HTTP Functions

You invoke HTTP functions from standard HTTP requests. These HTTP requests wait for the response and support handling of common HTTP request methods like GET, PUT, POST, DELETE and OPTIONS. When you use Cloud Functions, a TLS certificate is automatically provisioned for you, so all HTTP functions can be invoked via a secure connection.

This is an example using the Firebase SDK for Cloud Functions with an HTTPS trigger through building an endpoint returning the current time.
The function date returns the current server date. You can pass it a format URL Query parameter to format the date.

```js
exports.date = functions.https.onRequest((req, res) => {
  // Forbidding PUT requests.
  if (req.method === "PUT") {
    res.status(403).send("Forbidden!");
    return;
  }
  // [START usingMiddleware]
  // Enable CORS using the `cors` express middleware.
  cors(req, res, () => {
    // [END usingMiddleware]
    // Reading date format from URL query parameter.
    // [START readQueryParam]
    let format = req.query.format;
    // [END readQueryParam]
    // Reading date format from request body query parameter
    if (!format) {
      // [START readBodyParam]
      format = req.body.format;
      // [END readBodyParam]
    }
    // [START sendResponse]
    const formattedDate = moment().format(`${format}`);
    functions.logger.log("Sending Formatted date:", formattedDate);
    res.status(200).send(formattedDate);
    // [END sendResponse]
  });
});
```

## Background Functions

Before moving into background functions, we need to understand this term, Pub/Sub.

Pub/Sub, which stands for Publisher/Subscriber, allows services to communicate asynchronously, with latencies on the order of 100 milliseconds.

Pub/Sub is used for streaming analytics and data integration pipelines to ingest and distribute data. It is equally effective as messaging-oriented middleware for service integration or as a queue to parallelize tasks.

<b>What is background functions?</b>

A background function is one type of event-driven function.
You use background functions when you want to have your Cloud Function invoked indirectly in response to an event, such as a message on a Pub/Sub topic, a change in a Cloud Storage bucket, or a Firebase event.

Pub/Sub example

This example shows a Cloud Function triggered by Pub/Sub events. Every time a message is published to a Pub/Sub topic, the function is invoked, and a greeting using data derived from the message is written to the log

```js
/**
 * Background Cloud Function to be triggered by Pub/Sub.
 * This function is exported by index.js, and executed when
 * the trigger topic receives a message.
 *
 * @param {object} message The Pub/Sub message.
 * @param {object} context The event metadata.
 */
exports.helloPubSub = (message, context) => {
  const name = message.data
    ? Buffer.from(message.data, "base64").toString()
    : "World";

  console.log(`Hello, ${name}!`);
};
```

---

## References

- https://developers.google.com/learn/topics/functions
- https://cloud.google.com/functions
- https://aws.amazon.com/blogs/aws/introducing-cloudfront-functions-run-your-code-at-the-edge-with-low-latency-at-any-scale/
- https://github.com/firebase/functions-samples
