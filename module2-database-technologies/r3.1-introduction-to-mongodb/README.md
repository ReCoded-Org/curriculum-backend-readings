# Introduction to MongoDB
[MongoDB](https://www.mongodb.com/) is the most popular NoSQL database, and it
is considered a document database. MongoDB is generally considered very
straightforward to use, because working with it is very similar to working with
JSON, which many web developers are familiar with.

### General Mongo Concepts
In MongoDB, a database has many collections. A collection has many documents (a
collection can be considered the equivalent of a table in a relational database). A
document is similar to what we know normally as JSON.

An example of a document, as taken from the Mongo docs, would look like the
below. Note that the [_id field is present on each
document](https://docs.mongodb.com/manual/core/document/#the-_id-field).
```
{
   _id: 'some_id',
   field1: value1,
   field2: value2,
   field3: value3,
   ...
   fieldN: valueN
}
```

See the [official
documentation on collections](https://docs.mongodb.com/manual/core/databases-and-collections/)
and [the official documentation on
documents](https://docs.mongodb.com/manual/core/document/) for further reference.

### JavaScript 
To get started with MongoDB, you'll want to [follow the tutorial on the
official
documentation](https://www.mongodb.com/blog/post/quick-start-nodejs-mongodb--how-to-get-connected-to-your-database) for the Node.js client. Please be sure to follow the setup on this page before trying the examples.


