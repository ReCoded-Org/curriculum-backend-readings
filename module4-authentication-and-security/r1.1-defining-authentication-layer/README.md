# Defining Authentication Layer

Authentication is used by a backend web app when it needs to know exactly who is accessing their information or site, and that the request is authentic, which means it is coming from the expected user. The objectives of this lesson are:

- Learn how to define user models in a database
- Define endpoints and controllers to register, login, and validate a user

## Defining user models

As you've learned, an object model is a code-representation of data in the Database, it defines the object attributes and relationships. Using an ORM, you can easily build a model for any data representation.

In this section, Sequelize will be used to define a user model using the sqlite3 database. [Sequelize](https://sequelize.org/master/manual/getting-started.html) is an ORM that helps us create models for any type of database, and it handles querying and persisting these data schemas. Below is a simple example to define a `User` model.

Below is how we define an SQLite3 database with Sequelize

```js
// ./db.js

const Sequelize = require("sequelize");

// Import all your models
const User = require("./models/user");

// Instantiate a new sequelize instance to use SQLite
const sequelize = new Sequelize({
  dialect: "sqlite",
  storage: "db.sqlite",
});

const models = {
  User: User.init(sequelize, Sequelize),
};

// to import a model:
// const { User } = require(PATH_TO_THIS_FILE);
module.exports = { ...models, sequelize };
```

And here is the model:

```js
// ./models/user.js
const { Model } = require("sequelize");
const bcrypt = require("bcrypt");

class User extends Model {
  // Instead of constructor, we use static init function just like the super class
  // Our tablename will be pluralized from class name, i.e. : Users
  static init(sequelize, DataTypes) {
    // https://sequelize.org/master/class/lib/model.js~Model.html#static-method-init
    return super.init(
      // attributes definition (schema)
      {
        name: DataTypes.STRING,
        username: {
          type: DataTypes.STRING,
          allowNull: false,
          unique: true,
        },
        hashed_password: DataTypes.BLOB, // you can store it as char too
      },
      // options
      {
        sequelize, // Pass the database connection instance
        defaultScope: {
          attributes: {
            exclude: ["hashed_password"], // don't query password by default
          }
        },
        scopes: {
          withPassword: { attributes: {} }
        } }
    );
  }

  // Instance method
  async verify(password) {...}

  // Static functions
  static associate(models) {...} // relationship association

  static async login(username, password) {...}

  static async register(username, name, password) {...}

  // Convenient function to hash passwords
  static async hash(pw) {...}
}

module.exports = User;
```

Using Sequelize, a model can be created by extending the Model class and calling its `init` function to pass the schema definition and the database connection instance as seen in the code above. Our model above is simple, every user will have a unique username, a display name, and a password hash representation as **passwords should never be stored as plain text**.

In our model above we also put placeholder static functions to create, and login a user. We also have an instance method to verify a password is correct for login purposes. We will implement these functions next.

## User registration

To register a user is to create a `User` object in the database with the details required so that they can login, and we can track their actions by issuing them a unique identifier to relate to their data in the database.

To register, we can have an endpoint in our server, where they can send a request to register with the required data (username, and password). Below we will be defining a `POST` endpoint that takes the request parameters, and passes them to the register function in the model:

```js
// ./routes/auth.js
const express = require("express");
const router = express.Router();

const { User } = require("../db"); // as exported in the db file

// Define the /register end point
// The async callback function below can also be definer in a AuthController
router.post("/register", async (req, res) => {
  const { username, name, password } = req.body;

  // Create user
  User.register(username, name, password)
    .then((user) => {
      req.session.user = user; // save the user to the session
      res.status(201).redirect("/dashboard"); // redirect them to the dashboard
    })
    .catch((error) => {
      // User creation error would be thrown and caught here
      res.status(400).render("register", {
        error: error.message,
        username,
        name,
      });
    });
});

module.exports = router;
```

What's left is to define the register function in the User model

```js
// ./models/user.js
const { Model } = require("sequelize");
const bcrypt = require("bcrypt");

// to validate passwords: https://github.com/tarunbatra/password-validator
const passwordValidator = require('password-validator');

class User extends Model {
  ...
  static async register(username, name, password) {
    // check password strength, using a library
    const schema = new passwordValidator();
    schema
    .is().min(8)                                    // Minimum length 8
    .has().uppercase();                             // Must have uppercase letters
    // read more cases: https://github.com/tarunbatra/password-validator#rules

    const valid = schema.validate(password);
    if(!valid) {
      throw new Error("Password should include 1 uppercase letter and have 8 characters or more");
    }

    // check username exists
    const exists = await User.findOne({ where: { username } });
    if (exists) {
      throw new Error(`Username ${username} already exists.`);
    }

    // Hash the supplied password before saving to databse
    const hashed = await User.hash(password);
    // Save to databse
    const user = await User.create({
      username,
      name,
      hashed_password: hashed,
    });

    const { id, name, username } = user.get();

    // return the created user details to be saved to session
    return { id, name, username } ;
  }

  // Convenient function to hash passwords using bcrypt library
  static async hash(pw) {
    // saltRound is a factor to determine the cost of the salt
    // 10 is usually acceptable standard (default)
    // Read more: https://github.com/kelektiv/node.bcrypt.js#a-note-on-rounds
    const saltRounds = 10;
    return await bcrypt.hash(pw, saltRounds);
  }
}

module.exports = User;
```

Usually, the registration logic is inside a controller, but it can also sit with the model for encapsulation. Here it was defined in the model with very simple validation.

If any email or phone number validation is required, it is usually in this step as well. Your app can save the user, and queue a job to send a validation email to the user's email address. We can get into more details about that process later.

One thing to emphasize in the code above is the introduction of hashing function. BCrypt was used to salt and **hash the password before saving in the database**. Some password validation was also used to make sure any password we store in the database is strong enough against brute-force and rainbow-table attacks.

### Password management

Let's imagine this, we have 2 users Bob and Alice. They are using a form to register and out of coincidence they use the same password `c00k1eD0ugh`. Your app would hash this password before storing, and hash functions when given the same input, they always return the same hash. It is due to the deterministic nature of hashing functions. Your table would look like this:

| id  | name  | hashed_password                                                    |
| --- | ----- | ------------------------------------------------------------------ |
| 1   | Bob   | `695ddccd984217fe8d79858dc485b67d66489145afa78e8b27c1451b27cc7a2b` |
| 2   | Jane  | `73fb51a0c9be7d988355706b18374e775b18707a8a03f7a61198eefc64b409e8` |
| 3   | Alice | `695ddccd984217fe8d79858dc485b67d66489145afa78e8b27c1451b27cc7a2b` |

Now imagine an attacker breached your database and got a hold of this table and start studying it. Once they see a duplicate hash, they can determine that your app:

- is not using salt for passwords,
- and it is using a weak hashing algorithm because most suitable algorithms come with salting in-built
- or it can be that you are using a default password when registering users, and not enforcing them to update it

After these insights, the attacker can start with [dictionary-attack](https://en.wikipedia.org/wiki/Dictionary_attack). It is an attack that uses pre-computed hashes for common words, like words in the dictionary or previously used passwords that are harvested from another breach.
Fortunately, though, for Alice and Bob, while using the same password, it is not as common to find in a dictionary attack. Not like Jane for instance who used `Chocolate` as her password which is a direct entry in the English dictionary.

> 💡 A dictionary attack would usually contain lowercased, uppercased, and capitalized first letter hash versions for each entry.

Thus, Jane is at high risk of being breached through a dictionary attack. Alice and Bob are not so different, it might take some more time, but with some tools that can replace letters with similar characters like numbers or special characters. And once cracked, the attacker will have 2 user accounts simultaneously.

### Mitigating the damage with salts

To mitigate the damage introduced by this user vulnerability, we salt the passwords. A **salt** is a value generated by a [cryptographically secure function](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html) that is added to the input of hash functions to create unique hashes for every input, regardless of the input not being unique. Salt makes a hash function look non-deterministic, which is good as we don't want to reveal duplicate passwords through our hashing.

Let's take the example above and add salting to it. When Alice is registering, she sent her password to the server to create an account. The server would generate a random salt `d6%648SAw9` upon registration. Then this salt is either appended or prepended to the password. The password to be hashed would be `d6%648SAw9c00k1eD0ugh`. When Bob registers, a new random salt would be generated, and his password to be hashed will become `F32JsS9TuAc00k1eD0ugh`.

| id  | name  | hashed_password                                              | salt         |
| --- | ----- | ------------------------------------------------------------ | ------------ |
| 1   | Bob   | `11c150eb6c1b776f390be60a0aa2f8c0a0ce766ed92fea5bfd9313c8f6` | `F32JsS9TuA` |
| 2   | Jane  | `07dbb6e6832da0841dd79701200f1a94a7b3dd26f612817f3c03117434` | `U93gH32!AO` |
| 3   | Alice | `7528ed35c6ebf7e4661a02fd98ab884e48a4b27338fcc194b90ae8855c` | `d6%648SAw9` |

The hashes for these two salted passwords will be entirely different, and when stored in the database, **we will need to store the salt too**. So that when they login we can retrieve it and prepend it to their supplied password. This way, the attacker will never know that they are using the same password when studying the hashes even if they know the salt. And their attack will take greater time adjusting for the introduction of salts. The same can be said for Jane, even though she is using a dictionary word, the hash will be for a different sequence of letters, and the hash table won't match it.

### BCrypt

[BCrypt](https://en.wikipedia.org/wiki/Bcrypt) is a password hashing algorithm that is very hard to crack due to being super slow. It is adaptive and can be set up to be harder over time to provide more security by increasing the iteration count. It has an in-built feature to generate a salt when hashing so it won't need a salt column in the database.

```js
const bcrypt = require("bcrypt");
const plainPassword = "DFGh5546*%^__90";

const costFactor = 10; // aka: iteration count, salt rounds

bcrypt
  .genSalt(costFactor)
  .then((salt) => {
    console.log("Salt: ", salt);
    return bcrypt.hash(plainPassword, salt);
  })
  .then((hash) => {
    console.log("Hash: ", hash);
    // Store hash to database
  })
  .catch((err) => {
    console.log(err);
    // handle error
  });
```

running the code above in node (after installing [`bcrypt`](https://www.npmjs.com/package/bcrypt)) will output something similar to the log below:

```
Salt:  $2b$10$2vPfZJhvp0BKoq6/o8X5Vu
Hash:  $2b$10$2vPfZJhvp0BKoq6/o8X5Vu.qYoA.uwdgTtbMFttllhAtWl6Wc0rxW
```

and this is the breakdown of the segments of the hash output:

```
$2b$10$2vPfZJhvp0BKoq6/o8X5Vu.qYoA.uwdgTtbMFttllhAtWl6Wc0rxW
\__/\/ \____________________/\_____________________________/
Alg Cost      Salt                        Hash
```

As you see, all the parameters needed to verify a password are embedded into the hash itself.

In the next section, you will learn how to use `bcrypt` to verify passwords as well.

## User login

When a user registers, we persist their access usually for some time. But once the credentials expire, they need to login again. Below we will expose a `POST` endpoint as well, to send a login request.

```js
// ./routes/auth.js
...

// Define the /login end point
// The async callback function below can also be definer in a AuthController
router.post("/login", async (req, res) => {
  const { username, password } = req.body.username;

  const user = await User.login(username, password);

  if (user) {
    req.session.user = user; // store the user to a session
    res.redirect('/dashboard');
  } else {
    res
      .status(400)
      .render("login", { error: "Invalid username or password", username });
  }
});

...
```

Finally, we define the login function in the model

```js
// ./models/user.js
...

class User extends Model {
  ...

  // instance method
  async verify(password) {
    // read this user instance hashed_password
    const hashed = this.hashed_password.toString();

    // time-safe comparison function
    const result = await bcrypt.compare(password, hashed);
    return result; // true if equal, false otherwise
  }

  // class function
  static async login(username, password) {

    // attempt to find a user in the database with given username
    // Rememeber to use the withPassword scope so we query the password
    const user = await User.scope('withPassword').findOne({
      where: {
        username,
      },
    });

    if (user) {
      // username exists. Check password
      const verified = await user.verify(password);
      if (verified) {
        const { id, name, username } = user.get();
        // return the user details to be saved to session
        return { id, name, username } ;
      } else {
        return false; // Incorrect password
      }
    }

    return false; // invalid username
  }
  ...
}

...
```

What we did above, is taken a username and password, we search for the user record using the username. If no record for that username was found, we return false, which means user credentials are incorrect. Otherwise, we do a time-safe comparison between the given password and saved hash. If they are equal, we return the user details, which means credentials were valid. If not, we return false as well indicating an incorrect username or password.

The comparison between passwords here is also done using bcrypt library. It is a time-safe algorithm that takes the supplied password, hash it, then compares it with hash in the database in an invariable time approach. Read more about [timing-attack](https://codahale.com/a-lesson-in-timing-attacks/).

## Restricting access to the dashboard

Now that we have our user creation and login logic, we can prevent access to resources, and endpoints by ensuring that the request is authenticated. This means it has the correct authentic user object that is authorized to access that resource.

In the above examples, we assumed having a `/dashboard` endpoint that we were redirecting the user to when a login or registration was successful. Below, we will define simple logic that prevents unauthenticated requests to see the dashboard.

```js
// ./routes/dashboard.js
const express = require("express");
const router = express.Router();

const { Todo } = require("../db");

router.get("/dashboard", async (req, res) => {
  // check our session contains a user object
  const user = req.session.user;
  if (user) {
    // the request is authentic. We have a logged in user

    // contact database, collect the required data for dashboard
    // Assuming we have Todo list
    const todos = await Todo.findAll({
      where: {
        user_id: user.id,
      },
    });

    res.render("dashboard", { user, todos });
  } else {
    // user have not logged in, redirect to login page
    res.status(401).redirect("/login");
  }
});

module.exports = router;
```

In the code above, we have used session persistence to ensure a user is logged in. In addition, we have also assumed we have a `Todos` table in our database that has has `Todo` records related to a `User` by `user_id`. Having our user in the session, enabled querying the related todos.

What you've seen here is a simple authentication guard that ensured unauthenticated requests won't be able to see the dashboard and they would be redirected to a login page. However, in an app where you have lots of such endpoints, you won't actually have that `if-else` statement in the controller. Instead, you would be implementing an authentication guard (aka middleware) the do the validation automatically for any route that needs authentication.

## Defining routes that need authentication

As we've explored in the intro lesson, most resources in our app need to be guarded for reasons of privacy, personalization, and tracking. We will assume next we have an Express.js based Todo Application.

This is a list of our endpoints:

| endpoint      | HTTP verbs           | usage                                                                                                                                                  |
| ------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `/`           | `GET`                | A landing page when a user isn't logged in, otherwise a home page for users to show a summary of their completion rate, and the user's priority todos. |
| `/login`      | `GET` `POST`         | Navigate to login page, and POST login credentials.                                                                                                    |
| `/register`   | `GET` `POST`         | Navigate to account creation page, and POST registration data.                                                                                         |
| `/about`      | `GET`                | Navigate to the about page of the app                                                                                                                  |
| `/todos`      | `GET` `POST`         | List all todos, and create a new todo item                                                                                                             |
| `/todos/[id]` | `GET` `PUT` `DELETE` | Read a single todo item, update, and delete it                                                                                                         |
| `/account`    | `GET` `PUT`          | Navigate to user account page, and update it                                                                                                           |

It is clear that not all of these routes need guarding. In the `TodosController`, we need to completely block access to `GET` `POST` `PUT` `DELETE` for unauthorized and unauthenticated requests. The same goes for the `AccountController` as that endpoint would get data for a specific user, so it shouldn't be accessible for everyone.

However, the `AuthController` doesn't need to be guarded, because we want these endpoints to be accessible to anyone so that they can either login or create an account.

As for the home page `/`, it needs to have 2 different views, for both authenticated and unauthenticated requests. The about page shouldn't be guarded usually.

## Authentication and Authorization

Authentication means that to access this resource, a request needs to contain credentials (verified identity) because it doesn't make sense for an anonymous request to read that resource.

Authorization on the other hand means that even if a request has a valid credential, to access a resource, we need to make sure that it is for that intended user making the request.
If we assume having a Todo with an id 32, that belongs to user `A`, if a request is coming from user `B` for `/todos/32` we need to block it because user `B` _isn't authorized_ to read resources not belonging to them.

## Conclusion

In this lesson, we explored how to define a user schema and model, how to create and login a user, and how to guard an endpoint against unauthenticated requests. The takeaways from this lesson are:

- Always hash passwords before saving them to the database
- Enforce passwords validation and strength schema
- Use libraries like `bcrypt` to salt, hash and compare passwords
- Ensure to guard your protected routes against unauthenticated requests

In the next lessons, we will learn more about session storage, cookies, middlewares, and security practices.
