const express = require('express');
const app = express();

const { quotes } = require('./data');
const { getRandomElement } = require('./utils');

const PORT = process.env.PORT || 4001;

app.use(express.static('public'));

// setup get /api/quotes/random route
app.get('/api/quotes/random', (req, res, next) => {
  res.send ({quote: getRandomElement(quotes)});
});

// setup get /api/quotes router
app.get('/api/quotes', (req, res, next) => {
  if(!req.query.person) {
    res.send({ quotes: quotes });
    return;
  }

  const personQuotes = quotes
    .filter(quote => quote.person === req.query.person);

  res.send({quotes: personQuotes});
});

// setup post /api/quotes route
app.post('/api/quotes', (req, res, next) => {
  if (!req.query.person || !req.query.quote) {
    res.status(400).send();
    return;
  }

  const newQuote = {
    quote: req.query.quote,
    person: req.query.person
  }

  quotes.push(newQuote);
  res.status(201).send({ quote: newQuote });
});

// setup port listening
app.listen(PORT, () => {
  console.log(`Server is listening on port: ${PORT}`);
});
