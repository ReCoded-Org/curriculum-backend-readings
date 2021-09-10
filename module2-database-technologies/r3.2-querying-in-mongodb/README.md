# Querying in MongoDB
The core of querying in MongoDB comes from the `.find()` function. We'll take a
look at how it's used in JavaScript. Be sure to check the official documentation
for the exhaustive options; we will only go over the basic ones.

If you have a collection named `customer`, you can query it as so:
```
const cursor = db.collection('customer').find({});
```

The `{}` indicates that you want all documents in the `customer` collection.

You can filter by simply passing key-value pairs as part of the parameter:

```
const cursor = db.collection('customer').find({ 'first_name': 'Halit' });
```

If you want, for example, to filter using a boolean OR, you can use `$or`.
[Check the example in the
documentation](https://docs.mongodb.com/manual/tutorial/query-documents/#specify-or-conditions). There are a number of operators, such as `$in`, `$lt` -- skim the documentation to see what is possible in MongoDB.

Refer to the [official documentation for
querying](https://docs.mongodb.com/manual/tutorial/query-documents/). Select
JavaScript in the top-right.

Additionally, [MongoDB Compass] is a graphical interface that can be used to visually run
Mongo queries. There is no difference other than convenience. It is useful to
know how to query both in command-line and graphically. 


