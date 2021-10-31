# Model View Controller (MVC)

## Introduction to MVC projects

When beginning a new project (especially, when using Express), there are several different methods that can be used to set up the overall file structure and flow. One of the most commonly used architectural patterns is called MVC. This acronym stands for "Model, View, Controller".
This pattern is favored because of its alignment with the computer science design principle, [**separation of concerns**](https://en.wikipedia.org/wiki/Separation_of_concerns). By dividing up responsibilities within our file structure, for example, we can have our db connection work in one file and api routes in another file, ...etc.

```
app-name-here
 |- controllers
 |- db
 |- models
 |- node_modules
.gitignore
index.js
package.json
package-lock.json
```

### Components Of MVC

**Model:** This consists of the structure of our data and handle the database.

**View:** The part of our application which is shown to the user.

**Controller:** Controller has all the logic to control and respond to the action, the user performs using the views.

### Models

In this folder, you can write the functionality & logics related to the database (if you aren't using ORM) like insert, fetch, update, delete queries. It takes the query request from the controller & sends the response back to the controller.
The naming convention for the model files is: `name-here-model.js`.

Here's an example model using JavaScript and Mongoose.

```js
// post-model.js

const mongoose = require("mongoose");

const post = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  body: {
    type: String,
    required: true,
  },
  createdAt: {
    type: Date(),
  },
  author: {
    type: String,
    required: true,
  },
});

module.exports = mongoose.model("Post", post);
```

### Views

In this folder, you can write HTML code for displaying a web page on the web browser. You can send the data from the controller to view for displaying data dynamically.
In a back-end application, views are usually not implemented and rather we create a front-end app using maybe `React` to call our `api` end-points to manipulate and dispaly the data in the back-end.

### Controllers

Controllers are the layer between the Model and the View. the views can use the controllers to `add`, `read`, `delete`, ...etc data.
In controllers, you can write the functionality & logic to develop dynamic web applications. It takes the data request from the views & sends it to the model and sends the response back to the views.
The naming convention for the model files is: `name-here-controller.js`.

Here is an example:

```js
// post-controller.js

const express = require('express');
const router = express.Router();
const Post = require('../models/post-model.js')

router.get('/posts', (req, res) => {
 Post.find({})
  .then((posts) => {
    res.json(posts);
  })
  .catch(console.error)
})
});
```

---

## References

- https://medium.com/geekculture/mvc-architecture-with-express-server-e35aedfe7889
- https://codingstatus.com/express-mvc-structure/
