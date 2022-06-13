# Principles of setting up your schema
One of the biggest strengths of a well-built backend application is the schema of its database. The objectives of this lesson are:
1. Understanding best practices of good schema design
2. Preparing to apply schema design in CRUD projects

## What is the significance of good schema design?
Poorly designed databases can cause many problems, including wasting resources, making maintenance difficult, and hindering performance. That's why having a great database schema design is a crucial part of effective data management.

By defining categories of data and relationships between those categories, database schema design makes data much easier to retrieve, consume, manipulate, and interpret.
Without a clean, efficient, consistent database schema, you'll struggle to make the best use of your enterprise data. For example, the same data might be duplicated in multiple locations or even worse, might be inconsistent between these locations.

## MongoDB schema design
In this lesson we will focus on schema design best practices for MongoDB since we will be building MongoDB based CRUD applications in this module. Developers often don't see the difference between relational database schema and MongoDB schema, but in reality, it is not the same.

<img src="../assets/relationalDBmeme.png" alt="meme" width="400"/>

We have already read about the differences between relational and non-relational databases in the previous module. So, while developers may have the tendency to design their MongoDB collections like SQL tables, that approach will lead to a poor schema design. This means ignoring the strengths of MongoDB and what it was built for.

In relational databases, models are usually independent of queries, there is no duplication of data as it will _mostly_ be separated into different tables, and it is rigid, you will have to define types and fields for your schema beforehand.

On the other hand, MongoDB gives you more flexibility, there are no rules or rather flexible rules, documents can have new data or fields at any point of time, and there is no need to define fixed types. Data is usually stored in the way it will be queried, so that queries have good performance.

## Embedding vs. Referencing
One of the key points to establish a good schema design (especially, if you are using MongoDB) is whether to embed or reference your data. We have already been introduced to these concepts in the previous module.

### Embedding
When a collection has a document, and this document contains another document, another document contains another sub-document, and so on. This is called embedding or nesting.

#### When to Embed
- To retrieve all data in a single query.
- Avoid expensive JOINs or $lookups.
- Update all data with a single operation.
- For one-to-one or one-to-many relationships between documents.

### Referencing
When the value of a field in your document refers to a value of another field in another document. This is called referencing.

#### When to Reference
- If you need smaller documents, your data will be separated across multiple documents.
- No duplication of data.
- To reduce accessing infrequently required data on every query.
- For many-to-many relationships between documents.

## Thumb Rules
In general, there are few **rules** you can follow to better design your schema:

1. **Favor embedding over referencing unless there is a compelling reason not to.**
Embedded documents are an efficient and clean way to store related data, especially data that's regularly accessed together. The more often a given workload can retrieve a single document and have all the data it needs, the more consistently high-performance your application will be.

2. **Needing to access an object on its own is a compelling reason not to embed.**
Separate data that can be referred to from multiple places into its own collection.
This is not so much a "storage space" issue as it is a "data consistency" issue. If many records will refer to the same data it is more efficient and less error prone to update a single record and keep references to it in other places.

3. **Avoid JOINs and $lookups if they can be avoided, but don't be afraid if they can provide a better schema design.**
Having a JOIN or `$lookup` means you are doing some kind of search in your database for the corresponding field and that operation takes time. So if you embed your data in a single object, you will spare this operation, and your query can be much faster and cleaner.

4. **How you model your data depends _entirely_ on your particular application's data access patterns.**
This means that no matter what you read or watch, you may still need to make few changes to your schema based on your own use case and application.

As you can see there are no absolute fixed Do's and Dont's when it comes to database schema design. There are general guidelines and the advantages and disadvantages of each. When designing your application, it always comes down to how well you have understood the core functional requirements of what you are building. And accordingly applying these guidelines with necessary tweaks to build a robust, reliable and high performance application.

You can read the complete article of MongoDB schema design best practices [here](https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/). You can also read on some database schema examples [here](https://www.educative.io/blog/what-are-database-schemas-examples).

Now let's put our learnings on schema design into practice in the next few assignments.

---
## References
- https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/
- https://www.xplenty.com/blog/complete-guide-to-database-schema-design-guide/
