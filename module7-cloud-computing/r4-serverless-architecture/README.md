# Serverless Architecture

A serverless architecture is a way to build and run applications and services without having to manage infrastructure. Your application still runs on servers, but all the server management is done by the paltform you are using (For example, AWS). You no longer have to provision, scale, and maintain servers to run your applications, databases, and storage systems.

## Why use serverless architectures?

Hosting a software application on the internet usually involves managing some kind of server infrastructure. Typically this means a virtual or physical server that needs to be managed, as well as the operating system and other web server hosting processes required for your application to run. Using a virtual server from a cloud provider such as Amazon or Microsoft does mean the elimination of the physical hardware concerns, but still requires some level of management of the operating system and the web server software processes.

With a serverless architecture, you focus purely on the individual functions in your application code. Services such as AWS Lambda and Microsoft Azure Functions take care of all the physical hardware, virtual machine operating system, and web server software management. You only need to worry about your code.

## Advantages of serverless architecture

serverless architecture offers the following value propositions:

- Deploy & run. The infrastructure resources are managed by the cloud vendor. Internal IT can therefore focus on the business use case of software applications instead of managing the underlying hardware. Functions allow users to deploy application builds and configuration files necessary to provision the required hardware resources.
- Fault tolerant. Since serverless application coding is logically decoupled from the underlying infrastructure, hardware failures have minimal impact on the software development process. Users are not required to manage applications on their own.
- Low operational overhead. The infrastructure and operations management tasks are managed by cloud vendors, allowing organizations to focus their efforts on building software features. Applications are released faster, resulting in faster end-user feedback and therefore, continued improvements over the next software release cycles.
- Optimized usage-based billing. The pay-as-you-go billing model serves particularly well for small and midsize (SMB) organizations that lack the capital to establish and manage on-site data centers.
- Built-in integrations. Most cloud vendors offer integrations with a variety of services that allow users to focus on building high quality applications instead of configuring them.

## Types of serverless architecture software

There are three primary services offered via software developed with serverless architecture:

### Function as a service

In the realm of pre-packaged services, function as a service, sometimes known as FaaS or framework as, falls in between software as a service and platform as a service.

Think of FaaS as a ready-to-implement framework that can be easily tailored to the needs of an enterprise company. To be clear:

- SaaS is ready to use out of the box while FaaS is not.
- However, FaaS does not require the resources to implement that you would need if you were using PaaS.

### Backend as a service

Similar to FaaS, backend as a service (BaaS) is another serverless technology. Some will contend that BaaS takes it a step further as a NoOps offering. NoOps essentially refers to infrastructure that has been automated to the point that in-house developers have no hand in its operation.

Here’s an easy way to look at BaaS: Imagine your enterprise organization is developing a mobile app to connect employees to important information on the go. You might develop the basic application framework in-house and then outsource the functionality. This includes backend processes like:

- Accessing cloud storage
- Syncing
- Social collaboration

### Database

Database serverless frameworks access and automate your database functions. These are functions that write and read from a database and can also provide a response.

## Use case of Serverless Architecture on AWS

Amazon Web Services. is a subsidiary of Amazon providing on-demand cloud computing platforms and APIs to individuals, companies, and governments, on a metered pay-as-you-go basis.

In this use case, we are going to look at a simple to-do list web application that enables a registered user to create, update, view, and delete items.
For this use case, we may use few AWS servless services:

- [AWS Lambda](https://aws.amazon.com/lambda/?c=ser&sec=uc1): is a serverless, event-driven compute service that lets you run code for virtually any type of application or backend service without provisioning or managing servers.
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/?c=ser&sec=uc1): is a fully managed service that makes it easy for developers to create, publish, maintain, monitor, and secure APIs at any scale. APIs act as the "front door" for applications to access data, business logic, or functionality from your backend services.
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/?c=ser&sec=uc1): Fast, flexible NoSQL database service for single-digit millisecond performance at any scale.
- [AWS Amplify](https://aws.amazon.com/amplify/hosting/): Faster, easier static web hosting with continuous deployment using the AWS Amplify Console.

A web application like the to-do list may use AWS Lambda and Amazon API Gateway for its business logic and Amazon DynamoDB as its database, and AWS Amplify Console to host all static content.

## Architectural Diagram

![Architectural Diagram](../assets/to-do-list-app-architecture.png)

This architecural diagram has the following tiers:

- Presentation: The static website content hosted in Amazon S3.
- Logic: The backend application is where the actual business logic is implemented. The code is implemented using Lambda functions fronted by an API Gateway REST API.
- Data: Amazon DynamoDB is used for storing the todo list items data.

For more info about this use case, visit the use cases on AWS [here](https://aws.amazon.com/serverless/), or see the github repository for the whole project [here](https://github.com/aws-samples/lambda-refarch-webapp).

---

## References

- https://d0.awsstatic.com/whitepapers/AWS_Serverless_Multi-Tier_Architectures.pdf
- https://aws.amazon.com/lambda/serverless-architectures-learn-more/
- https://aws.amazon.com/serverless/
- https://www.twilio.com/docs/glossary/what-is-serverless-architecture
