## Principles Of Setting up Your Schema

Poorly designed databases can cause many problems, including wasting resources, making maintenance difficult, and hindering performance. That's why having a great database schema design is a crucial part of effective data management.
By defining categories of data and relationships between those categories, database schema design makes data much easier to retrieve, consume, manipulate, and interpret.
Without a clean, efficient, consistent database schema, you’ll struggle to make the best use of your enterprise data. For example, the same data might be duplicated in multiple locations—or even worse, might be inconsistent between these locations.

### Type of database

Most developers don't see the difference between relational database schema and MongoDB schema, but in reality, it is not the same

<img src="../assets/relationalDBmeme.png" alt="meme" width="400"/>

In a nutshell, in relational databases, models are usually independent of queries, there is no duplication of data as data will _mostly_ be separated into different tables, and it is rigid, you will have to define types and fields for your schema beforehand.

In the other hand, `MongoDB`, you have more flexibility, there are no rules, documents can have new data or fields at any point of time, no need to define types.

### Embedding vs. Referencing

One of the key points to establish a good schema design (especially, if you are using MongoDB) is whether to embed or reference your data.

#### Embedding

When a collection has a document, and, this document contains another document, another document contains another sub-document, and so on. This is called embedding or nesting.

#### When to Embed

- To retrive all data in a single query.
- Avoid expense JOINs or $lookups.
- Update all data with a single operation.
- In one-to-one or one-to-many relationships between documents.

#### Referencing

When a value of a field in your table or collection referes to a value of another field in another table or collection.

#### When to `Reference`

- If you need smaller documents or tables, your data will be separated across multiple documents or tables.
- No duplicate of data.
- To reduce accessed data not accessed on every query.
- In many-to-many relationships between tables and documents.

In general, there are few **rules** you can follow to better design your schema:

##### 1. Favor embedding over referencing unless there is a compelling reason not to.

Embedded documents are an efficient and clean way to store related data, especially data that's regularly accessed together. The more often a given workload can retrieve a single document and have all the data it needs, the more consistently high-performance your application will be.

##### 2. Needing to access an object on its own is a compelling reason not to embed.

Separate data that can be referred to from multiple places into its own collection.
This is not so much a "storage space" issue as it is a "data consistency" issue. If many records will refer to the same data it is more efficient and less error prone to update a single record and keep references to it in other places.

##### 3. Avoid JOINs and $lookups if they can be avoided, but don't be afraid if they can provide a better schema design.

Having a JOIN or `$lookup` means you are doing some kind of search in your database for the corresponding field and that operation takes time. So if you embed your data in a single object, you will spare this operation, and your query can be much faster and cleaner.

##### 4. How you model your data depends _entirely_ on your particular application's data access patterns.

This means that no matter what you read or watch, you may still need to make few changes to your schema based on your own use case and application.

## Resources

- [Schema design best practices](https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/)
- [Guide to database schema design](https://www.xplenty.com/blog/complete-guide-to-database-schema-design-guide/)
