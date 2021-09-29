# Securing a backend app

So far, you've learned how to create server side applications and how to use databases to persist and manipulate the data using CRUD operations. All these features sound awesome, but as it stands currently, they come with a high vulnerability and security risk.

In this module, we will go over how we secure our app and how to make sure that neither intended nor unintended security breaches happen.

Follow me in the following journey to understand why we need security.

## Wishlist inventory app

You've created an amazing app to store a shopping wishlist for your users. You have endpoints that retrieve the list, add an item to the list, update an item in the list, and delete an item in the list.

I liked the app and started using it to create 2 lists for the things that I love, computers and kitchenware, and started adding items to both.

In your database, you have 2 tables that store these items as follows:

### Table 1: lists

| id  | name           |
| --- | -------------- |
| 1   | Computer Parts |
| 2   | Kitchenware    |

### Table 2: items

| id  | name                 | list_id | url                   | price | bought |
| --- | -------------------- | ------- | --------------------- | ----- | ------ |
| 1   | NVidia RTX 3070      | 1       | https://amzn.com/313  | $785  | false  |
| 2   | Philips Blender      | 2       | https://url.com/313   | $90   | false  |
| 3   | AMD Ryzen 9          | 1       | https://amzn.com/585  | $599  | true   |
| 4   | Tefal Iceforce knife | 2       | https://amzn.com/1311 | $20   | false  |

Now, suppose another user comes to your app: how will your app decide what to show them? When they land on the homepage, they would see my items because the code can't decide what to show. This is the first security risk. The app needs somehow to relate the data to a specific user, so it only queries data that belongs to the requesting user.

That's why almost everywhere online, you need to register or log in to an account in order to use an application, so the data can be related to you and you only.

## Let's add some security

To secure our wishlist above, we can add a new column to the lists table to attach it to an identity (a user). We can name that column `user_email` for example, and use this query to get the user wishlist:

```SQL
SELECT `id`, `name`, `user_email` from `lists`
INNER JOIN `items`
ON `items`.`list_id` = `lists`.`id`
WHERE `lists`.`user_email` = "test@domain.com"
```

Thus, when a user comes to your app, you can ask them first about their email address, and then query the database to get their lists. But that is also insufficient. A malicious user can peep on other users' wishlists if he/she knew their emails, or he/she check different email combinations to see if it lands a hit, aka, **brute force**.

To make this a bit harder to brute force, you can create a token system. Tokens are random strings of characters, usually with arbitrary length, that are intended to be hard to brute force (guess). A token can look something like this: `4f57ec27561d4524e6b5bb1f08fb7cccfb36a5e5` and is generated using special functions called _Cryptographically Secure Pseudo-Random Number Generator_ (CSPRNG). For example, you can run this code inside NodeJS to get a secure token using the `crypto` NodeJS library:


```js
const crypto = require('crypto');
const size = 20; // bytes (or 40 hex digits)

const token = crypto.randomBytes(size).toString('hex')
console.log(token); // example output: 5d4225087676cf60670144e37b1694355a2e24d2
```

You can change the column `user_email` to `token` and every time a user comes in, you can ask them for the token, or allow them to generate a token. If they are new users, they can generate a new token, and save it, then start creating their lists. When they visit again, they enter that token to get their lists back.

![Bingo!](https://media.giphy.com/media/W5dBnWmcGDABi/giphy.gif)

Bingo! You've just created your first, very adequate authentication layer! You've secured your app and **slimmed the chances** of brute-forcing user data! Many apps today use this pattern to secure data. However, keep in mind that you usually need other features to track, like user email, name, age, etc. So such a simplistic approach wouldn't suffice. That's when this token is moved into another table and tracked with a `user_id` instead.

## Why do we need passwords

The token system developed above is very robust, but it isn't always an acceptable security measure (at least not alone). That's because, if a user loses the token, it is next to impossible (especially if it was generated with CSPRNGs with reasonable size) to gain access back to their lists using today's technologies.

So, maybe instead of a long random token, use a password? We can ask the user when they land on our page for a passcode (aka password). And we check the database if we can find a list where `password = USER_SUBMITTED_PASSCODE` then display them. If not, that means they are a new user.

Indeed this works, passwords are okay and a perfectly viable and widespread approach. Keeping in mind that users tend to use easy to remember words, dates, phone numbers, and the like. This makes passwords vulnerable to brute-force attacks. It would be relatively harder than brute-forcing emails, but still easy to guess, and very easy for computers to break by checking every possible combination of words, dates, numbers, and even relatively harder passwords using a technology called **rainbow tables**.

Hence, there are two things to remember about passwords:
They require validation to prevent brute force attacks (thus preventing easy to guess passwords)
Use salt and hash to prevent rainbow attacks -- point to a code example here or include your own, and then this needs an in-depth explanation because this is probably the most important section that new people will forget about writing passwords
 
## Security Checklist

### Storing Passwords
**Never** save the password as plain text in a database. Always use industry-standard cryptographic algorithms like bcrypt to hash and salt passwords. More on that later.

### Password Policy
You need to implement and **enforce** a password validation policy. It can contain:
- The minimum acceptable combination of characters (lowercase, uppercase, special characters) in a password
- Minimum length
- Expiry dates (if necessary)

### Use Federated Identity Management
Federated identity management is a configuration that can be made between two or more trusted domains to allow consumers of those domains to access applications and services using the same digital identity. Such identity is known as federated identity, and the use of such a solution pattern is known as identity federation.
An example of this is to offer people to sign in with Google, or Github. Here, Google is an identity provider (IdP).

Many benefits come with this:
User convenience, they don't have to remember lots of passwords and fill preliminary registration forms.
Delegate account and password management overhead to the identity provider.
Sometimes, you can even skip email validation logic since that has been already done.
Avoid privacy compliance burden.
There are three protocols for federated identity:
SAML
OpenID
OAuth
We will cover OID and OAuth later in this module.

### Database security
You need to ensure basic isolation of your database servers, use firewalls to limit access, protect and encrypt backups, and opt-in for database as service (DBaaS) providers when possible. 

### API Throttling (Rate Limiting)
This is a wide subject too and it can be applied to different elements of security. It can protect your server from some types of DDoS and DoS attacks, as well as thwarts brute-forcing attempts to break through your security. You can also limit how many login attempts are allowed, and then block attempts for a pre-defined cool-off period.

### Secure HTTP (HTTPS)
As you've known know, HTTP is a protocol to exchange messages between a client and server. And since all your messages will go through the network connection (a wire), an attacker anywhere on the network can sniff (listen to) all your messages, including passwords, tokens, etc. en route.
To make these messages obscure (or gibberish), you need to encrypt them using encryption technology. That's when the protocol is upgraded to SECURE status.

The process is usually done by obtaining a certificate from a Certificate Authority (CA) that issues the digital identity for the browsers to trust. The certificate contains a private key that is used by the server to encrypt and decrypt the messages.

### Test your code
Testing the code correctly to ensure it achieves its intended purpose around normal and abnormal scenarios. 

For instance, if you define an endpoint is only intended for admins, you need to test that it:
Rejects gracefully any request from non-admin users
Rejects requests from unauthenticated clients
When if a token has expired, it redirects the request correctly
These are some examples of test cases. You need to account for edge cases in your logic as well.

### Update your code and libraries
Cyberattacks evolve, as well as the tools to carry them out. A library used today can be broken tomorrow. You need to ensure that you always update your libraries and apply the necessary patches to your code so it follows up-to-date security practices and guides.

Cybersecurity is an unattainable quest, so we will never be 100% secure. We just aspire to be as close as possible to that.

## Module overview

In this module, we will cover best practices to establish and implement most of the tips shared above. We will focus on current industry standards and libraries to ensure our built web apps are running with the best security practices available. We will also explore authorization and validation as means to security and data integrity.
