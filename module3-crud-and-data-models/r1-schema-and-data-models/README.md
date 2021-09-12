## Intoduction to database schemas

A database schema is a blueprint or architecture of how our data will look. It doesn’t hold data itself, but instead describes the shape of the data and how it might relate to other tables or models.

<<<<<<< HEAD
For example, this is a `customer` schema in MongoDB using mongoose.
=======
A database model is a type of data model that determines the logical structure of a database. It is the high level design which defines the kind of tables, the `fields` in those tables and the `relations` between different tables.

The most popular example of a database model is the relational model, which uses a table-based format, which is the one we use in most SQL databases.

### What are database schemas?

A database schema is a `blueprint` or `architecture` of how our data will look. It doesn’t hold data itself, but instead describes the shape of the data and how it might relate to other tables or models.

For example, This is a `Customer` schema in mongoDB using mongoose.

> > > > > > > c7eff66f097a2a47f25f1ab1b06941e77c329eb9

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

module.exports = mongoose.model("Customer", customer);
```

The same `customer` schema in a MySql database.

```sql
CREATE TABLE customer (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 zipcode INT(15) default NULL,
)

```

We can see that the schema definition for the `customer` has a `name` which is a type `string` and a `zipcode` that is of type `number`.

### The Difference between data model and schema

The database schema is one that contains list of attributes and instructions to tell the database engine how data is organised whereas data model is a collection of conceptional tools for describing data, data-relationship and consistency constraints.

## Introduction to CRUD operations

When we are building APIs, we want our models to provide four basic types of functionality. The model must be able to Create, Read, Update, and Delete resources. Computer scientists often refer to these functions by the acronym `CRUD`. A model should have the ability to perform at most these four functions in order to be complete.

### CRUD and REST

### What is REST?

REST is a set of architectural constraints. API developers can implement REST in a variety of ways. When a client request is made via a RESTful API, it transfers a representation of the state of the resource to the requester or endpoint. This information, or representation, is delivered in one of several formats, JSON is the most generally popular file format to use.

### CRUD (CREATE, READ, UPDATE, DELETE)

In a REST environment, CRUD often corresponds to the HTTP methods `POST`, `GET`, `PUT`, and `DELETE`, respectively. These are the fundamental elements of a persistent storage system.

For example, imagine we are working with a system that is keeping track of meals and their corresponding prices for a restaurant. Let’s look at how we would implement CRUD operations.

- #### Create

To create resources in a REST environment, we most commonly use the HTTP POST method. POST creates a new resource of the specified resource type.
Imagine that we are adding a new food item to the stored list of dishes for this restaurant, and the dish objects are stored in a dishes resource.

Note: Use `POST` when you want to add a child resource under resources collection.

Request:
`POST http://www.myrestaurant.com/api/dishes/`

We will need to send the `dish` data too.
`

- #### Read

To read resources in a REST environment, we use the GET method. in practice, reading a resource shouldn't change any information - it should only retrieve it.

Note: technically, you can change data in a `GET` request but since we are creating a RESTful API, you shouldn't do that, and, in-general, changing data in a `GET` request would be confusing to the users of your api.

Request:
`GET http://www.myrestaurant.com/api/dishes/`

- #### Update

PUT is the HTTP method used for the CRUD operation, Update.
So if the price of Avocado Toast has gone up, we should go into the database and update that information using PUT.

Note: Use `PUT` when you want to modify a singular resource which is already a part of resources collection. `PUT` replaces the resource with the data you send in its entirety.

Request:
`PUT http://www.myrestaurant.com/dishes/1223`

- #### Delete

The CRUD operation Delete corresponds to the HTTP method DELETE. It is used to remove a resource from the system.
Let’s say that the world avocado shortage has reached a critical point, and we can no longer afford to serve this modern delicacy at all. We should go into the database and delete the item that corresponds to `"Avocado Toast"`, which we know has an `id` of 1223.

Request:
`DELETE http://www.myrestaurant.com/dishes/1223`

## Resources

- [What is REST](https://restfulapi.net/)
- [See this](https://www.educative.io/blog/crud-operations#what) for more information on how CRUD operations are performed directly on `SQL` database.
- [database schemas](https://www.educative.io/blog/what-are-database-schemas-examples#types)

```

```

```

```

```

```
