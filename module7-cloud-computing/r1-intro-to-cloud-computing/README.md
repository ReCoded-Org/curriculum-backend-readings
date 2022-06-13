# Introduction to cloud computing

In the olden days, companies would keep physical computers at their company to run a website (aka on-premises datacenter). You might also have tried hosting your application on a hosting server that gives you a shared or dedicated hosting storage space on Virtual Private Server (VPS) to host your application. The hosting server is usually in charge of handling the infrastructure and the underlying environment like PHP preprocessor, or Node.js.

That was enough at some point in time, but then the needs grew larger when web apps were used more and more, the VPS bandwidth was not enough to accommodate the usage surge. Nor it was enough to facilitate the communications between many backend applications.

On the other hand, if the company used their physical servers, they have to manage everything, such as purchasing and installing hardware, virtualization, installing the operating system and any other required applications, setting up the network, configuring the firewall, and setting up storage for data. After doing all the setup, they become responsible for maintaining it through its entire lifecycle.

That was when the cloud infrastructure came alive. Cloud computing is the delivery of computing services such as servers, storage, databases, networking, software, analytics, intelligence, and more, over the Cloud (Internet). It provides an alternative to the on-premises data center.

In cloud computing, a cloud vendor is responsible for hardware purchase and maintenance. They also provide a wide variety of software and platform as a service. The cloud computing services will be charged based on usage, aka pay-as-you-go. The cloud environment provides an easily accessible online portal that makes it handy for the user to manage the compute, storage, network, and application resources.

## Usage of the Cloud

In this course, we have added a cloud computing module as an entry-level overview for backend students. Using cloud vendors to host and deploy a product is the current market standard everywhere. As a backend developer, you may use the cloud in the following scenarios:

- Deploy your source code on a cloud machine that acts as a server.
- Host cloud functions that are responsible for doing certain business logic as a serverless computing solution.
- Use the cloud to run fault-tolerant, auto-scaling, and containerized applications in clusters using Kubernetes or containers services.
- To host, run, and secure a remote database using either database as a service (DBaaS) offering, or a machine that hosts your Database.
- To use cloud provider's certain Backend as a service (BaaS) offering, that would enable you to run frontend apps without developing a backend.
- Use the cloud to securely store, archive, or backup your data with or without encryption using the cloud storage services.
- To run self-managed registries for packages, container images, and version control.
- You can also use the cloud to manage your network (isolate, load-balance, and proxy), connect datacenters, and manage DNS (IP to domain resolution).
- Cloud providers offer tools to monitor your application and services with analytics and logs.
- Cloud vendors also offer CDNs that would deliver your content everywhere with very low latency and high speed.
- Use the cloud to geo-locate your app in different regions for faster load time to end-user.
- Use the cloud as a security gateway to prevent various attacks aimed to overload your servers.
- You can also use the cloud to build, monitor, manage, and test your projects using code building services and CI/CD pipelines.
- Finally, you can even use the cloud to develop and write code using cloud-managed IDEs. They can be self-hosted or offered as a service and can be configured to ensure a secure remote development environment for your team by ensuring no piece of business property (source code, proprietary tools) is sitting in any personal computer.

## Advantages of cloud computing

- Cost: It reduces the huge capital costs of buying hardware and software.
- Speed: Resources can be accessed in minutes, typically within a few clicks.
- Scalability: We can increase or decrease the requirement of resources according to the business requirements.
- Productivity: While using cloud computing, we put less operational effort. We do not need to apply patches, as well as no need to maintain hardware and software. So, in this way, the IT team can be more productive and focus on achieving business goals.
- Reliability: Backup and recovery of data are less expensive and very fast for business continuity.
- Security: Many cloud vendors offer a broad set of policies, technologies, and controls that strengthen our data security.

## Cloud Technologies

All major cloud providers offer a variety of tools and stacks that help you host your applications and expose them to the internet. There are many ways to do this, each way has its benefits, cost projection, maintenance, and scaling requirements. We will summarize some of the main technologies that can be helpful to you as a backend software developer.

### Compute Instances

These are the basic units of any cloud vendor. They are computers predefined with a set of hardware (processors, RAMs, GPUs) that are run remotely through virtualization technologies. You can deploy your app directly on a compute instance via continuous delivery or by uploading it manually.

Once your source code is there on the cloud machine, you need to ensure the prerequisites to build and run it are installed, like installing Node.js, or Apache server. If you want your backend app to be available to the public, you need to also expose the port that is being listened to by your application (usually 80 for HTTP and 443 for HTTPS).

The instance will have its public IP address, you can access your app using that IP address or configure your domain DNS to forward to that IO.

Databases can also be hosted on these compute instances, by installing the DB software and exposing its ports or simply connecting to the database using the local cloud vendor subnet (subnetwork) to isolate it from the public. Alternatively, most cloud vendors offer managed, highly available database hosting that comes preconfigured with backup schedule, scaling, and data residency policy (where is your data located and under which country laws).

### Clusters & Scaling Groups

To run your instances means you are merely renting a computer. You still have to do most of the heavy lifting yourself. At some point, pages will start to load slowly, network connections start timing out and your servers are starting to creak under heavy load. Congratulations – your web app has hit scale! One of the most important concepts you will need to learn then is scaling your application. By scaling, we mean resizing or running more instances that contain the same application, and then when an instance is busy, the load is redirected towards another instance.

Servers bottlenecks are mainly due to:

CPU
Memory (RAM)
Disk I/O
Network I/O

When a webserver listens to requests, it will spawn a worker thread or process for each request that is coming to your app. The worker will be responsible to run the instructions that handle that request and responding to it up till the connection closes. The instruction might include reading/writing files to disk, connecting to other computers, or query databases, among others.

When many requests come to the server, the processor will be loaded and at some point, it will start lagging due to overloading. On the other hand, if your app uses lots of memory like querying lots of data or image processing, your server can run out of RAM quickly.

These would contribute to server errors, crashes, slow loading, or failed connections. That is why more machines are needed to balance the load.

If you are running your app inside an instance, and this load peaked at a certain time due to some promotion or advertisement that led people to your app. Then you will lose lots of customers due to their bad experience using your laggy-crashy app. Until you've figured out the problem and ran and configured more machines, it would be too late...

That's mostly an indication that you need to run your app in scaling groups or clusters. These are tools that help auto-scale your app (run more machines/containers) when needed. They are configuration files that define how your app can be installed and run. It would automatically create copies of your app, and balance the load between these machines to serve all the requests.

We will explore this more in the Kubernetes lesson.

### Serverless Architecture

Another flow that can be appealing at times is to not manage a whole backend application. Instead, you can run cloud functions, and use a backend as a service platform to host your business logic.

Such configuration is mostly favorable for mobile apps, and web frontend apps that do not necessarily require a backend.

Using the serverless architecture, directly from your frontend app (mobile, or web) you can use:

- Services like Auth0, Firebase Auth, or Congnito to offer seamless authentication.
- Databases like DynamoDB, DocumentDB, or Firestore to be queried frontend side.
- Cloud functions to create a simple HTTP server, or to run a job that interacts with databases and other services similar to a backend server without actually running a server.
- Cloud storage like AWS S3, or Google Storage to upload and persist user data.
- CDNs to deliver your app content (images, assets, js, and css files) anywhere with very high speeds.
- Analytics that logs errors and crashes that happen in your app anywhere.
- Push notifications to be able to notify your app users when an event occurs.
- Machine learning to offer labeling, translation, facial recognition, object detection, smart reply, etc.

### Continuos Integration / Continuous Delivery (CI/CD)

This isn't necessarily a cloud technology, however, most cloud providers offer it as a service in their arsenal. Plus, it does require computers to do the required pipeline for CI/CD, and cloud computers are often used for this.

Continuous integration is the practice of merging code changes back to the main branch as often as possible. The developer's changes are validated by creating a build and running automated tests against the build. By doing so, you avoid integration challenges that can happen when waiting for release day to merge changes into the release branch.

Continuous integration puts a great emphasis on testing automation to check that the application is not broken whenever new commits are integrated into the main branch.

Usually, a machine is run to build and run the tests against any code merge request.

Continuous delivery is an extension of continuous integration since it automatically deploys all code changes to a staging and/or production environment after the build stage.

This means that on top of automated testing, you have an automated release process and you can deploy your application any time by clicking a button.

CD can also refer to another practice called continuous deployment which in turn goes one step further than continuous delivery. With this practice, every change that passes all stages of your production pipeline is released to your customers. There's no human intervention, and only a failed test will prevent a new change to be deployed to production. This practice accelerates the feedback loop with your customers and takes the pressure off the team as there isn't a Release Day anymore. Developers can focus on building software, and they see their work go live minutes after they've finished working on it.

CI/CD pipelines are part of larger DevOps practices that are often offered as a service by cloud providers. Examples are Github Actions, Jenkins, AWS CodePipeline and GCP Cloud Build.

## Conclusion

In this lesson, we only scratched the surface of cloud computing. It was meant to give you an overview of how you can use the cloud to serve your role as a backend engineer.

Most of the time, you aren't required to do cloud management as a backend engineer. However, you will need to know what makes the cloud and how it can be used so you can leverage it to your product development needs.
