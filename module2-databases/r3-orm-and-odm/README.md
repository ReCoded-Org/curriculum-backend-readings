# ORMs
So far we have looked at standalone databases and performed queries directly on them. But what happens when we want our backend code to interact with the database? The objectives of this lesson are:
1. Understand ORMs and how they are useful
2. Understand ODMs and how they are useful

## ORM
ORM stands for **Object Relational Mapping**. Don't let the terminology scare
you: an ORM is simply a library that makes it easier to communicate with a
database in code. It is basically a technique to query or perform CRUD (Create, Read, Update, Delete) operations to the database, mainly RDBMS (Relational Databases), using an object-oriented paradigm. With the help of ORM, you don"t actually need to use SQL at all. You can directly interact with the database and perform queries in the same language you are using for your back-end code!

For example, some popular JavaScript ORMs are [Sequelize](https://sequelize.org/) and [TypeORM](https://typeorm.io/#/). These are all libraries that help you query the database from the code.

Let's take the example of inserting data. Without an ORM your code would look something like this:
```js
const mysql = require("mysql");
const conn = mysql.createConnection({
	host: "localhost",
	user: "your_username",
	password: "you_password",
	database: "mydb",
});

conn.connect(function (error) {
	if (error) {
		console.log(error);
	} else {
		console.log("Connected!");
    let sql = "INSERT INTO Users (username, password) VALUES ('john-doe', 'randompassword')";
    conn.query(sql, function (error, result) {
      if (error) {
        console.log(error);
      } else {
        console.log(result);
      }
    });
  }
});
```

Using Sequelize, the same code would become:
```js
const Sequelize = require("sequelize");
const sequelize = new Sequelize("mydb1", "your_username", "your_password", {
	dialect: "mysql",
});

//Defining User model
const User = sequelize.define("User", {
	username: Sequelize.STRING,
	password: Sequelize.STRING,
});

sequelize.sync();

User.create({
	username: "john-doe",
	password: "randompassword",
}).then(function (user) {
	console.log(user);
});
```

### Why is an ORM useful?
Consider the case of a SQL database. Writing raw SQL queries in the code is quite unsafe -- there is no type-checking on raw query strings, and a single typo could cause the query to fail. Additionally, substituting variable values into a query (such as `SELECT * FROM customer WHERE first_name = $myVariable`) can get quite cumbersome if you are manipulating the strings yourself.

ORMs often simplify the process of fetching relationships as well. For example, if you
want to get all the posts for a user, you don't have to think so hard about
concepts such as joins. The same goes at insertion time: you don't have to think
too hard about foreign keys. 

Here is an example from another Node ORM, [Prisma](https://www.prisma.io/). Knowing Prisma is not particularly important for this example; even without knowing how Prisma works, try to understand what the code below tries to do.
```js
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

## ODM
ODM stands for **Object Document Mapping**. It is like an ORM for non-relational databases such as MongoDB, i.e., mapping an object model and NoSQL database.

Once again, let's look at the example of inserting data in MongoDB without using an ODM.
```js
const MongoClient = require("mongodb").MongoClient;
const url = "mongodb://localhost:27017/";

MongoClient.connect(url, function (error, db) {
	if (error) throw error;
	const mydb = db.db("mydb");
	const user = { username: "john-doe", password: "randompassword" };

	mydb.collection("users").insertOne(user, function (error, result) {
		if (error) throw error;
		console.log(result);
	});
});
```

But using an ODM like [Mongoose](https://mongoosejs.com/) the code becomes:
```js
const mongoose = require("mongoose");
// Database Connection
mongoose.connect("mongodb://127.0.0.1:27017/mydb1", {
	useNewUrlParser: true,
	useCreateIndex: true,
	useUnifiedTopology: true,
});

//user model
const User = mongoose.model("User", {
	username: { type: String },
	password: { type: String },
});

//new user object
const newUser = new User({
	username: "john-doe",
	password: "randompassword",
});

//inserting the document in collection
newUser.save(function (error, result) {
	if (error) {
		console.log(error);
	} else {
		console.log(result);
	}
});
```

### Why is an ODM useful?
An ODM like Mongoose allows a predefined schema, collection validation and constraints which are helpful from the application maintainability perspective for developers. It provides an additional layer of abstraction on top of the MongoDB driver for Node.js.

In the next module, we will implement CRUD operations on persistent databases using ORM/ODM on our Node.js applications.

---
## References
- https://medium.com/spidernitt/orm-and-odm-a-brief-introduction-369046ec57eb
- https://www.geeksforgeeks.org/what-are-the-advantages-of-using-mongoose-module/
