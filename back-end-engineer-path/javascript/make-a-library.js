// setup starting Media class
class Media {
  constructor(title, genre, releaseYear) {
    this._title = title;
    // add genre
    this._genre = genre;
    // add release year
    this._releaseYear = releaseYear
    this._isCheckedOut = false;
    this._ratings = [];
  }

  // set getters for title, isCheckedOut, and ratings
  // add flourishes to make output readable when logged
  get title() {
    return 'Title: ' + this._title;
  }
  //add genre
  get genre() {
    return 'Genre: ' + this._genre;
  }
  get isCheckedOut() {
    return 'This item is available: ' + this._isCheckedOut;
  }
  get ratings() {
    return this._ratings;
  }
  //added release year
  get releaseYear() {
    return 'Year of Release: ' + this._releaseYear;
  }

  // set checkout/checkin status
  set isCheckedOut(isCheckedIn) {
    this._isCheckedOut = isCheckedIn;
  }

  // toggle checked out status
  toggleCheckedOutStatus() {
    this._isCheckedOut = !this._isCheckedOut;
  }

  // get average rating from existing rating array by summing ratings and then dividing by array length
  getAverageRating() {
    let ratingSum = this._ratings.reduce((currentSum, rating) => currentSum + rating, 0);
    return 'Average Rating Score: ' + Math.floor(ratingSum / this._ratings.length)
  }

  // added check to make sure rating is between 1 and 5
  addRating(ratingValue) {
    if(ratingValue <= 5 && ratingValue >= 1){
      this._ratings.push(ratingValue);
    } else {
      console.log('Rating value must be between 1 and 5')
    }
  }
}

// setup book sub-class
class Book extends Media {
  constructor(author, title, genre, language, pages, releaseYear) {
    super(title, genre, releaseYear);
    this._author = author;
    // add language option
    this._language = language
    this._pages = pages;
  }
  //add flourishes to make logged output readable
  get author() {
    return 'Written By: ' + this._author;
  }
  //add language option
  get language() {
    return 'Available In: ' + this._language;
  }
  get pages() {
    return 'Page Count: ' + this._pages;
  }
}

// setup Movie sub-class
class Movie extends Media {
  constructor(director, movieCast, title, genre, runTime, releaseYear) {
    super(title, genre, releaseYear);
    this._director = director;
    this._movieCast = movieCast;
    this._runTime = runTime;
  }
  // added flourishes
  get director() {
    return 'Directed By: ' + this._director;
  }

  //added cast list
  get movieCast() {
    return 'Featuring: ' + this._movieCast
  }
  get runTime() {
    return 'Runtime: ' + this._runTime + ' minutes';
  }
}

//create CD sub-class
class CD extends Media {
  constructor(artist, title, genre, songs, producer, releaseYear) {
    super(title, genre, releaseYear);
    this._artist = artist;
    this._songs = songs;
    // added producer
    this._producer = producer;
  }
  // added flourishes
  get artist() {
    return  'Recording Artist: ' + this._artist;
  }
  get songs() {
    return 'Track List: ' + this._songs;
  }
  //added producer
  get producer() {
    return 'Produced By: ' + this._producer;
  }
  //added shuffle function
  shuffle() {
    return this._songs.sort(() => Math.random() - 0.5);
  }
}

//--------------Book instances--------------
// create new book instance
const historyOfEverything = new Book('Bill Bryson', 'A Short History of Nearly Everything', ['Popular Science', ' Non-Fiction'], 'English', 544, 2003);
historyOfEverything.toggleCheckedOutStatus();
//console.log(historyOfEverything.isCheckedOut);

// add ratings to historyOfEverything
console.log('Books:');
historyOfEverything.addRating(4);
historyOfEverything.addRating(5);
historyOfEverything.addRating(5);
console.log(historyOfEverything.title);
console.log(historyOfEverything.author);
console.log(historyOfEverything.genre);
console.log(historyOfEverything.language);
console.log(historyOfEverything.pages);
console.log(historyOfEverything.releaseYear);
console.log(historyOfEverything.isCheckedOut);
console.log(historyOfEverything.getAverageRating('rating'));

console.log('\nMovies:');
//--------------Movie instances--------------
// create new movie instance
const speed = new Movie('Jan de Bont', ['Keanu Reeves', 'Dennis Hopper', 'Sandra Bullock'], 'Speed', 'Action', 116, 1994);
speed.toggleCheckedOutStatus();
//console.log(speed.isCheckedOut);

// add ratings to speed
speed.addRating(1);
speed.addRating(1);
speed.addRating(5);
console.log(speed.title);
console.log(speed.director);
console.log('Featuring: ' + speed._movieCast.join(', '));
console.log('Genre: ' + speed._genre.join);
console.log(speed.runTime);
console.log(speed.releaseYear);
console.log(speed.isCheckedOut);
console.log(speed.getAverageRating('rating'));

console.log('\nCDs:');
//--------------CD instances--------------
const meliora = new CD('Ghost', 'Meliora', ['Heavy Metal', 'Hard Rock', 'Pop Rock', 'Psychedelic Rock'], ['Spirit', 'From the Pinnacle to the Pit', 'Cirice', 'Spoksonat', 'He Is', 'Mummy Dust', 'Majesty', 'Devil Church', 'Absolution', 'Deus in Absentia'], 'Klas Ahlund', 2015);
meliora.addRating(4);
meliora.addRating(5);
meliora.addRating(3);
console.log(meliora.title);
console.log(meliora.artist);
console.log('Genre: ' + meliora._genre.join(', '));
console.log('Track List: ' + meliora._songs.join(', '));
console.log(meliora.producer);
console.log(meliora.releaseYear);
console.log(meliora.isCheckedOut);
console.log(meliora.getAverageRating('rating'));

// test shuffle
console.log('\n');
console.log('Shuffle List: ' + meliora.shuffle().join(', '));
