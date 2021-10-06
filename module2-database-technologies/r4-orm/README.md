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


