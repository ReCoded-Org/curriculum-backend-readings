# Model View Controller (MVC)

## Introduction to MVC projects

When beginning a new project, there are several different methods that can be used to set up the overall file structure and flow. One of the most commonly used architectural patterns is called MVC. This is an acronym for `Model`, `View`, `Controller`.
This pattern is favored because of its alignment with the computer science design principle, Separation of Concerns. By dividing up responsibilities within our file structure, we can encapsulate information to be referred to via abstraction and maintain cleaner codebases.

```
app-name-here
 |- Controllers
 |- db
 |- Models
 |- node_modules
.gitignore
index.js
package.json
package-lock.json
```

### Models

In the models folder, the files will contain our schema definition and expected fields for the model.
The naming convention for the model files is: `name-here-model.js`.

Here’s an example model using JavaScript and mongoose.

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

### Controllers

Controllers are the layer between the Model and the View. the views can use the controllers to `add`, `read`, `delete`, ...etc data.
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

### Views

In a back-end application, views are usually not implemented and rather we create a front-end app using maybe `React` to call our `api` end-points to manipulate the data in the back-end.
