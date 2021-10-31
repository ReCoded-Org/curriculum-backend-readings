# Introduction to NoSQL databases
In the past decade, **NoSQL** databases have become a popular way to store and manage data. The objectives of this lesson are:
1. Understanding the use of NoSQL databases
2. Getting familiar with types of NoSQL databases

## What are NoSQL databases?
Although relational databases are used widely in the industry, they still have some limitations. One of the most severe limitations of relational databases is that each item can only contain one attribute. But there is often a need to store several related items in one "row" of data in the same table. With growing and changing data, relational databases can face issues with scalability.

As of today, a lot of work has gone into creating non-relational databases that are also as reliable as relational databases with the advantage that the data doesn"t have to strictly conform to some schema, or sometimes there is a schema which is so variable that it would be a huge pain to try to represent it in relational form.

These non-relational databases are often called "NoSQL" databases. They have roughly the same characteristics as SQL databases (durable, resilient, persistent, replicated, distributed, and performant) except for the major difference of not enforcing schemas (or enforcing only very loose schemas). These databases provide flexible schemas and scale easily with large amounts of data and high user loads.

"NoSQL" can be a misleading term - it does not mean we're saying "No" to SQL. Although the term originally came from calling these databases "non-SQL" but it has now evolved to mean "Not only SQL" as many of these databases support relational structures and SQL-like query languages.

### Advantages of NoSQL
NoSQL databases offer many benefits over relational databases. NoSQL databases have flexible data models, scale horizontally, have incredibly fast queries, and are easy for developers to work with.

1. **Flexible data models**: A flexible schema allows you to easily make changes to your database as requirements change. You can iterate quickly and continuously integrate new application features to provide value to your users faster.
2. **Horizontal scaling** : Most SQL databases require you to scale-up vertically (migrate to a larger, more expensive server) when you exceed the capacity requirements of your current server. Conversely, most NoSQL databases allow you to scale-out horizontally, meaning you can add cheaper, commodity servers whenever you need to.
3. **Fast queries** : Queries in NoSQL databases can be faster than SQL databases. Why? Data in SQL databases is typically normalized, so queries for a single object or entity require you to join data from multiple tables. As your tables grow in size, the joins can become expensive. However, data in NoSQL databases is typically stored in a way that is optimized for queries. The rule of thumb when you use MongoDB is data that is accessed together should be stored together. Queries typically do not require joins, so the queries are very fast.
4. **Easy for developers** : Some NoSQL databases like MongoDB map their data structures to those of popular programming languages. This mapping allows developers to store their data in the same way that they use it in their application code. While it may seem like a trivial advantage, this mapping can allow developers to write less code, leading to faster development time and fewer bugs.

### When to use NoSQL
Non-relational databases are most suited to handling large volumes of data and/or unstructured data. They're extremely popular in the world of big data because writes are fast. NoSQL databases don't enforce complicated cross-table schemas, so writes are unlikely to be a bottleneck in a system using NoSQL. Non-relational databases offer a lot of flexibility to developers, so they are also popular with early-stage startups or young tech companies with lean and agile teams.

You can read more about when to use a NoSQL database on [this blog post by MongoDB](https://www.mongodb.com/nosql-explained/when-to-use-nosql).

You can also go through this [comparison of SQL and NoSQL databases](https://www.mongodb.com/nosql-explained/nosql-vs-sql) by MongoDB.

## Types of NoSQL databases
NoSQL databases can be categorized into a few types, but there are two primary types which come to mind when we think of NoSQL databases: document stores and wide column stores.

### Document Store
A document store is basically a fancy key-value store where the key is often omitted and never used (although one does get assigned under the hood, we just don't typically care about it). The values are blobs of semi-structured data, such as JSON or XML, and we treat the data store like it's just a big array of these blobs. The query language of the document store will then allow you to filter or sort based on the content inside of those document blobs.

Popular document stores you might have heard of are [MongoDB](https://www.mongodb.com/) and [CouchDB](http://couchdb.apache.org/).

### Wide Column Store
A wide column store is somewhere in between a document store and a relational DB. It still uses tables, rows, and columns like a relational DB, but the names and formats of the columns can be different for various rows in the same table. This strategy combines the strict table structure of a relational database with the flexible content of a document store.

Popular wide column stores you may have heard of are [Cassandra](https://cassandra.apache.org/_/index.html) and [Bigtable](https://cloud.google.com/bigtable).

NoSQL databases also include Key-Value Stores like Redis, Full-Text Search Engines like Elasticsearch and Graph databases like Neo4J. But we will look into these in another lesson.

Let's move ahead to the next lesson where we will dive into MongoDB, the most popular NoSQL database used widely in the industry.

---
## References
- https://www.mongodb.com/nosql-explained
- https://www.mongodb.com/nosql-explained/nosql-vs-sql
- https://shopify.engineering/five-common-data-stores-usage