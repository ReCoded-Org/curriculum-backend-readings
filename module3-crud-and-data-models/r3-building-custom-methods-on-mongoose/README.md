# Custom model methods
So far we have seen the use of pre-existing model methods of the Mongoose ODM. What if we wanted to perform a custom model operation that is not available directly in the ODM? The objectives of this lesson are:
1. Getting familiar with other features of Mongoose ODM
2. Understanding the use of custom methods and virtual fields

## Custom method example
In Mongoose, instances of models are documents. Documents have many of their own built-in instance methods (called static methods). We have seen some of these method such as `find()`, `findById()`, `findByIdAndUodate()` and so on. You can see more query methods in the Mongoose documentation [here](https://mongoosejs.com/docs/queries.html).

If required, we may also define our own custom document instance methods. We use instance methods to add new custom methods to our model that didn't exist before, that will help us reduce code duplication specially if that method is required to be used in multiple places, thus improving the overall code structure.

For example:
```js
// define a schema
const animalSchema = new Schema({ name: String, type: String });

// assign a function to the "methods" object of our animalSchema
animalSchema.methods.findSimilarTypes = function (cb) {
  return mongoose.model("Animal").find({ type: this.type }, cb);
};
```

Now all of our `animal` instances have a `findSimilarTypes` method available to them.
```js
const Animal = mongoose.model("Animal", animalSchema);
const dog = new Animal({ type: "pet" });

dog.findSimilarTypes((err, dogs) => {
  console.log(dogs); // woof
});
```

## Virtual Fields
Another very useful feature of Mongoose is the concept of virtual fields. Virtual fields are fields that you can get and set like another document field, but these fields don't actually persist on the database. Usually these fields are used to prevent data duplication or storing data that might change over time depending on another field.

Let's take a look at fiew examples:
```js
const personSchema = new Schema({
    name: {
      first: String,
      last: String
    },
    dateOfBirth: Date
  });

  // compile our model
  const Person = mongoose.model("Person", personSchema);

  // create a document
  const axl = new Person({
    name: { first: "Axl", last: "Rose" },
    dateOfBirth: ISODate("1996-01-22T14:56:59.000Z")
  });
```

Let's say you want to get the full name and age of Axl or any other person. You can do this as:
```js
personSchema.virtual("fullName").get(function() {
  return this.name.first + " " + this.name.last;
});

personSchema.virtual("age").get(function() {
  return new Date() - this.dateOfBirth;
});
```

Let's say you received a request to update the full name, you can write a virtual setter function to update the first name and last name separately.
```js
personSchema.virtual("fullName").
  get(function() {
    return this.name.first + " " + this.name.last;
    }).
  set(function(v) {
    this.name.first = v.substr(0, v.indexOf(" "));
    this.name.last = v.substr(v.indexOf(" ") + 1);
  });

axl.fullName = "William Rose"; // Now `axl.name.first` is "William"
```

We will explore using these features in the next assignment. You can refer to the Mongoose documentation to learn about these and other features.

---
## References
- https://mongoosejs.com/docs/guide.html#methods
- https://mongoosejs.com/docs/guide.html#virtuals
