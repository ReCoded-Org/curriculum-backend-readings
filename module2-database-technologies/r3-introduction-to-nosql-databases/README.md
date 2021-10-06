# Introduction to NoSQL databases
In the past decade, **NoSQL** databases have become a popular way to store
databases.
There are multiple types of NoSQL databases, the most common being:
* **Document**: stores data similar to JSON
* **Key-value**: data is stored as a pair of key-values, with each value having
    a unique key that identifies it
* **Graph databases**: used to store data that is represented well by the graph
    data structure (see the later section on neo4j)

## When to use SQL vs NoSQL
Generally speaking, you will want to use SQL databases when your data is highly
structured. SQL databases enforce a rigid structure, which is
generally a good thing for type safety, documentation, and so on.

However, sometimes,
it may be faster or more convenient not to adhere to such a rigid structure.
This is one of the reasons that NoSQL database have emerged in popularity.

When operating at scale, SQL and NoSQL also have some differences, with SQL
primarily being more robust when it comes to potential invalid or failed
transactions. You can read more about this topic
[here](https://www.imaginarycloud.com/blog/sql-vs-nosql/#Structure).


