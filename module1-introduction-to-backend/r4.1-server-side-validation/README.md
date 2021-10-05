# Server-side Validation
Your API can handle different types of requests now. But does it validate the request data before processing it? The objectives of this lesson are:
1. Understanding the need for server-side validation
2. Getting familiar with implementing validation
3. Understanding the characteristics of a good error response

## What is Validation?
Validation can mean a lot of things, but in API land it generally means figuring out if the data being sent to the API is any good or not. Validation can happen both on client-side before sending the request or on server-side when receiving the request. Client-side validation is generally used to provide quick feedback to a user. For example, when you're submitting a form and you see a field highlighted in red saying "Required field", basically what happened is the client validated that the field cannot be empty. However, an API must not entirely rely on client-side validation. Even if it might seem redundant to have validation both on frontend and backend, it is essential from the perspective of security and reliability of your backend application. We have talked about how the frontend need not know the underlying implementation of an API. Similarly, an API does not know what actually happened on the frontend when it receives a request from a client. It is also possible that requests are coming from a source like Postman where there is no client-side validation. That is why more often than not, the first step in processing a request is to validate the data that came with it.

There might also be scenarios where the frontend cannot perform the validation. Consider this example: The API receives a signup request with an email ID. In case it turns out that this email ID was already used with a previous user account, it could cause issues if the new signup request is processed. So the API must first validate the email ID from the user database and inform the client accordingly. The frontend has no way by itself to check if the email ID was used in a previous user account.

Validation ensures that your API performs optimally irrespective of what kind of requests it receives.

### Types of Validation
1. **required**: Specifies whether a data parameter needs to be provided before the request can be processed.
2. **minlength and maxlength**: Specifies the minimum and maximum length of textual data parameters.
3. **min and max**: Specifies the minimum and maximum values of numerical data parameters.
4. **type**: Specifies whether the data parameter needs to be a number, an email address, or some other specific preset type. 
5. **pattern**: Specifies a [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions) that defines a pattern the data parameter needs to follow.
6. **business rules validation**: Specifies whether a request can be processed based on custom business rules. For example, a customer can use only 2 coupon codes in a day or a user cannot use the same email ID for more than one user account.

### Implementing Validation
You might be thinking do I have to write a bunch of if statements within my API routes for validation? Earlier this used to be the case, but now we have ready to use libraries that can be easily configured to setup validation on our APIs.

We will be learning to use [express-validator](https://express-validator.github.io/docs/) in the next assignment.

Consider this piece of code:
```js
// ...initial code omitted for simplicity
const { body, validationResult } = require('express-validator');

app.post(
  '/user',
  // username must be an email
  body('username').isEmail(),
  // password must be at least 5 chars long
  body('password').isLength({ min: 5 }),
  (req, res) => {
    // Finds the validation errors in this request and wraps them in an object with handy functions
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    // ...later code omitted for simplicity
  },
);
```

Now, whenever a request that includes invalid username or password fields is submitted, your server will respond with a 400 error response like this:
```json
{
  "errors": [
    {
      "location": "body",
      "msg": "Invalid value",
      "param": "username"
    }
  ]
}
```

Basic validations can be handled by such middleware. However, custom validations based on specific business rules may require custom code. In any case, your server-side application must have a high level of validation across API routes and test cases ensuring that each and every erroneous possibility is checked and handled by sending a validation error response. A good validation response will help the frontend developers using your API to display graceful error messages to the end-user.

## What makes a good error response?
Error messages are almost the last thing that any developer wants to see in an API response. But an error message that doesn't tell the developer anything about what went wrong is even worse. Error codes and error messages are probably the most useful diagnostic element in the API space, and it is surprising, how little attention sometimes developers pay them.

Error codes in the response of an API is the fundamental way in which a developer can communicate failure to a user as well as jump-start the error resolution process. A user doesn't choose when an error is generated, or what error it gets. So error responses are the only truly constant, consistent communication the user can depend on when an error has occurred. Error codes have an implied value in the way that they both *clarify the situation*, and communicate the *required solution*.

Consider for instance an error code such as `401 Unauthorized – Please Pass Token`. In such a response, you understand the point of failure, specifically that the user is unauthorized. Additionally, however, you discover the intended functionality — the API requires a token, and that token must be passed as part of the request in order to gain authorization.

Essentially there are three parts to a good error response:
1. **An HTTP Status Code**: We have already talked about these in the previous lessons on API best practices and REST APIs.
2. **An Internal Reference ID**: For documentation-specific notation of errors. In some cases, this can replace the HTTP Status Code, as long as the internal reference sheet includes the HTTP Status Code scheme or similar reference material.
3. **Human readable messages**: To summarize the context, cause, and general solution for the error at hand.

Let's look at some examples.

### Twitter API
Let's attempt to send a GET request to retrieve our mentions timeline.
```
https://api.twitter.com/1.1/statuses/mentions_timeline.json
```

When this is sent to the Twitter API, we receive the following response:
```
HTTP/1.1 400 Bad Request
x-connection-hash:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
set-cookie:
guest_id=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Date:
Thu, 01 Jun 2017 03:04:23 GMT
Content-Length:
62
x-response-time:
5
strict-transport-security:
max-age=631138519
Connection:
keep-alive
Content-Type:
application/json; charset=utf-8
Server:
tsa_b
 
{"errors":[{"code":215,"message":"Bad Authentication data."}]}
```

Looking at this data, we can generally figure out what our issue is. First, we're told that we've submitted a 400 Bad Request. This tells us that the problem is somewhere in our request. Our content length is acceptable, and our response time is well within normal limits. We can see, however, that we're receiving a unique error code that Twitter itself has denoted — “215”, with an attached message that states “Bad Authentication data”. This tells us that the fix is to supply authentication data, but also gives us a number to reference on the internal documentation of the Twitter API for further details.

### Facebook
Let's pass a GET request to ascertain some details about a user. All personal information will be blanked out for security purposes.
```
https://graph.facebook.com/v2.9/me?fields=id%2Cname%2Cpicture%2C%20picture&access_token=xxxxxxxxxxx
```

This request should give us a few basic fields from this user's Facebook profile, including id, name, and picture. Instead, we get this error response:
```
{
  "error": {
    "message": "Syntax error \"Field picture specified more than once. This is only possible before version 2.1\" at character 23: id,name,picture,picture",
    "type": "OAuthException",
    "code": 2500,
    "fbtrace_id": "xxxxxxxxxxx"
  }
}
```

While Facebook doesn't directly pass the HTTP error code in the body, it does pass a lot of useful information. The “message” area notes that we've run into a syntax error, specifically that we've defined the “picture” field more than once. Additionally, this field lets us know that this behavior was possible in previous versions, which is a very useful tool to communicate to users a change in behavior from previous versions to the current. Additionally, we are provided both a code and an `fbtrace_id` that can be used with support to identify specific issues in more complex cases. We've also received a specific error type, in this case `OAuthException`, which can be used to narrow down the specifics of the case even further.

Let's put these learnings about validation into practice in the next assignment.

---
## References
- https://www.apisyouwonthate.com/blog/server-side-validation-with-api-descriptions
- https://express-validator.github.io/docs/
- https://nordicapis.com/best-practices-api-error-handling/