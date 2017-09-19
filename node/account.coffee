mongoose = require('mongoose');
Schema = mongoose.Schema;

blogSchema = new Schema({
  title:  String,
  author: String,
  body:   String,
  comments: [{ body: String, date: Date }],
  date: { type: Date, default: Date.now },
  hidden: Boolean,
  meta: {
    votes: Number,
    favs:  Number
  }
})

Blog = mongoose.model('Blog', blogSchema);

animalSchema = new Schema({ name: String, type: String });

# assign a function to the "methods" object of our animalSchema
animalSchema.methods.findSimilarTypes = (cb) ->
  return this.model('Animal').find({ type: this.type }, cb);

mongoose.connect('mongodb://localhost/test');

db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));

db.once('open', () ->
  # we're connected!
);


kittySchema = mongoose.Schema({
    name: String
});


kittySchema.methods.speak = ()->
  greeting = "hello"
  console.log(greeting);

Kitten = mongoose.model('Kitten', kittySchema);

silence = new Kitten({ name: 'Silence' });
console.log(silence.name);

silence.save((err)->
  if (err)
    return console.error(err);
  silence.speak();
);
