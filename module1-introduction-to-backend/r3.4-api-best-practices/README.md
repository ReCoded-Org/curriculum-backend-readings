# API Best Practices

Now that we have learnt to build our own APIs, in this lesson we will cover some best practices for API development.

Although some of these suggestions may require going through more modules of the course before implementation, consider this as a guide that you can come back and refer to at any time as you progress through the course.

## What is API design?
API design is the collection of planning and architectural decisions you make when building an API. Your basic API design influences how well developers are able to consume it and even how they use it. Just like website design or product design, API design informs the user experience. Good API design principles meet initial expectations and continue to behave consistently and predictably.

Frontend developers need good UI design before building the product for their end users. Similarly backend developers need good API design because the users in this case are the frontend developers who will integrate with your API to build the end-user facing product.

## Characteristics of a well-designed API
In general, an effective API design will have the following characteristics:
- **Easy to read and work with**: A well designed API will be easy to work with, and its resources and associated operations can quickly be memorized by developers who work with it constantly.
- **Hard to misuse**: Implementing and integrating with an API with good design will be a straightforward process, and writing incorrect code will be a less likely outcome. It has informative feedback, and doesn’t enforce strict guidelines on the API’s end consumer.
- **Complete and concise**: Finally, a complete API will make it possible for developers to make full-fledged applications against the data you expose. Completeness happens over time usually, and most API designers and developers incrementally build on top of existing APIs. It is an ideal which every engineer or company with an API must strive towards.

## Here are some widely accepted best practices

Please note: This list is not necessarily exhaustive and there is always room for flexibility around these principles depending on your approach towards API design.

1. **Accept and respond with JSON**
REST APIs should accept JSON for request payload and also send responses to JSON. JSON is the standard for transferring data. Almost every networked technology can use it: JavaScript has built-in methods to encode and decode JSON either through the Fetch API or another HTTP client. Server-side technologies have libraries that can decode JSON without doing much work.

In Express, we can use the body-parser middleware to parse the JSON request body.
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.post('/', (req, res) => {
  res.json(req.body);
});

app.listen(3000, () => console.log('server started'));
```

2. **Use nouns instead of verbs in endpoint paths**
We shouldn’t use verbs in our endpoint paths. Instead, we should use the nouns which represent the entity that the endpoint that we’re retrieving or manipulating as the pathname. This is because our HTTP request method already has the verb. Having verbs in our API endpoint paths isn’t useful and it makes it unnecessarily long since it doesn’t convey any new information.

For example, we should create routes like GET `/articles` for getting news articles. Likewise, POST `/articles` is for adding a new article , PUT `/articles/:id` is for updating the article with the given id. DELETE `/articles/:id` is for deleting an existing article with the given ID. Here `articles` represents a REST API resource.

The combination of the HTTP verb and resource noun convey the purpose of an API endpoint. API endpoints like GET `/fetchArticles` or POST `/update-articles` use redundant verbs like "fetch" and "update" which is not required.

In Express, we can write these endpoints as:
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.get('/articles', (req, res) => {
  const articles = [];
  // code to retrieve an article...
  res.json(articles);
});

app.post('/articles', (req, res) => {
  // code to add a new article...
  res.json(req.body);
});

app.put('/articles/:id', (req, res) => {
  const { id } = req.params;
  // code to update an article...
  res.json(req.body);
});

app.delete('/articles/:id', (req, res) => {
  const { id } = req.params;
  // code to delete an article...
  res.json({ deleted: id });
});

app.listen(3000, () => console.log('server started'));
```

3. **Use logical nesting on endpoints**
When designing endpoints, it makes sense to group those that contain associated information. That is, if one object can contain another object, you should design the endpoint to reflect that. This is good practice regardless of whether your data is structured like this in your database. In fact, it may be advisable to avoid mirroring your database structure in your endpoints to avoid giving attackers unnecessary information.

For example, if we want an endpoint to get the comments for a news article, we should append the `/comments` path to the end of the `/articles` path.

In Express, we can write this as:
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.use(bodyParser.json());

app.get('/articles/:articleId/comments', (req, res) => {
  const { articleId } = req.params;
  const comments = [];
  // code to get comments by articleId
  res.json(comments);
});


app.listen(3000, () => console.log('server started'));
```

4. **Handle complexity elegantly**
The data you’re trying to expose can be characterized by a lot of properties which could be beneficial for the end consumer working with your API. These properties describe the base resource and isolate specific assets of information that can be manipulated with the appropriate method. An API should strive towards completion, and provide all the required information, data and resources to help developers integrate with them in a seamless manner.

However, instead of defining more resources and endpoints to cover dynamic use cases and relationships, you can sweep properties and limit responses behind the ‘?’ in a query parameter, or isolate specific component of the data the client is working with using a path parameter.

For example, let's consider a photosharing app. It could be of use to developers to get information on all the photos shared in a particular location and a specific hashtag. You also want to limit the number of results to 10 per API call to prevent server load. If the end user wants to find all photos in Boston with a hashtag #winter, the call would be: `GET /photos?location=boston&hashtag=winter&limit=10`

5. **Handle errors gracefully and return standard error codes**
To eliminate confusion for API users when an error occurs, we should handle errors gracefully and return HTTP response codes that indicate what kind of error occurred. This helps the frontend developers using our API handle the error situations gracefully on the UI of the application, which ultimately leads to a good user experience for the end users. In the previous lessons, we have already mentioned the most commonly used HTTP response status codes.

Along with error codes, try to provide good feedback through your response messages. Good feedback involves positive validation on correct implementation, and an informative error on incorrect implementation that can help users debug and correct the way they use the product. Describe your error responses well, but keep them concise and neat.

For example, if we want to reject the data from the request payload, then we should return a 400 response as follows in an Express API:
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// existing users
const users = [
  { email: 'abc@foo.com' }
]

app.use(bodyParser.json());

app.post('/users', (req, res) => {
  const { email } = req.body;
  const userExists = users.find(user => user.email === email);
  if (userExists) {
    return res.status(400).json({ error: 'User already exists' })
  }
  res.json(req.body);
});


app.listen(3000, () => console.log('server started'));
```

6. **Allow filtering, sorting, and pagination**
The databases behind a REST API can get very large. Sometimes, there’s so much data that it shouldn’t be returned all at once because it’s way too slow or will bring down our systems. Therefore, we need ways to filter items. We also need ways to paginate data so that we only return a few results at a time. We don’t want to tie up resources for too long by trying to get all the requested data at once. Filtering and pagination both increase performance by reducing the usage of server resources.

Here’s a small example where an API can accept a query string with various query parameters to let us filter out items by their fields:
```
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

// employees data in a database
const employees = [
  { firstName: 'Jane', lastName: 'Smith', age: 20 },
  //...
  { firstName: 'John', lastName: 'Smith', age: 30 },
  { firstName: 'Mary', lastName: 'Green', age: 50 },
]

app.use(bodyParser.json());

app.get('/employees', (req, res) => {
  const { firstName, lastName, age } = req.query;
  let results = [...employees];
  if (firstName) {
    results = results.filter(r => r.firstName === firstName);
  }

  if (lastName) {
    results = results.filter(r => r.lastName === lastName);
  }

  if (age) {
    results = results.filter(r => +r.age === +age);
  }
  res.json(results);
});

app.listen(3000, () => console.log('server started'));
```

7. **Maintain good security practices**
Most communication between client and server should be private since we often send and receive private information. Therefore, using SSL/TLS for security is a must. A SSL certificate isn’t too difficult to load onto a server and the cost is free or very low. There’s no reason not to make our REST APIs communicate over secure channels instead of in the open.

People shouldn’t be able to access more information that they requested. For example, a normal user shouldn’t be able to access information of another user. They also shouldn’t be able to access data of admins. To enforce the principle of least privilege, we need to add role checks either for a single role, or have more granular roles for each user.

If we choose to group users into a few roles, then the roles should have the permissions that cover all they need and no more. If we have more granular permissions for each feature that users have access to, then we have to make sure that admins can add and remove those features from each user accordingly. Also, we need to add some preset roles that can be applied to a group users so that we don’t have to do that for every user manually.

8. **Cache data to improve performance**
We can add caching to return data from the local memory cache instead of querying the database to get the data every time we want to retrieve some data that users request. The good thing about caching is that users can get data faster. However, the data that users get may be outdated. This may also lead to issues when debugging in production environments when something goes wrong as we keep seeing old data.

There are many kinds of caching solutions like Redis, in-memory caching, and more. We can change the way data is cached as our needs change.

9. **Versioning our APIs**
We should have different versions of API if we’re making any changes to them that may break clients. The versioning can be done according to semantic version (for example, 2.0.6 to indicate major version 2 and the sixth patch) like most apps do nowadays.

This way, we can gradually phase out old endpoints instead of forcing everyone to move to the new API at the same time. The v1 endpoint can stay active for people who don’t want to change, while the v2, with its shiny new features, can serve those who are ready to upgrade. This is especially important if our API is public. We should version them so that we won’t break third party apps that use our APIs.

Versioning is usually done with `/v1/`, `/v2/`, etc. added at the start of the API path.

For example, we can do that with Express as follows:
```
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

app.get('/v1/employees', (req, res) => {
  const employees = [];
  // code to get employees
  res.json(employees);
});

app.get('/v2/employees', (req, res) => {
  const employees = [];
  // different code to get employees
  res.json(employees);
});

app.listen(3000, () => console.log('server started'));
```

---
## References
- https://stoplight.io/api-design-guide/basics/
- https://swagger.io/resources/articles/best-practices-in-api-design/
- https://stackoverflow.blog/2020/03/02/best-practices-for-rest-api-design/