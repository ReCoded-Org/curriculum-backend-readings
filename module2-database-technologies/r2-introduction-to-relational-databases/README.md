# Introduction to relational databases

One of the most common types of databases is the **relational database**. A
relational database stores data in tables, and these tables may have *relations*
to one another. For example, you may have a table `Customer`; each row
represents a customer in your application. You may have another table 
`Order`, a customer can order many things, and each order will appear in this
table. We will later look in more detail at how the two tables are linked.

Relational databases are frequently referred to as SQL databases. SQL
(Structured Query Language) is a
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
1|Joe|Smith|2012-01-02
2|Jane|Doe|2012-01-03
3|Susan|Stone|2012-01-05

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

This table says that Joe has ordered a keyboard, mouse, and cookies. He has
three orders, because there are three rows with `customer_id = 1`. Jane has ordered one item: rice (`customer_id = 2`).


