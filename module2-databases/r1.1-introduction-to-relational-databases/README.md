# Introduction to Relational Databases
The objectives of this lesson are:
1. Understanding the relational model
2. Understanding the advandatages of relational databases
3. Getting familiar with popular relational databases

## The Relational Model
A database management system (DBMS) is a software package designed to define, manipulate, retrieve and manage data in a database. A DBMS generally manipulates the data itself, the data format, field names, record structure and file structure. It also defines rules to validate and manipulate this data.

Edgar F. Codd was the pioneer of the relational model for databases, who came up with what is today known as Codd's twelve rules for a database management system to be considered relational, as in a relational database management system or RDBMS. The relational model was a radical departure from the reigning hierarchical model in that it focused on the ability to search a database by content rather than by following a linked navigation system. This offered the significant advantage of allowing databases to grow and store more and more data, all without having to change or rewrite the applications that accessed that data. Even today the relational model is still used for the overwhelming majority of commercial database offerings.

If you're interested in some core CS, you can read about Codd's twelve rules [here](https://en.wikipedia.org/wiki/Codd%27s_12_rules). We'll move ahead to look at relational databases in practice.

### How do relational databases work?
A relational database is essentially a group of tables. Each table is made up of rows (also known as records) and columns (also known as fields), where a row represents a data record and a column represents a data attribute or property. The tables can have relationships between them that are defined as using a certain column in one table that references a column in another table. Every row in a table must have a primary key which is a unique value that is used to reference the specific row. If a table is related to another table, it will have a foreign key which is used to reference the related record on the related table.

For example, you may have a table `Customer` in which each row represents a customer in your application. You may have another table `Order`, a customer can place many orders, and each order will appear in this table.

The `Customer` table may look something like the following. Note that this is not any particular syntax but simply a visualization of the data in tabular format.

**id**|**first\_name**|**last\_name**|**registered\_at**
:-----:|:-----:|:-----:|:-----:
1|Joe|Smith|2012-01-02
2|Jane|Doe|2012-01-03
3|Susan|Stone|2012-01-05

The column `id` here is the primary key for the table with a unique value for each row. Each row has the properties `first_name`, `last_name` and the date the customer `registered_at`.

The `Order` table may look something like so:

**id**|**product**|**delivered**|**customer\_id**
:-----:|:-----:|:-----:|:-----:
1|Keyboard|TRUE|1
2|Mouse|FALSE|1
3|Cookies|TRUE|1
4|Rice|TRUE|2

The `Order` table also has its own primary key `id` and the fields `product` and `delivered`. Note that there is a field called `customer_id`, which is
a **foreign key**. This column creates a **relation** between the `Customer` and `Order` tables: it tells us to which customer the order belongs. This is the core of relational databases: expressing relations between entities.

This table says that Joe has ordered a Keyboard, Mouse, and Cookies. He has
three orders, because there are three rows with `customer_id = 1`. Jane has ordered one item: Rice (`customer_id = 2`). Of all orders, Joe's Mouse is yet to be delivered.

### SQL
Structured Query Language (SQL) is the industry standard language used for the management and manipulation of data in relational databases. SQL can be used to query, insert, update and modify data. All major relational databases support SQL, and that's why relational databases are frequently referred to as SQL databases. SQL is often pronouced as "sequel".

SQL is a [declarative programming language](https://365datascience.com/tutorials/sql-tutorials/sql-declarative-language/) that is commonly used to query for data. Most commercial RDBMS platforms have their own customized SQL implementations, but these tend to be fully compatible with the standard SQL, so in practice, SQL database and relational database are synomyous terms.

## Advantages of RDBMS
A Relational Database system has multiple other advantages over any other type of database, such as:
1. **Simple Model** : It does not require any complex structuring or querying processes.
2. **Data Accuracy** : Multiple tables can be related to one another, leaving no chance for duplication of data.
3. **Data Integrity** : The structured schema constraints and relational reliability amongst the tables in the database helps in avoiding the records from being imperfect, isolated or unrelated, which in turn supports ease of use, precision and stability of data.
4. **Normalization** : Normalization is the process of minimizing redundancy from a relation or set of relations and can be easily acheived in relational databases. This term often comes up when working with SQL databases, so you can read more about it [here](https://www.geeksforgeeks.org/normal-forms-in-dbms/).
5. **High Security** : RDBMS support controlled access for different users, and as the data is divided between tables, it is possible to tag a few tables as confidential and others not.

### When to use a relational database
Relational databases are typically the most mature databases: they have withstood the test of time and continue to be an industry standard tool for the reliable storage of important data. So they are pretty much to go-to choice for databases.

However, it's possible that your data doesn't conform nicely to a relational schema or your schema is changing so frequently that the rigid structure of a relational database is slowing down your development. In this case, you can consider using a non-relational database instead.

## Popular Relational Databases
The most frequently used relational databases are MySQL and PostgreSQL. There
are many other offerings for SQL databases, and each may have slightly different
syntax for SQL. However, if you understand the general concept of relational
databases, you will be able to easily use different databases.

### MySQL
MySQL is the most popular open source SQL database. It is typically used for web application development, and often accessed using PHP in what is called the [LAMP stack](https://en.wikipedia.org/wiki/LAMP_(software_bundle)).

The main advantages of MySQL are that it is easy to use, inexpensive, reliable (has been around since 1995), and has a large community of developers who can help answer questions. MySQL is durable, resilient, and persistent. You can trust MySQL to store your data and never, ever lose it.

Some of the disadvantages are that it has been known to suffer from poor performance when scaling, open source development has lagged since Oracle has taken control of MySQL, and it does not include some advanced features that developers may be used to.

### PostgreSQL
PostgreSQL is an open source SQL database that is not controlled by any corporation. It is typically used for web application development with different server-side languages.

PostgreSQL shares many of the same advantages of MySQL. It is easy to use, inexpensive, reliable and has a large community of developers. It also provides some additional features such as foreign key support without requiring complex configuration.

The main disadvantage of PostgreSQL is that sometimes it can be slower in performance than other databases such as MySQL. It is also slightly less popular than MySQL.

Some other popular RDBMS include SQLite, SQL Server and Oracle DB.

In this bootcamp we will mostly be exploring MySQL. So now that you have some more knowledge of relational databases, let's understand the structuring and querying of these databases in the next lessons.

---
## References
- https://www.techopedia.com/definition/24361/database-management-systems-dbms
- https://www.techopedia.com/6/28832/enterprise/databases/introduction-to-databases
- https://www.codecademy.com/articles/what-is-rdbms-sql
- https://shopify.engineering/five-common-data-stores-usage
- https://www.educba.com/relational-database-advantages/