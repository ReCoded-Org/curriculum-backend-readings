### Understanding Relational Database Structure
We usually use the terms one-to-many and many-to-many to describe
relationships between tables. 

For example, a customer may have multiple orders. This is a one-to-many relationship,
since one customer has many orders. It should be noted that the foreign key goes
on the side that is "many". In the example above, note that the `customer_id`
key is located on the `Order` table.

![One to many relationship](../assets/one-to-many.png)

For a many-to-many relationship, consider students and courses at a university.
A student can take many courses; a course also has many students. Many-to-many
relationships are [expressed slightly
differently](https://dzone.com/articles/how-to-handle-a-many-to-many-relationship-in-datab) than using a single foreign key.

To express a many-to-many relationship between two tables, we create a third
table that contains the foreign keys of the two tables being connected. For
example, the diagram below connects classes and students together through a
table called `Enrollments`. Each row in `Enrollments` represents one class that
one student is taking; there can be multiple such entries in the table.

![Many to many relationship](../assets/many-to-many.png)

See this [StackOverflow
question](https://stackoverflow.com/questions/4601703/difference-between-one-to-many-and-many-to-one-relationship)
for more details.


