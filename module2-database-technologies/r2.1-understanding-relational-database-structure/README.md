### Understanding Relational Database Structure
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


