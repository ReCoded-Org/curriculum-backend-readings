# Joins

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



