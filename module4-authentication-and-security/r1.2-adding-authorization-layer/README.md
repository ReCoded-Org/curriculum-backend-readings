# Adding authorization layer

With authorization, we introduce another level of app security. In this lesson, we will learn how to restrict some users from accessing certain routes of our app. The lesson objectives are:

- Define what is Authorization, and how is it different from Authentication
- Introduce role-based authorization
- How to restrict access to routes using authorization

## Authorization

- Authorization is a process by which a server determines if the client has permission to use a resource or access a file.
- Authorization is usually coupled with authentication so that the server has some concept of who the client is that is requesting access.
- The type of authentication required for authorization may vary; passwords may be required in some cases but not in others.
- In some cases, there is no authorization; any user may use a resource or access a file simply by asking for it. Most of the web pages on the Internet require no authentication or authorization.

## Authentication

- Authentication is used by a server when the server needs to know exactly who is accessing their information or site.
- Authentication is used by a client when the client needs to know that the server is the system it claims to be.
- In authentication, the user or computer has to prove its identity to the server or client.
- Usually, authentication by a server entails the use of a user name and password. Other ways to authenticate can be through cards, retina scans, voice recognition, and fingerprints.
- Authentication by a client usually involves the server giving a certificate to the client in which a trusted third party such as Verisign or Thawte states that the server belongs to the entity (such as a bank) that the client expects it to. This is required to initiate secure communication (HTTPs) between client and server.
- Authentication does not determine what tasks the individual can do or what files the individual can see (aka scopes). Authentication merely identifies and verifies who the person or system is.

## **Role-based authorization**

By role-based authorization, we assign a role or roles to the user either when we register them, or by some other mechanism that happens later to elevate a user access level.

In simple terms, we assign an attribute to the User model, that would tell us later when he/she signs in, what is their access level, or role. Based on that, our app can determine whether they can access that resource/endpoint.

Let's assume we have a vlog web app. We have 3 access levels:

- An anonymous user can watch videos and search on the website without signing up.
- To upload videos or flag content, the user needs to create an account.
- Our app needs moderators as well, who are users that can delete videos in case they violate the usage agreement, or are inappropriate.
- And finally, our app needs admins, who have the ability to make moderators by elevating other users to a moderator access level.

From these requirements, we can distinguish our app structure as follows:

- Some endpoints wouldn't have any authentication guard, any request can reach them. Which are endpoints to read a list of videos, watch a specific video, or search for videos.
- Certain endpoints like `/upload` and `/flag` will need an authentication guard. This is to check if we have a JWT in the request or a `user` in the session. If there isn't, they shouldn't be able to reach that resource.
- Endpoints like `/delete` would need an authorization guard. Which is a guard that contains the authentication guard, plus it also checks if the user is a `moderator`, before letting them complete the action. Otherwise, it shouldn't let them through.
- To elevate a user, an endpoint like `/elevate` would have the same authorization guard, but instead it will check if the user is an `admin`.

### Implementation

To implement this as simply as possible, we need to first define our roles as numbers. That is mainly to:

- avoid hardcoded strings in our database,
- it offers better scalability when our app grows and,
- is easier to search and add more roles in the future

hence, we can define our roles like this:

- User: Role 1 (_default_)
- Moderator: Role 2
- Admin: Role 3

Then we need to add a new attribute `role_id` to our User model schema:

```js
// ./models/user.js
const ROLES = {
  USER: 1,
  MODERATOR: 2,
  ADMIN: 3
}

// attributes definition (schema)
const schema = {
  name: DataTypes.STRING,
  username: {
    type: DataTypes.STRING,
    allowNull: false,
    unique: true,
  },
  hashed_password: DataTypes.BLOB, // you can store it as char too
  role_id: {
    type: DataTypes.INTEGER, // As we will identify it by numbers
    allowNull: false, // it shouldn't be null
    defaultValue: ROLES.USER, // defaults to 1
  }
},
```

With this setup, the registration logic can stay as seen in the previous lesson. Whenever a new user registers, they will by default gain a `role_id: 1` which is for normal users.

> 💡 **TIP:** When you have role-based authorization with this setup, your app needs to start with at least one user seed that has an `admin` access level, usually called the app master. This is to prevent getting locked out of the app.

Then we need to add 2 instance methods to the `User` class: `isAdmin` and `isModerator`:

```js
// ./models/user.js

const ROLES = {
  USER: 1,
  MODERATOR: 2,
  ADMIN: 3
}

class User extends Model {
  static roles = ROLES; // to be able to access them else where
  ...

  // instance method
  async verify(password) {
    ...
  }

  isAdmin() {
    return this.role_id === ROLES.ADMIN;
  }

  isModerator() {
    return this.role_id === ROLES.MODERATOR;
  }

  ...
}
```

> ⚠️ **Warning:** Roles were defined as a JavaScript Object in the file above which isn't a best practice. Usually, they are hardcoded in the database with a `Role` model to prevent accidental tampering with roles. Or they are exported from another file that is well guarded against writing using UNIX `chmod` and `chown`.

The final change we need to do is to pass the user role when he/she logs in or registers. As seen in the previous lesson, the functions `login` and `register` returns `{ id, name, username }`. We need to add 2 more attributes to that:

```js
// ./models/user.js

class User extends Model {
  ...

  static async register(username, name, password) {
    ...
    return {
      id,
      name,
      username,
      isAdmin: user.isAdmin(),
      isModerator: user.isModerator()
    }
  }

  static async login(username, password) {
    ...
    return {
      id,
      name,
      username,
      isAdmin: user.isAdmin(),
      isModerator: user.isModerator()
    }
  }

  ...
}
```

With this, our session or JWT will hold these claims. In our authorization guard we can simply check if `user && user.isAdmin` or `user && user.isModerator` and either let them carry out the action or not as follows:

```js
// ./routes/role.js
const express = require("express");
const router = express.Router();
const { User } = require("../db"); // as exported in the db file

router.post("/elevate", async (req, res) => {
  const user = req.session.user;

  // Check if the user has signed in, and is admin
  if (user && user.isAdmin) {
    const { subject_id, role_id } = req.body;

    // check role_id is correct
    const roles = Object.values(User.roles);
    if (!roles.includes(parseInt(role_id, 10))) {
      res.status(400).json({
        error: `role_id is incorrect. Accepted values are: ${roles.join(", ")}`,
      });
      return; // exit
    }

    // check subject to be elevated exists
    // we will query users with defaultScope to exclude password
    const subject = await User.findByPk(subject_id);

    if (!subject) {
      res.status(400).json({
        error: `User with id: ${subject_id} cannot be found.`,
      });
    } else {
      subject.role_id = parseInt(role_id, 10);
      await subject.save(); // save dirty instance to database
      res.status(202).json({ status: "OK" });
    }
  } else {
    // user is not logged in, and not admin
    res.status(401).json({
      error: `Unauthorized`,
    });
  }
});
```

With this, we've guarded our `/elevate` endpoint against non-admin and non-authenticated access. The same can be applied for other, moderators only, endpoints by checking:

```js
if (user && (user.isAdmin || user.isModerator)) {
  // carry out the action
}
```

There is still a problem with our code though. It is very messy with lots of if-else and we can introduce a bug very easily by not returning or badly structures if-else clauses.

In the next lesson, we will introduce an easier way to enforce our guards using a feature called **middleware**. We can define an `onlyAdmins`, `onlyModerators`, and `onlyAuthenticated` middleware that would stop unauthorized requests, and only let authorized access through.

## Conclusion

In this lesson, we introduced authorization as a new security feature to our app. It would prevent users without the required access level from entering protected endpoints.

Keep in mind that you're not limited to the approach we took above. With backend web development, your options are limitless. We merely took one of the simplest approaches.

For more sophisticated applications with many features, each part of the app can be called a scope, and authorization would be scope-based, not role-based. However, that's a topic for another lesson.
