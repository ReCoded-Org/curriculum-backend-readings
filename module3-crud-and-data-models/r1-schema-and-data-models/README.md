# Introduction To Database Schemas

A database schema is a blueprint or architecture of how our data will look. It doesn’t hold data itself, but instead describes the shape and structure of the data and how it might be related to other data.

For example, this is a `customer` schema in MongoDB using Mongoose.

```js
const mongoose = require("mongoose");

const customer = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  zipcode: {
    type: Number,
  },
});

module.exports = mongoose.model("customer", customer);
```

The same `customer` schema in PostgreSQL using [Sequelize](https://sequelize.org/).

```js
const Sequelize = require("sequelize");

module.exports = (sequelize, DataTypes) => {
  const Customer = sequelize.define("customer", {
    name: {
      type: DataTypes.STRING,
      allowNull: false,
    },
    zipcode: {
      type: DataTypes.INTEGER,
    },
  });
  return Customer;
};
```

We can see that the schema definition for the `customer` has a `name` that is type `string` and a `zipcode` that is of type `number`. The `name` field is mandatory and cannot be empty.

Another concept that can be confused with the database schema is the "Model".
Models are fancy constructors compiled from schema definitions. An instance of a model is called a document. Models are responsible for creating and reading documents from the underlying MongoDB database.

## Introduction to CRUD operations

When we are building APIs, we want our models to provide four basic types of functionality. The model must be able to Create, Read, Update, and Delete resources. Computer scientists often refer to these functions by the acronym CRUD. A model should have the ability to perform at most these four functions in order to be complete.

### CRUD in REST

In a REST environment, CRUD often corresponds to the [HTTP request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) `POST`, `GET`, `PUT`, and `DELETE`, respectively. These are the fundamental elements of a persistent storage system.

For example, imagine we are working with a system that is keeping track of meals and their corresponding prices for a restaurant. Let’s look at how we would implement CRUD operations.

First of all, we need to define our food item schema (we will use mongoose for that), and let's call it "dish".

```js
const mongoose = require("mongoose");

const dish = new mongoose.Schema({
  title: {
    type: String,
    required: true,
  },
  image: {
    type: String,
    required: true,
  },
  tags: [String],
});

module.exports = mongoose.model("dish", dish);
```

#### Create

To create resources in a REST environment, we most commonly use the HTTP POST method. POST creates a new resource of the specified resource type.
Imagine that we are adding a new food item to the stored list of dishes for this restaurant, and the dish objects are stored in a dishes resource.

Note: Use `POST` when you want to add a child resource under resources collection.

Request:

`POST http://www.myrestaurant.com/api/dishes/`

We will need to send the dish data too as an object in the body.

For example

```js
{
  title: "Lasagna",
  image: "www.food.com/lasagna.jpg",
  tags: ["simple", "classic"]
}

```

On the backend side, our express route will be

```js
router.post("/dishes", async (req, res) => {
  // get the data we sent in the body
  const dishData = req.body;
  try {
    // using the create() method with Mongoose will insert the data we sent in the body to our MongoDB database
    // and return an object of that data when done
    const newDish = await DishModel.create(dishData);
    // then, we return the new created dish object
    res.status(201).json(newDish);
  } catch (err) {
    res.status(422).json({ message: err.message });
  }
});
})
```

#### Read

To read resources in a REST environment, we use the GET method. In practice, reading a resource shouldn't change any information - it should only retrieve it.

To read resources in a REST environment, we use the GET method. Reading a resource should never change any information - it should only retrieve it. REST itself is more like a set of guidelines. Technically, you can change data in a `GET` request, but since we are creating a RESTful API, you shouldn't do that. Having a GET request that updates data in your database would be confusing to the users of your API and violate the expected behavior of REST.

Request:

`GET http://www.myrestaurant.com/api/dishes/`

The express route for getting all dished will be

```js
router.get("/dishes", async (_, res) => {
  // here, we are using the find() to return all dishes from our MongoDB database
  // find() will return an array of dish objects
  const posts = await DishModel.find();
  res.json(posts);
});
```

#### Update

PUT is the HTTP method used for the CRUD operation, Update.
So if the price of Avocado Toast has gone up, we should go into the database and update that information using PUT.

Note: Use `PUT` when you want to modify a singular resource which is already a part of resources collection. `PUT` replaces the resource with the data you send in its entirety.

Request:

`PUT http://www.myrestaurant.com/dishes/:id`

We will need to send the new dish data too as an object.

For example

```js
{
  title: "New dish title",
  image: "www.food.com/dish.jpg",
  tags: ["simple", "classic"]
}
```

Note that when using Mongoose you don't have to send all the object fields, you can only send the ones that got changed.

For example, we can only send the title.

```js
{
  title: "New dish title",
}
```

Respectively, our express route for both these examples will be

```js
router.put("/dishes/:id", async (req, res) => {
  // we need the dish id in order to tell Mongoose which dish to update in our database
  const { id } = req.params;
  try {
    // the findByIdAndUpdate() will make sure the dish exist before updating it
    const updatedDish = await DishModel.findByIdAndUpdate(id, req.body, {
      // the { new: true } here is just to tell Mongoose we want the newely updated dish back
      new: true,
    });
    // we return the updated dish as a JSON object to the user
    res.json(updatedDish);
  } catch (err) {
    res.status(422).json({ message: err.message });
  }
});
```

#### Delete

The CRUD operation Delete corresponds to the HTTP method DELETE. It is used to remove a resource from the system.
Let’s say that the world avocado shortage has reached a critical point, and we can no longer afford to serve this modern delicacy at all. We should go into the database and delete the item that corresponds to **Avocado Toast**, which we know has an `id` of 1223.

Request:

`DELETE http://www.myrestaurant.com/dishes/:id`

The express route for this deleting request can be

```js
router.delete("/dishes/:id", async (req, res) => {
  const { id } = req.params;
  try {
    const dish = await PostModel.findByIdAndDelete(id);
    // the status code is 204 because we are not returning data or entities
    return res.status(204).json({ success: true });
  } catch (err) {
    res.status(422).json({ message: err.message });
  }
});
```

---

## References

- https://restfulapi.net/
- https://www.educative.io/blog/crud-operations#what
- https://www.educative.io/blog/what-are-database-schemas-examples#types
