# Module 3: Crud and data models

## Intoduction to schemas and data modeling

### Data modeling

A database model is a type of data model that determines the logical structure of a database. It is the high level design which defines the kind of tables, the `fields` in those tables and the `relations` between different tables.

The most popular example of a database model is the relational model, which uses a table-based format, which is the one we use in most SQL databases.

### What are database schemas?

A database schema is a `blueprint` or `architecture` of how our data will look. It doesn’t hold data itself, but instead describes the shape of the data and how it might relate to other tables or models.

For example, This is a `Customer` schema in mangodb using mongoose.

```js
const mongoose = require("mongoose");

const Customer = new mongoose.Schema({
  name: {
    type: String,
    required: true,
  },
  zipcode: {
    type: Number,
  },
});

module.exports = mongoose.model("Customer", Customer);
```

The same `Customer` schema in a MySql database.

```sql
CREATE TABLE customer (
 id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(50) NOT NULL,
 zipcode INT(15) default NULL,
)

```

We can see that the schema definition for the `Customer` has a `name` which is a type `string` and a `zipcode` that is of type `number`.

For more details about database schemas [see this](https://www.educative.io/blog/what-are-database-schemas-examples#types)

### The Difference between data model and schema

The database schema is one that contains list of attributes and instructions to tell the database engine how data is organised whereas Data model is a collection of conceptional tools for describing data, data-relationship and consistency constraints.

## Introduction to CRUD operations

When we are building APIs, we want our models to provide four basic types of functionality. The model must be able to Create, Read, Update, and Delete resources. Computer scientists often refer to these functions by the acronym `CRUD`. A model should have the ability to perform at most these four functions in order to be complete.

### CRUD and REST

In a REST environment, CRUD often corresponds to the HTTP methods `POST`, `GET`, `PUT`, and `DELETE`, respectively. These are the fundamental elements of a persistent storage system.

For example, imagine we are working with a system that is keeping track of meals and their corresponding prices for a restaurant. Let’s look at how we would implement CRUD operations.

#### Create

To create resources in a REST environment, we most commonly use the HTTP POST method. POST creates a new resource of the specified resource type.
Imagine that we are adding a new food item to the stored list of dishes for this restaurant, and the dish objects are stored in a dishes resource.

Request:
`POST http://www.myrestaurant.com/api/dishes/`

We will need to send the `dish` data too.

Body -

```json
{
  "dish": {
    "name": "Avocado Toast",
    "price": 8
  }
}
```

Response: Status Code - 201 (Created)

This creates a new item with a `name` value of `“Avocado Toast”` and a price value of 8. Upon successful creation, the server should return a header with a link to the newly-created resource.

#### Read

To read resources in a REST environment, we use the GET method. Reading a resource should never change any information - it should only retrieve it.

Request:
`GET http://www.myrestaurant.com/api/dishes/`

Response: Status Code - 200 (OK)

Your response should have a list of `dishes`.

Body -

```json
{
  "dishes": [
    {
      "id": 1,
      "name": "Spring Rolls",
      "price": 6
    },
    {
      "id": 2,
      "name": "Mozzarella Sticks",
      "price": 7
    },
    ...
    {
      "id": 1223,
      "name": "Avocado Toast",
      "price": 8
    },
    {
      "id": 1224,
      "name": "Muesli and Yogurt",
      "price": 5
    }
  ]
}
```

#### Update

PUT is the HTTP method used for the CRUD operation, Update.
So if the price of Avocado Toast has gone up, we should go into the database and update that information

Request:
`PUT http://www.myrestaurant.com/dishes/1223`

and we send the new data.

Body -

```json
{
  "dish": {
    "name": "Avocado Toast",
    "price": 10
  }
}
```

Response: Status Code - 200 (OK)

#### Delete

The CRUD operation Delete corresponds to the HTTP method DELETE. It is used to remove a resource from the system.
Let’s say that the world avocado shortage has reached a critical point, and we can no longer afford to serve this modern delicacy at all. We should go into the database and delete the item that corresponds to `"Avocado Toast"`, which we know has an `id` of 1223.

Request:
`DELETE http://www.myrestaurant.com/dishes/1223`

Response: Status Code - 204 (NO CONTENT)

Body - None

[See this](https://www.educative.io/blog/crud-operations#what) for more information on how these operations are performed on `SQL` database.

## Principles of setting up your schema

Poorly designed databases can cause many problems, including a waste of resources, difficult maintenance, and faulty performance. That's why having a great database schema design is a crucial part of effective data management.

There are few things to focus on when creating a database schema:

- How the data will be stored (what database will be used)?
- The query performance.
- How much hardware it will take?

### Type of database

Most developers don't see the difference between relation database schema and MongoDB schema, but in reality, it is not the same
![meme](https://i.imgur.com/3yobiPB.jpg)

In a nutshell,
relational databases, models are usually independent of queries, there is no duplication of data as data will _mostly_ be separated into different tables, and it is rigid, you will have to define types and fields for your schema beforehand.

in the other hand, MongoDB, you have more flexibility, there are no rules, documents can have new data or fields at any point of time, no need to define types.

### Embedding vs. Referencing

One of the key points to establish a good schema design (especially, if you are using MongoDB) is weither to embed or reference your data, as it can make a big difference in the performance and hardware use.

#### When to `Embed`:

- Retrive all data in a single query.
- Avoid expense JOINs or $lookups.
- Update all data with a single operation.
- In one-to-one or one-to-many relationships between documents.

#### When to `Reference`

- You will have smaller documents or tables as your data will be separated across multiple documents or tables.
- No duplicate of data.
- Infrequently accessed data not accessed on every query.
- In many-to-many relationships between tables and documents.

In general, there are few `rules` you can follow to better design you schema:

1. Favor embedding over referencing unless there is a compelling reason not to.
2. Needing to access an object on its own is a compelling reason not to embed.
3. Avoid JOINs and $lookups if they can be avoided, but don't be afraid if they can provide a better schema design.
4. How you model your data depends _entirely_ on your particular application's data access patterns.

Watch [this video](https://www.youtube.com/watch?v=leNCfU5SYR8) for a detailed explanation about schema design best practices.
