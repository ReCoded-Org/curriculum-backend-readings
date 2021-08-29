# Module 2: Databases

## Introduction to Databases
In this module, you'll learn about **databases**. Database is a general term
that refers to the data stored in a structured format. We use databases when we
want to persist data for future use. For example, in a web application, when a
user writes something in a text box, this data will be lost when the page is
refreshed -- unless this data is persisted in a database.

Databases are a ubiquitous and foundational part of backend technology.

### Introduction to relational databases

One of the most common types of databases is the **relational database**. A
relational database stores data in tables, and these tables may have *relations*
to one another. For example, you may have a table `Customer`; each row
represents a customer in your application. You may have another table 
`Order`, a customer can order many things, and each order will appear in this
table. We will later look in more detail at how the two tables are linked.

Relational databases are frequently referred to as SQL databases. SQL is a
[declarative programming
language](https://365datascience.com/tutorials/sql-tutorials/sql-declarative-language/)
that is commonly used to query for data. Not all relational databases
necessarily use SQL, but it is by far the most common, so in practice, SQL
database and relational database are synomyous terms.

The most frequently used relational databases are PostgreSQL and MySQL. There
are many offerings for SQL databases, and each may have slightly different
syntax for SQL. However, if you understand the general concept of relational
databases, you will be able to easily use different databases. 

### Understanding relational database structure
As mentioned previously, data in relational databases are usually organized in a
tabular format, similar to spreadsheets.

* A database has many tables
* A table has many rows (also known as records)
* A row has many columns (also known as fields).

For example, the previously mentioned `Customer` table may look something like
the following. Note that this is not any particular syntax but simply a
visualization of the data.

**id**|**first\_name**|**last\_name**|**registered\_at**
:-----:|:-----:|:-----:|:-----:
1|Ammar|Sammour|2012-01-02
2|Halit|Batur|2012-01-03
3|Shrreya|Bhatachaarya|2012-01-05

The `Order` table may look something like so:

**id**|**product**|**delivered**|**customer\_id**
:-----:|:-----:|:-----:|:-----:
1|Keyboard|TRUE|1
2|Mouse|FALSE|1
3|Cookies|TRUE|1
4|Rice|TRUE|2

On the `Order` table, note that there is a field called `customer_id`. This is
called a **foreign key** (or sometimes join key). This column creates a
**relation** between the `Customer` and `Order` tables: it tells us to which
customer the order belongs. This is the core of relational databases: expressing
relations between entities.

This table says that Ammar has ordered a keyboard, mouse, and cookies. He has
three orders, because there are three rows with `customer_id = 1`. Halit has ordered one item: rice (`customer_id = 2`).

### Describing relationships
We usually use the terms one-to-many and many-to-many to describe
relationships between tables. 

For example, a customer may have multiple orders. This is a one-to-many relationship,
since one customer has many orders. It should be noted that the foreign key goes
on the side that is "many". In the example above, note that the `customer_id`
key is located on the `Order` table.

For a many-to-many relationship, consider students and courses at a university.
A student can take many courses; a course also has many students. Many-to-many
relationships are [expressed slightly
differently](https://dzone.com/articles/how-to-handle-a-many-to-many-relationship-in-datab) than using a single foreign key.

See this [StackOverflow
question](https://stackoverflow.com/questions/4601703/difference-between-one-to-many-and-many-to-one-relationship)
for more details.

### SQL queries

Now that we understand the general concept behind relational data, how do we
query it? Note that every SQL database may have slightly different syntax in
terms of quotations, capitalization, commas, etc., so be sure to check. In these
examples, we will be using MySQL.

Suppose you have an existing MySQL database. To create the `customer` table (we
will now lowercase the table names by convention), you would use the `CREATE
TABLE` statement. Note that every column has a type.
[`AUTO_INCREMENT`](https://www.guru99.com/auto-increment.html) is used to
automatically generated the IDs. 

```sql
CREATE TABLE IF NOT EXISTS customer (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  
```

We can now add some data using `INSERT INTO`. Note that we do not need to
manually provide an id or a created timestamp, these are automatically generated
by MySQL.

```sql
INSERT INTO customer (first_name, last_name) VALUES ('Halit', 'Batur');
INSERT INTO customer (first_name, last_name) VALUES ('Ammar', 'Sammour');
```

Now let's `SELECT` the data -- that is, let's view the data.
```sql
SELECT * FROM customer;
```

The `*` symbol tells us to get all columns. You should see something like this:

```
 id | first_name | last_name |          created_at
----+------------+-----------+-------------------------------
  1 | Halit      | Batur     | 2021-08-29 03:33:14.559122-07
  2 | Ammar      | Sammour   | 2021-08-29 03:34:08.522222-07
(1 row)
```

However, you could select only certain columns by typing the name of the column:
```sql
SELECT first_name FROM customer;
```

Finally, let's create a table with a foreign key, the `order` table, noting the
syntax that is used to create a foreign key that references our `customer`
table.

```sql
CREATE TABLE student (
  id INT AUTO_INCREMENT PRIMARY KEY,
  product VARCHAR(255) NOT NULL,
  delivered BOOL,
  customer_id INT FOREIGN KEY REFERENCES customer(id)
);
```

### Understanding joins

**Join** refers to the process of combining two tables together based on a
common column. In this case, for example, if we want to answer, in one query,
the question: what did Ammar order? We would write a query like so:

```
SELECT product FROM order INNER JOIN customers on orders.customer_id =
customer.id WHERE customer.id = 2;
```

On your own, try running only the first part of this query and see what happens.
In your own words, what does this give you?

```
SELECT product FROM order INNER JOIN customers on orders.customer_id;
```

You can read more about [SQL
joins](https://www.educative.io/blog/what-are-sql-joins) here. There are many
types of joins, but an inner join will by far the most common one.


### Further resources for SQL
* [This repository](https://github.com/LambdaSchool/Relational-Databases) provides
a good additional resource for reviewing SQL databases and some common parts of
the query language.
* When in doubt, you can simply Google, for example, "how to select in MySQL" and check
    StackOverflow.


### SQL queries practice
Now try to run some SQL queries against the tables that you created:
* Create at least two new customers
* Create at least three orders for each customer
* Select the last names of all customers
* Select the users, sorted by oldest first (hint: use Google)
* Use the `LIMIT` keyword to select only one order
* *Optional:* write a query that returns two columns: the ID of each user and
    the number of orders for that user. Hint: you need join, use `GROUP BY`, and
    use `COUNT(*)`. Use Google to read about these.

## Introduction to NoSQL databases
In the past decade, **NoSQL** databases have become a popular way to store
databases.
There are multiple types of NoSQL databases, the most common being:
* **Document**: stores data similar to JSON
* **Key-value**: data is stored as a pair of key-values, with each value having
    a unique key that identifies it
* **Graph databases**: used to store data that is represented well by the graph
    data structure (see the later section on neo4j)

### When to use SQL vs NoSQL
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

### Introduction to MongoDB
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

### Querying in MongoDB
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

### MongoDB queries practice
* Create two collections, `customer` and `order`
* Try to insert similar data as you did in the MySQL database, but this time in
    a NoSQL database
* Try to do the same queries as the previous exercise, but in MongoDB (either
    through the command-line or JavaScript)

## ORMs
ORM stands for **object-relational mapping**. Don't let the terminology scare
you: an ORM is simply a library that makes it easier to communicate with a
database in code. For example, some popular JavaScript ORMs are
[Sequelize](https://sequelize.org/), [TypeORM](https://typeorm.io/#/), etc.
These are all libraries that help you query the database from the code.

Why is an ORM useful? Consider the case of a SQL database. Writing raw SQL
queries in the code is quite unsafe -- there is no type-checking on raw query
strings, and a single typo could cause the query to fail. Additionally,
substituting variable values into a query (such as `SELECT * FROM customer WHERE
first_name = $myVariable`) can get quite cumbersome if you are manipulating the
strings yourself.

ORMs often simply the process of fetching relations as well. For example, if you
want to get all the posts for a user, you don't have to think so hard about
concepts such as joins. The same goes at insertion time: you don't have to think
too hard about foreign keys. 

Here is an example from another Node ORM, Prisma. Knowing Prisma is not
particularly important for this example; even without knowing how Prisma works,
try to understand what the code below tries to do.

```
const createCategory = await prisma.post.create({
  data: {
    title: 'How to be Bob',
    categories: {
      create: [
        {
          assignedBy: 'Bob',
          assignedAt: new Date(),
          category: {
            create: {
              name: 'New category',
            },
          },
        },
      ],
    },
  },
});
```

Notice how this conveniently creates rows in two tables in a single function
call -- it creates a post, but it also creates a category for that post, and
finally, it assigns that category to the post. This happens all in a single
function call, in a way that feels natural to a JavaScript programmer (using
objects, functions, and so on, rather than SQL queries).


### Drawbacks of ORMs
For most use cases, ORMs are extremely convenient and should be used so that the
code is more organized. However, ORMs can be inconvenient in the case of
extremely complex queries, and it's possible that you may run into performance
problems with certain queries that may be difficult to optimize.

However, almost all ORMs allow you to use raw queries as a last resort (e.g.,
type your own SQL and pass it to a function call) to handle these cases.

### ORM lab
TODO

## Other popular databases

### Elasticsearch
[Elasticsearch](https://github.com/elastic/elasticsearch) is a database that
specializes in the search of text. While relational databases focus on a tabular
format, Elasticsearch can efficiently search through large text files, such as
application logs.

### neo4j
[neo4j](https://neo4j.com) is a [graph
database](https://aws.amazon.com/nosql/graph/). These databases are optimized
for data that can be represented easily by a [graph](http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/Graphs.html), a type of data structure
common in programming. Graphs are generally used to represent the relationships
between entities of the same type, such as in a social network (relationships between friends) or
recommendation engines (relationships between movies).

## Conclusion
You've learned a bit about the different types of databases. Think about some
applications that you like to use, and ponder what types of databases they may
be using. What tables might they have? What might those columns look like?
