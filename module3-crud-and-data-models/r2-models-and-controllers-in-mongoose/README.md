# Models and Controllers in Mongoose
Mongoose is one of the fundamental tools for manipulating data for a Node.js and MongoDB based backend. The objectives of this lesson are:
1. Getting familiar with Mongoose methods
2. Understanding implementation of models and controllers
3. Preparing to build CRUD applications using Mongoose

## Mongoose Models
We have read about models in a previous lesson. You can refer to the [Mongoose documentation for Models](https://mongoosejs.com/docs/models.html) as an end-to-end guide.

## Express Controllers
Routes are the essence of Express. We have implemented routes in previous assignments like this:
```js
app.method("<path>", callbackFunction)

// Examples
app.get("/something", callbackFunction)
app.post("/something", callbackFunction)
```

As we build more complex functionality in our project, it is the `callbackFunction` which can be extracted out of the route definition into a self-contained file and refer to as Controllers.

## Food App Example
Let's imagine that we have this food model.
```js
// models/food.js

const mongoose = require("mongoose");

const food = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  calories: {
    type: Number,
    default: 0,
    validate(value) {
      if (value < 0) throw new Error("Negative calories aren't real.");
    },
  },
});

const Food = mongoose.model("Food", food);

module.exports = food;
```
Now we are required to do CRUD operations using this model, how can we acheive that with Mongoose? We will first create a folder called `routes` with an `index.js` file where will handle all our routes.
```js
// routes/index.js

const express = require("express");
const router = express.Router();
const foodController = require("../controllers/food");

router.get("/foods", foodController.getAll);
router.post("/foods", foodController.add);
router.put("/foods/:id", foodController.update);
router.delete("/foods/:id", foodController.remove);

module.exports = router;
```
We use the Express router which is a utility method built on top of Express to make RESTful APIs even easier. As you can see this is a simple routing definition, which maps each route to a controller method. For this route file to work, we will add a line to our main `index.js` file to inform our express application to use this router. So it will finally look like:
```js
// index.js 

const express = require("express");
const router = require("./routes");

const app = express();

app.use(express.json());
app.use('/', router);

app.listen(3000);
```

Now let's build our `food-controller` for all the food data operations.
```js
// controllers/food.js

const express = require("express");
const foodModel = require("../models/food");

const foodController = {};

// Using the mongoose find() function to get all foods
foodController.all = async (request, response) => {
  const foods = await foodModel.find({});
  response.json(foods);
});

// Using the mongoose model constructor and save() function to add a new food item
foodController.add = async (request, response) => {
  const food = new foodModel(request.body);
  await food.save();
  response.status(201).json(food);
});

// Using the mongoose findByIdAndUpdate() method to update a food item
foodController.update = async (request, response) => {
    await foodModel.findByIdAndUpdate(request.params.id, request.body);
    response.json(food);
  }
});

// Using the findByIdAndDelete method to remove a food item
foodController.remove = async (request, response) => {
    const food = await foodModel.findByIdAndDelete(request.params.id);

    if (!food) response.status(404).send("No item found");
    response.status(204).json();
  }
});
```

From this example, we can see a clear separation of concerns. The food model file takes care of database schema and data operations. The route index file takes care of mapping each endpoint to a controller function. The controller file takes all food related requests, calls the relevant model function and returns the response. This makes our code modular and easily maintainable.

Our example application here does not much complex functionality. Imagine a large-scale application like an E-commerce app or a social media app, and you can visualize how separation of concerns would be helpful for the developers working on these codebases.

Now it's time to build our own Mongoose based CRUD application using the MVC pattern we just learned about.

---
## References
- https://mongoosejs.com/docs/models.html#Querying
- https://scotch.io/courses/build-an-online-shop-with-vue/routes-and-controllers
