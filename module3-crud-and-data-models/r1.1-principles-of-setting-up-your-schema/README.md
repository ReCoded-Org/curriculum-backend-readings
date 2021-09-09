## Principles of setting up your schema

Poorly designed databases can cause many problems, including a waste of resources, difficult maintenance, and faulty performance. That's why having a great database schema design is a crucial part of effective data management.

There are few things to focus on when creating a database schema:

- How the data will be stored (what database will be used)?
- The query performance.
- How much hardware it will take?

### Type of database

Most developers don't see the difference between relation database schema and MongoDB schema, but in reality, it is not the same

<img src="https://i.imgur.com/3yobiPB.jpg" alt="meme" width="400"/>

In a nutshell,

in `relational databases`, models are usually independent of queries, there is no duplication of data as data will _mostly_ be separated into different tables, and it is rigid, you will have to define types and fields for your schema beforehand.

in the other hand, `MongoDB`, you have more flexibility, there are no rules, documents can have new data or fields at any point of time, no need to define types.

### Embedding vs. Referencing

One of the key points to establish a good schema design (especially, if you are using MongoDB) is weither to embed or reference your data, as it can make a big difference in the performance and hardware use.

#### When to `Embed`:

- To retrive all data in a single query.
- Avoid expense JOINs or $lookups.
- Update all data with a single operation.
- In one-to-one or one-to-many relationships between documents.

#### When to `Reference`

- If you need smaller documents or tables, your data will be separated across multiple documents or tables.
- No duplicate of data.
- To reduce accessed data not accessed on every query.
- In many-to-many relationships between tables and documents.

In general, there are few `rules` you can follow to better design your schema:

1. Favor embedding over referencing unless there is a compelling reason not to.
2. Needing to access an object on its own is a compelling reason not to embed.
3. Avoid JOINs and $lookups if they can be avoided, but don't be afraid if they can provide a better schema design.
4. How you model your data depends _entirely_ on your particular application's data access patterns.

## Resources

- [schema design best practices](https://www.mongodb.com/developer/article/mongodb-schema-design-best-practices/)
