# API Documentation
Think about an API you have used previously. How did you know what endpoints to call and what data to pass in your requests? You read the documentation. The objectives of this lesson:
1. Understand the principles of writing good API documentation
2. Get familiar with API documentation tools

## What is API documentation?
API documentation is a reference document that outlines how to use the API. It's a technical manual that contains information about the services the API offers, how to use its various endpoints and parameters, and other implementation instructions. With good API documentation, developers can understand the usage of an API and incorporate it into their use cases without experiencing programming obstacles. There are three types of API documentation.
1. **Reference documentation**: provides information about the structure, parameters, and return values for each function or method in an API.
2. **Tutorials**: provide step-by-step instructions for using APIs to accomplish specific tasks or workflows with detailed explanations about using the endpoints and parameters in each function call.
3. **Conceptual documentation**: provides information about using APIs to build applications rather than just describing what each function does individually; it also includes details on integrating multiple APIs into a single application.

## Why is API documentation important?
In previous lessons we have mentioned that as a backend developer, quite often the end-users of the product you are building will be frontend developers. They need not know how you have built the backend or implemented the endpoints, but they must how to use your API on the frontend. Just like a frontend developer tries to deliver a great user experience in the websites they build, good API documentation is a way to deliver good user experience for your end-users. And if you are building an API for public use, good API documentation will increase the adoption of your product and services.

## Principles of good API documentation

### 1. Plan for your docs
Before you begin documenting, you should know who you are creating the docs for. If you know your audience, it'll assist you to decide on the language, structure and design of your documentation.

### 2. Include fundamental sections
There are fundamental sections that are essential for enhancing the readability and adoption of your API. You can tailor them based on the needs you want to address with your documentation. Some common sections include Overview (conveying what your API is about quickly), Authentication (clearly explains how to get the access credentials), Resources (provide all the necessary information about requests and responses) and Error messages (list of possible error codes and messages).

### 3. Be consistent and avoid jargon
Maintain consistency in the use of terminology throughout your documentation. Your docs should be entirely uniform and without contradictions in language and code. You should sufficiently proofread your documentation to eliminate sections that are ambiguous or difficult to understand. Also you should keep the docs free from unnecessary technical jargon, as much as possible. Assuming that your audience is completely technical and understands how APIs work can be a big mistake. Good documentation should be easily understood by people new to working with APIs.

### 4. Include interactive examples and other resources
More than anything, most developers like it when they can test what they read in the documentation and see how it works. If you can include interactive sample codes in the most popular programming languages, it can greatly reduce the friction in implementing your API. You can also include a sandbox environment filled with test data so that users can run requests and see the types of responses returned.

### 5. Maintain API Docs
Ensuring your docs remain accurate and up-to-date is critical for its success. If your API descriptions are obsolete, users can get frustrated and lose trust in your services. In case any new feature has been introduced into the API, ensure it's properly and timely documented. You can also version the API documentation to reflect the newly added features. If a feature has been removed from your API, take it from the documentation and explain the reasons behind the decision.

## API Documentation Tools

In case you were thinking do I have to write both code and documentation, the answer is no you actually don't have to write all your documentation from scratch. There are some popular tools to put together your API documentation.

### Swagger
[Swagger](https://swagger.io/tools/swagger-ui/) is a software tool used for designing, building, documenting, and using RESTful APIs. It follows the OpenAPI specification. The OpenAPI specification is a specification used for creating interfaces used in describing, producing, consuming, and visualizing RESTful APIs. It is also known as the swagger specification. With the help of just some JSON configurations, Swagger lets you easily setup an interactive API documentation. You can take a look at this [Swagger example of a pet store API](https://petstore.swagger.io/) to see what the final documentation looks like.

### GitBook
[GitBook](https://docs.gitbook.com/) is another modern documentation tool useful for API documentation. Using a GitHub repo and the GitBook tool, you can create, manage and host your API documentation easily. If you're familiar with React and Redux, then take a look at the [Redux documentation created using GitBook](https://redux.js.org/api/api-reference).

### Postman
You have already been using Postman to test APIs. Another great feature of Postman is API documentation. You can read more about it [here](https://learning.postman.com/docs/publishing-your-api/documenting-your-api/).

In the next assignment, you will put together your own interactive API documentation.

---
## References
- https://blog.api.rakuten.net/best-practices-for-writing-api-documentation/
- https://hackernoon.com/how-to-write-great-api-documentation-c710cd1c696
- https://swagger.io/blog/api-documentation/create-compelling-easy-to-use-api-documentation/
- https://strapi.io/blog/gitbook-open-source-documentation