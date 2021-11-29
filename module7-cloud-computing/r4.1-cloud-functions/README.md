# Cloud Functions

We now understand what is the serverless architecture, in this lesson, we will focus on the cloud functions used in the serverless architecture.

The objectives of this lesson are:

- Getting familiar with google cloud functions.
- Understanding how to write a cloud function.

## Introduction to Cloud Functions

Cloud Functions are an easy way to run your code in the cloud. With Cloud Functions, there are no servers to provision, manage, patch, or update. Functions automatically scale and are highly available and fault-tolerant.Cloud Functions are great for building serverless backends, doing real-time data processing, and creating intelligent apps.

With Cloud Functions you write simple, single-purpose functions that are attached to events emitted from your cloud infrastructure and services. Your Cloud Function is triggered when an event being watched is fired. Your code executes in a fully managed environment. There is no need to provision any infrastructure or worry about managing any servers.

Cloud Functions can currently be written in Javascript, Python, or Go. In the case of Javascript, they execute in a Node.js environment on Google Cloud Platform. You can take your Cloud Function and run it in any standard Node.js runtime which makes both portability and local testing a breeze.

## Connect and Extend Cloud Services

Cloud Functions provides a connective layer of logic that lets you write code to connect and extend cloud services. Listen and respond to a file upload to Cloud Storage, a log change, or an incoming message on a Cloud Pub/Sub topic. Cloud Functions augments existing cloud services and allows you to address an increasing number of use cases with arbitrary programming logic. Cloud Functions have access to the Google Service Account credential and are thus seamlessly authenticated with the majority of Google Cloud Platform services such as Datastore, Cloud Spanner, Cloud Translation API, Cloud Vision API, as well as many others.

## Events and Triggers

Cloud events are things that happen in your cloud environment.These might be things like changes to data in a database, files added to a storage system, or a new virtual machine instance being created.

Events occur whether or not you choose to respond to them. You create a response to an event with a trigger. A trigger is a declaration that you are interested in a certain event or set of events. Binding a function to a trigger allows you to capture and act on events.

---

## References

- https://developers.google.com/learn/topics/functions
- https://cloud.google.com/functions
