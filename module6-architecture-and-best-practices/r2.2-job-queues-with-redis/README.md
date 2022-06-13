# Job Queues with Redis

After caching, another common and beneficial use case of Redis in backend applications is queues. These are called job queues or task queues. The objectives of this lesson are:
1. Understanding the use of a job queue
2. Exploring a job queue example in Node applications

## What is a job queue?

As per Wikipedia: In system software, a job queue (sometimes batch queue), is a data structure maintained by job scheduler software containing jobs to run. Users submit their programs that they want executed, "jobs", to the queue for batch processing. The scheduler software maintains the queue as the pool of jobs available for it to run.

- Sometimes a process/job can be heavy and running such jobs in parallel on a machine with limited resources can be inefficient.
- Also some jobs requires exclusive access to the system and as we all know our Node/Express APIs service requests concurrently , so that can be a problem in high-traffic scenarios.

To resolve these issues we can use a data structure called a job queue which stores/caches jobs and processes each job in a scheduled manner one by one, given that the response is not wanted immediately.

Some practical examples of job queues are:
1. **Sending emails**: Let's say that your application must send an automated email based on multiple user events like user signup, order placed, order shipped and so on. A job queue can schedule each email send in a job and process these jobs sequentially as well as store information about the email send operation and its result in the job's logs.
2. **Saving data from data store to CRM**: Let's say that your application uses MongoDB as primary data store but also needs to move the data to a CRM for the comapny's marketing team. However, the CRM cannot accept frequest data updates and also has more maintenance downtime than your primary data store. So, based on significant low frequency user events or scheduled time periods, the consolidated user data can be moved to the CRM using a job queue. If the CRM rejects the data for some reason, the error state is maintained on the failed jobs and they can be retried when circumstances are suitable again.
3. **Picture resizing or video encoding**: If you have an application that lets user upload pictures and videos, but you want to optimize the size and/or file formats, a job queue can be helpful to process these tasks in the background. For the user, the upload happens in 1 click and they don't need to know that the system actually performed much more file operations in the background.

Basically, any operation that the end user doesn't need immediate response of but the system needs to process efficiently without loss of data and the ability to check completion status and retry in case of failure, can be achieved through a job queue.

Although it is possible to implement queues directly using Redis commands, there are [many popular Node.js libraries](https://openbase.com/categories/js/best-nodejs-job-queues-libraries) available to implement queueing. As always using a library helps us to avoid reinventing the wheel and setting up boilerplate low-level code, and just focus on what our application needs as a customization.

## Creating a job queue in Node.js

Let's look at the library called [Bull](https://optimalbits.github.io/bull/) used to handle job queues in Node.js. Bull allows us to make a job queue, add jobs to it and process different types of jobs.

Installing Bull: `npm install bull --save`

Initializing the Job Queue:
```js
const Queue = require('bull');
const myJobQueue = new Queue('myJob',  'redis://127.0.0.1:6379');
```

You can add a job to the queue in your controllers:
```js
const Queue = require('bull');
const myJobQueue = new Queue('myJob', 'redis://127.0.0.1:6379');
router.post('/job-use-case', async (req, res) => {
    // your stuff 
    try {
        myJobQueue.add({ jobData:req.body.jobData });
        res.status(200).send({ success:true, message:"Job added to queue!"}
    }
    catch(err){
      res.status(200).send({ success:false }
    }
})
```

While we can add jobs to the queue from anywhere in our application, we need to define our job processor functions in one place:
```js
// jobProcessor.js
const myJobQueue = new Queue('myJob', 'redis://127.0.0.1:6379');
myJobQueue.process(function(job, done) {
    // your job complex operations 
    console.log(job.data.jobData)
    done();
});
```

As soon as the job queue receives new jobs, the job processor will process them one-by-one, completing jobs and emptying the queue. Your job processor can process many types of jobs by writing one process function for each job. As long as you add jobs to the queue with a fixed job type name, the processor can handle jobs accordingly. For example, `sendEmail`, `optimizeImage` and so on for job names.

The two parts of a job queue using Bull are also called producer and consumer. A producer creates jobs and adds them to the Redis Queue, while a consumer picks jobs from the queue and processes them.

To ensure that the job processor is always running in the background and in a separate process from the main application, you can use PM2: `pm2 start jobProcessor`

There are many more operations you can perform on a job queue such as: checking pending jobs, checking failed jobs, restarting or retrying a job, cancelling a job, scheduling a job with a time delay and so on. You can explore the Bull Queue documentation for learning about these functions and their usage.

Here are some more code examples of Bull queues:
- https://blog.logrocket.com/scale-node-js-app-using-distributed-queues/
- https://betterprogramming.pub/message-queue-using-bull-redis-and-mongodb-in-node-js-d7dedaa426ea
- https://betterprogramming.pub/using-bull-to-manage-job-queues-in-a-node-js-micro-service-stack-7a6257e64509
- https://blog.logrocket.com/asynchronous-task-processing-in-node-js-with-bull/

These days there are many ready to use admin frontends for job queues that can be easily setup and rendered on our Express applications. Basically, these provide an interactive web page or UI that helps monitor our job queues. [Arena](https://github.com/bee-queue/arena) is a popular solution used with Bull Queue and requires minimal setup code.

## Message queues

Another similar use case of Redis is the message queue which works as a pub/sub service. A message queue is a form of asynchronous service-to-service communication used in serverless and microservices architectures, which we will learn about in upcoming readings and modules. Messages are stored on the queue until they are processed and deleted. Each message is processed only once, by a single consumer. Message queues can be used to decouple heavyweight processing, to buffer or batch work, and to smooth spiky workloads.

In modern cloud architecture, applications are decoupled into smaller, independent building blocks that are easier to develop, deploy and maintain. Message queues provide communication and coordination for these distributed applications. Message queues can significantly simplify coding of decoupled applications, while improving performance, reliability and scalability.

Message queues allow different parts of a system to communicate and process operations asynchronously. A message queue provides a lightweight buffer which temporarily stores messages, and endpoints that allow software components to connect to the queue in order to send and receive messages. The messages are usually small, and can be things like requests, replies, error messages, or just plain information. To send a message, a component called a producer adds a message to the queue. The message is stored on the queue until another component called a consumer retrieves the message and does something with it.

Many producers and consumers can use the queue, but each message is processed only once, by a single consumer. For this reason, this messaging pattern is often called one-to-one, or point-to-point, communications. When a message needs to be processed by more than one consumer, message queues can be combined with Pub/Sub messaging in a fanout design pattern.

[RabbitMQ](https://www.rabbitmq.com/) is a very popular message broker library for setting up message queues in Node.js. There are also other enterprise solutions like [Simple Queue Service](https://aws.amazon.com/sqs/) by AWS. You can check out an example of using RabbitMQ in [this article](https://blog.logrocket.com/understanding-message-queuing-systems-using-rabbitmq/).

## Conclusion

Queues are very helpful in scaling up backend applications for higher peformance and reliability. Redis is a great solution to build queues on.

Note: It may not make sense to use queues in small applications like our practice assignments but most companies working on delivering highly available and reliable services make use of queueing systems in their architecture. As a result, knowledge of working with queues is a high-demand skill for a backend developer. Often these skills are expected only from intermediate or advanced backend developers, but with this curriculum and some practice you can stand out among candidates when applying for a role of a junior backend developer by listing this skill on your resume. You will also be able to talk about your understanding of queues in technical interviews.

---

## References
- https://medium.com/@piyushgupta_81472/job-queuing-in-node-express-application-ee5642541c03
- https://aws.amazon.com/message-queue/