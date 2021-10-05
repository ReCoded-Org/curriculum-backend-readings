# Building Your Own Methods on Mongoose

In Mongoose, instances of models are documents. Documents have many of their own built-in instance methods (called static methods). We may also define our own custom document instance methods.
We use instance methods to add new custom methods to our model that didn't exist before, that will help us reduce our code duplications if that method is used in multiple places, and, imporove the overall code structure.

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

---

## References

- https://mongoosejs.com/docs/guide.html#methods
