## Building Your Own Methods on Mongoose

In Mongoose, instances of Models are documents. Documents have many of their own built-in instance methods. We may also define our own custom document instance methods.

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
const dog = new Animal({ type: "dog" });

dog.findSimilarTypes((err, dogs) => {
  console.log(dogs); // woof
});
```

## Resources

- [instance methods in Mongoose](https://mongoosejs.com/docs/guide.html#methods)
