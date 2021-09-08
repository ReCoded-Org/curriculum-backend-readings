## Models and controllers in mongoose

Mongoose is one of the fundamental tools for manipulating data for a Node.js and MongoDB backend.

Let's imagine that we have this food model.

```js
// food-model.js

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

module.exports = Food;
```

And we are required to do the CRUD operation on this model, how can we acheive that with mongoose?
we will first create a `food-conroller` for all the food requests and place all requests in there.

#### Read

To get all the foods from our MongoDB using mongoose we can simply use the `find({})` function.

Note: we can read specific items from MongoDB using queries in the `find()` function.

[Read here](https://mongoosejs.com/docs/models.html#Querying) for more information.

Example:

```js
// food-controller.js

const express = require("express");
const foodModel = require("../models/food-model");
const app = express();

app.get("/foods", async (request, response) => {
  const foods = await foodModel.find({});
  response.send(foods);
});

module.exports = app;
```

#### Create

Create or add a new `food` item to our foods.

Example:

```js
// ...

app.post("/food", async (request, response) => {
  const food = new foodModel(request.body);
  await food.save();
  response.send(food);
});

// ...
```

#### Update

To update an item, we need to first make sure it exist by using the id to find it and then updating it, using the`findByIdAndUpdate()`, and then save the new item in the database.

Example:

```js
// ...

app.patch("/food/:id", async (request, response) => {
    await foodModel.findByIdAndUpdate(request.params.id, request.body);
    await foodModel.save();
    response.send(food);
  }
});

// ...
```

#### Delete

To delete, we need to check if the item exist by using the id to find it and then delete it, we us `findByIdAndDelete()`.

Example:

```js
// ...

app.delete("/food/:id", async (request, response) => {
    const food = await foodModel.findByIdAndDelete(request.params.id);

    if (!food) response.status(404).send("No item found");
    response.status(200).send();
  }
});

// ...
```
