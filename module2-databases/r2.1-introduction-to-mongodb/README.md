# Introduction to MongoDB
The objectives of this lesson are:
1. Understanding the fundamental and important concepts of MongoDB
2. Understanding how MongoDB works differently from relational databases

[MongoDB](https://www.mongodb.com/) is the most popular NoSQL database, and it
is considered a document database. MongoDB is generally considered very
straightforward to use, because working with it is very similar to working with
JSON, which many web developers are familiar with.

## Fundamental MongoDB Concepts
There are no tables, rows and columns in MongoDB but similar concepts for a non-relational structure.

### Collections: Documents and Fields
In MongoDB, a collection is the basic data-storage unit. A database can have many collections. A collection can be considered the equivalent of a table in relational databases.

A collection has many documents. A record in a MongoDB collection is basically called a document. The document, in turn, will consist of fields. It is similar to what we know normally as JSON.

A field is a name-value pair in a document. A document has zero or more fields. Fields are analogous to columns in relational databases.

An example of a document, as taken from the Mongo docs, would look like this.
<img src="../assets/document-example.svg">

Since there are no column constraints, this document can grow to hold as many new fields as required.

### _id
All documents in MongoDB have a field called `_id`. This is a required field and represents a unique value in the MongoDB document. It is like the document's primary key. If you create a new document without an `_id` field, MongoDB will automatically create the field. You can read more about this [here](https://docs.mongodb.com/manual/core/document/#the-_id-field).

Visit the [official documentation on collections](https://docs.mongodb.com/manual/core/databases-and-collections/) and the [official documentation on
documents](https://docs.mongodb.com/manual/core/document/) for further reference.

## Other Important Concepts
There are some other important concepts beyond the fundamentals.

### Indexes
Indexes support the efficient execution of queries in MongoDB. Without indexes, MongoDB must perform a collection scan, that is, scan every document in a collection, to select those documents that match the query statement. If an appropriate index exists for a query, MongoDB can use the index to limit the number of documents it must inspect.

Indexes are special data structures that store a small portion of the collection's data set in an easy to traverse form. The index stores the value of a specific field or set of fields, ordered by the value of the field. The ordering of the index entries supports efficient equality matches and range-based query operations. In addition, MongoDB can return sorted results by using the ordering in the index.

By default, MongoDB always creates a unique index on the `_id` field. While structuring your database, you can create additional indexes on other fields. You can read about the different types of indexes on the MongoDB documentation [here](https://docs.mongodb.com/manual/indexes/#index-types).

### Data Modelling
Unlike SQL databases, where you must determine and declare a table's schema before inserting data, MongoDB's collections, by default, do not require their documents to have the same schema. However, data modelling is still important and helpful for developers to define how the data is stored and what relationships exist between data entities.

Did we just say relationships? Yes, although MongoDB is known as a non-relational database, you can have one-to-many and many-to-many relationships among your collections.

MongoDB provides the following two ways to model our data:
1. **Embedded Documents** : Consider a scenario where you want to save data about blog posts and their comments. One way to model this is to embed the child document in the parent document, that is the comment documents inside the blog post document. It would look something like this:
```js
{
   _id: <ObjectId123>,
   title: "Data Modelling in MongoDB",
   body: "some long text...",
   comments: [
      { 
         _id: <ObjectId111>,
         comment: "some text...",
         author: "mike@email.com"     
      },
      { 
         _id: <ObjectId222>,
         comment: "some text...",
         author: "jake@email.com"    
      }
   ]
}
```
Embedding documents lead to better performance because we can read and update data in a single database operation, only with the caveats that it can lead to data duplication and should not exceed the allowed maximum size limit of 16MB for a document.

Embedded models should be used for one-to-many relationships where entities have a "contains" or "has a" relationship between them.

2. **References** : In this scenario, we would store blog posts and comments in separate collections and reference the blog post document in each comment document, that is the parent document is referenced in the child documents. Pretty much similar to what we would do with foreign keys in SQL databases. It would look like this:
```js
// blog post
{
  _id: <ObjectId123>,
  title: "Data Modelling in MongoDB",
  body: "some long text..."
}

// comments
{ 
  _id: <ObjectId111>,
  comment: "some text...",
  author: "mike@email.com",
  postId: <ObjectId123>. // reference to the blog post
},
{ 
  _id: <ObjectId222>,
  comment: "some text...",
  author: "jake@email.com",
  postId: <ObjectId123>    // reference to the blog post 
}
```

Referencing documents helps to avoid data duplication, represent complex many-to-many relationships and hierarchical data sets. The only disadvantage is that the data cannot be fetched in a single fast query as we need to join the related collections.

Referencing model should be used for many-to-many related hierarchical data where read performance is less important than data duplication.

### Aggregation
Aggregation operations are used to perform additional computations on the data beyond what is fetched in the read queries. Aggregation operations group values from multiple documents together, and can perform a variety of operations on the grouped data to return a single result. MongoDB provides three ways to perform aggregation: the aggregation pipeline, the map-reduce function, and single purpose aggregation methods. The aggregation pipeline is the most popularly used option. You can read more about Aggregation on MongoDB [here](https://docs.mongodb.com/manual/aggregation/).

Now that you have learned these concepts of MongoDB, let's learn about querying in MongoDB in the next lesson.

---
## References
- https://www.guru99.com/what-is-mongodb.html
- https://docs.mongodb.com/manual/introduction/
- https://docs.mongodb.com/manual/indexes/
- https://www.educative.io/edpresso/what-is-data-modeling-in-mongodb