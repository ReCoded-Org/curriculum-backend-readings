# Server-side Validation
Your API can handle different types of requests now. But does it validate the request data before processing it? The objectives of this lesson are:
1. Understanding the need for server-side validation
2. Getting familiar with implementing server-side validation

## What is Validation?
Validation can mean a lot of things, but in API land it generally means figuring out if the data being sent to the API is any good or not. Validation can happen both on client-side before sending the request or on server-side when receiving the request. Client-side validation is generally used to provide quick feedback to a user. For example, when you're submitting a form and you see a field highlighted in red saying "Required field". Basically the client validated that the field cannot be empty. However, an API must not entirely rely on client-side validation. We have talked about how the frontend need not know the underlying implementation of an API. Similarly, an API does not know what actually happened on the frontend when it receives a request from a client. That is why more often than not, the first step in processing a request is to validate the data that came with it.

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

---
## References
- https://www.apisyouwonthate.com/blog/server-side-validation-with-api-descriptions
- https://express-validator.github.io/docs/