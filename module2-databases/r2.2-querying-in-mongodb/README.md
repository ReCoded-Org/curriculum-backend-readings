# Querying in MongoDB
How do we query data in MongoDB? The objectives of this lesson are:
1. Getting familiar with important MongoDB commands and their syntax
2. Getting familiar with fetching data from embedded documents

## Important MongoDB commands
Some of the most important MongoDB commands are as follows:
- `find()`
- `findOne()`
- `insert()`
- `insertOne()`
- `update()`
- `updateOne()`
- `remove()`
- `deleteOne()`
- `createIndex()`
- `getIndexes()`
- `count()`
- `distinct()`
- `aggregate()`
- `createCollection()`

The core of querying in MongoDB comes from the `.find()` function.

If you have a collection named `customers`, you can query for all documents in it as so:
```js
db.customers.find({})
```
The `{}` indicates that you want all documents in the `customer` collection.

To fetch specific fields, you can filter by simply passing key-value pairs as part of the parameter:
```
db.customers.find({ city: 'Istanbul' })
```
This query will filter all documents and return only those customers who are from Istanbul.

To return specific fields, we can pass another object param. For example, consider the above query to return only `first_name` for all matching documents.
```js
db.customers.find({ city: 'Istanbul' }, { first_name: 1});
```

You can browse through the different [collection methods](https://docs.mongodb.com/manual/reference/method/js-collection/) of MongoDB in their official documentation. Other than `find()`, you have `insert()`, `update()` and `remove()`. All functions can take an object as a parameter with filtering conditions for the data.

[This tutorial](https://docs.mongodb.com/manual/tutorial/query-documents/) by MongoDB is a great way to explore MongoDB queries. Select MongoDB Shell on the right where it says "Select your language" and go through the interactive tutorial.

### Querying on Embedded Documents
We can query with equality check for an entire nested document. For example, the following query selects all documents where the field `size` equals the document `{ h: 14, w: 21, uom: "cm" }`:
```js
db.inventory.find( { size: { h: 14, w: 21, uom: "cm" } } )
```

To specify a query condition on a specifc field of a nested document, we can use the dot notation. The following example selects all documents where the field `uom` nested in the size field equals `"in"`:
```js
db.inventory.find( { "size.uom": "in" } )
```

Similarly we can also query arrays and specific items within arrays. You can read more about this [here](https://docs.mongodb.com/manual/tutorial/query-arrays/).

Sometimes it can get confusing between concepts of SQL and those of MongoDB. Take a look at this [SQL to MongoDB Mapping Chart](https://docs.mongodb.com/manual/reference/sql-comparison/) as a quick reference. It also shows query commands for the same operation in each database.

Once again, it's time to move into some hands-on learning. We will now work on an assignment where we will try out different MongoDB queries.

---
## References
- https://docs.mongodb.com/v4.2/
- https://docs.mongodb.com/manual/reference/method/