# Serverless Architecture

Serverless architecture is a way to build and run applications and services without having to manage infrastructure. Your application still runs on servers, but all the server management is done by the platform you are using (For example, AWS). You no longer have to provision, scale, and maintain servers to run your applications, databases, and storage systems.

## Why use serverless architectures?

Hosting a software application on the internet usually involves managing some kind of server infrastructure. Typically this means a virtual or physical server that needs to be managed, as well as the operating system and other web server hosting processes required for your application to run. Using a virtual server from a cloud provider such as Amazon or Microsoft does mean the elimination of the physical hardware concerns, but still requires some level of management of the operating system and the web server software processes.

With a serverless architecture, you focus purely on the individual functions in your application code. Services such as AWS Lambda and Microsoft Azure Functions take care of all the physical hardware, virtual machine operating system, and web server software management. You only need to worry about your code.

## Advantages of serverless architecture

serverless architecture offers the following value propositions:

- Deploy & run. The infrastructure resources are managed by the cloud vendor. Internal IT can therefore focus on the business use case of software applications instead of managing the underlying hardware. Functions allow users to deploy application builds and configuration files necessary to provision the required hardware resources.
- Fault tolerant. Since serverless application coding is logically decoupled from the underlying infrastructure, hardware failures have minimal impact on the software development process. Users are not required to manage applications on their own.
- Low operational overhead. The infrastructure and operations management tasks are managed by cloud vendors, allowing organizations to focus their efforts on building software features. Applications are released faster, resulting in faster end-user feedback and therefore, continued improvements over the next software release cycles.
- Optimized usage-based billing. The pay-as-you-go billing model serves particularly well for small and midsize (SMB) organizations that lack the capital to establish and manage on-site data centers.
- Built-in integrations. Most cloud vendors offer integrations with a variety of services that allow users to focus on building high-quality applications instead of configuring them.

## Types of serverless architecture software

There are three primary services offered via software developed with serverless architecture:

### Function as a service

In the realm of pre-packaged services, function as a service, sometimes known as FaaS or framework as, falls in between software as a service and platform as a service.
A function is a piece of software running business logic on an operating system. Applications can be composed of many functions.

FaaS gives developers an abstraction for running web applications in response to events, without managing servers.

With Amazon Lambda (a FaaS service from Amazon Web Services, we will talk more about it later in this lesson), you can directly run your code without even managing the servers.
For example, you upload an image in the server, now the Lambda function will work for you and will automatically resize the image according to the device a user is using, be it mobile, laptop, desktop or tablet.

Think of FaaS as a ready-to-implement framework that can be easily tailored to the needs of an enterprise company.

### Backend as a service

Backend-as-a-Service (BaaS) is a cloud service model in which developers outsource all the behind-the-scenes aspects of a web or mobile application so that they only have to write and maintain the frontend. BaaS vendors provide pre-written software for activities that take place on servers, such as user authentication, database management, remote updating, and push notifications (for mobile apps), as well as cloud storage and hosting.

Let's take [Firebase](https://firebase.google.com/) as an example of BaaS.
Firebase is owned by Google. It has extensive features for building, hosting, and managing apps. The platform consists of several tools that developers need for building and managing apps. In essence, it provides all the tools developers need to build an app, launch it, and engage with the app users.

Since the backend platform gives the developer access to several ready-made services like file storage, database, authentication, they can put more effort into building excellent apps. Another superb feature of Firebase is the seamless scaling of apps. All these features work together to make Firebase one of the leading BaaS platforms today.

### Database

Database serverless frameworks access and automate your database functions. These are functions that write and read from a database and can also provide a response.

## Use case of Serverless Architecture on AWS

Amazon Web Services. is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

In this use case, we are going to look at a simple to-do list web application that enables a registered user to create, update, view, and delete items.

For this use case, we may use a few AWS serverless services:

- [AWS Lambda](https://aws.amazon.com/lambda/?c=ser&sec=uc1): is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers.

  Lambda Automatically respond to code execution requests at any scale, from a dozen events per day to hundreds of thousands per second.

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/?c=ser&sec=uc1): is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services. Using API Gateway, you can create RESTful APIs and WebSocket APIs that enable real-time two-way communication applications. API Gateway supports containerized and serverless workloads, as well as web applications.

  API Gateway handles all the tasks involved in accepting and processing up to hundreds of thousands of concurrent API calls, including traffic management, CORS support, authorization and access control, throttling, monitoring, and API version management.

- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?c=ser&sec=uc1): Fast, flexible NoSQL database service for single-digit millisecond performance at any scale.

  Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database designed to run high-performance applications at any scale. DynamoDB offers built-in security, continuous backups, automated multi-region replication, in-memory caching, and data export tools.

- [AWS Amplify](https://aws.amazon.com/amplify/hosting/): Faster, easier static web hosting with continuous deployment using the AWS Amplify Console.
  AWS Amplify offers a fully managed service for deploying and hosting static web applications globally, served via Amazon's reliable content delivery network with hundreds of points of presence globally and with built-in CI/CD workflows that accelerate your application release cycle. Simply connect your application's code repository in the Amplify console, and changes to your front end and backend are deployed in a single workflow on every code commit.

- [Amazon Cognito](https://aws.amazon.com/cognito/): Amazon Cognito lets you add user sign-up, sign-in, and access control to your web and mobile apps quickly and easily. Amazon Cognito scales to millions of users and supports sign-in with social identity providers, such as Apple, Facebook, Google, and Amazon, and enterprise identity providers via SAML 2.0 and OpenID Connect.

## Web Application components

This application consists of 3 main components outlined below.

### Front End Application

The front-end application is all the static content (HTML files, CSS files, JavaScript files, and images) that are generated by `create-react-app`. All these objects are hosted on AWS Amplify Console.

When a user connects to the web site, the needed resources are downloaded to their browser and start to run there. When the application needs to communicate with the backend it does so by issuing REST API calls to the backend.

### Back End Application (Business Logic)

The backend application is where the actual business logic is implemented. The code is implemented using Lambda functions fronted by an API Gateway REST API. In our case, we have different Lambda functions, each handling a different aspect of the application: list the to-do items, get details about a specific item, update an item, create a new item, mark an item as complete and delete an existing item. The application saves all items in a DynamoDB table.

### User Registration and Authentication

As the ToDo application contains personal information (the user's ToDo items), access is restricted only to registered and authenticated users. Each user can access only their own items.

To accomplish this, we are using Cognito User Pools, which allows users to register to the application, authenticate and so on. Only after a user is authenticated, the client will receive a JWT token which it should then use when making the REST API calls.

A web application like the to-do list may use AWS Lambda and Amazon API Gateway for its business logic and Amazon DynamoDB as its database, and AWS Amplify Console to host all static content.

## Architectural Diagram

![Architectural Diagram](../assets/to-do-list-app-architecture.png)

For more info about this use case, visit the use cases on AWS [here](https://aws.amazon.com/serverless/), or see the github repository for the whole project [here](https://github.com/aws-samples/lambda-refarch-webapp).

---

## References

- https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf
- https://aws.amazon.com/lambda/serverless-architectures-learn-more/
- https://aws.amazon.com/serverless/
- https://www.twilio.com/docs/glossary/what-is-serverless-architecture
