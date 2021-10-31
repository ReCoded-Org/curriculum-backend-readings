# Introduction to Databases
Welcome to the next module, where you'll learn about **databases**. The objectives of this lesson are:
1. Getting familiar with the basic concepts of databases
2. Understanding the relevance of database knowledge for backend developers

## What is a database?
A database, in the most general sense, is an organized collection of data. It is a general term that refers to data stored in a structured format in a system where it can be easily accessed, manipulated and updated.

### Why do we need a database on the backend?
In the previous module, we initially read that one of the main components of the backend architecture is the database. Data is the core of any website, application or API. Users come to a website or application looking for some kind of data - list of restaurants on a food ordering app, a vast number of products on an E-commerce site or interesting courses on an online learning platform. As the users interact with an application, they generate useful data such as ratings given to a restaurant, products added to their cart or course completion progress.

Data that doesn't disappear when an application stops running is referred to as being "persistent". Databases help us to persist data for future use or continuous use. Our APIs are incomplete without data persistence. We have already seen this while working on the assignments of module 1. We were storing data in arrays and objects, but this data is lost from memory once the app is stopped or web page is refreshed. That is why, databases are an essential component of any backend application.

Today data is becoming or probably has already become the most valuable commodity in our world, surpassing fossil fuels like oil. Should we be worried? Probably a discussion for another day, but first let's understand working with databases.

### Can data be stored only on the backend?
Of course not! On the frontend, data can be stored using [cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies) or [web storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API). However, these methods allow for storing small amounts of data which cannot be persisted as the data lifetime depends on browser session time, browser close or a fixed expiry time. Also such data stored on one client cannot be accessed by another. For example, if you were to store information about user
settings in local storage, then those settings would no longer be available on a
different browser or device -- but if you store them in a database on the backend, the user can access them from any client.

For data that needs to be persisted long-term, the client-side always relies on the backend to have a database. APIs allow clients to send and receive this data from the database through the backend server.

### How much knowledge of databases is relevant for a backend developer?
In tech companies, there are different roles and specializations and many of them are focussed on data and databases. Depending on the size, team structure and requirements of a company, there might be a Database Administrator - who is responsible for day-to-day operations on the database such as creating, updating and cleaning data records, ensuring data is available to users readily and securely. There could even be a Data Analyst - who is responsible for analyzing the data collected by the organisation and drive strategic decisions from the same. There might be a Data Scientist - who writes code to perform complex analysis on large datasets with the knowledge of statistics, probability, advanced mathematics and machine learning. Some companies might even have a Database Developer - if the product they are building and maintaining is a database itself. Other roles include Database Architect, Data Modeler and Database Tester.

However, databases being a ubiquitous and foundational technology of the backend imply that backend developers must have an overall good knowledge of databases. This means that you may not specialize as a data analyst or data scientist, but you must be able to work with databases - which includes data modelling, data querying and enabling the APIs to connect and communicate with the database.

So now that you have been introduced to databases, let's move on to the next lesson where we will learn about the most widely used type of database - relational database.

---
## References
- https://www.techopedia.com/6/28832/enterprise/databases/introduction-to-databases
- https://learnsql.com/blog/types-of-database-jobs/