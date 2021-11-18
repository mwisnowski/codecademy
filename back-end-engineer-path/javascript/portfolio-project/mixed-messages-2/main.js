// Create array of genres (12 options total)
const songGenre = [
  'Rock',
  'Pop',
  'Metal',
  'Jazz',
  'Punk',
  'Electronic',
  'Country',
  'Blues',
  'Hip Hop',
  'R&B',
  'Folk'
];

// Create array of keys (12 options total)
const songKey = [
  'Ab',
  'A',
  'A#',
  'Bb',
  'B',
  'C',
  'C#',
  'Db',
  'D',
  'D#',
  'Eb',
  'E',
  'F',
  'F#',
  'Gb',
  'G',
  'G#'
];
// test songKey array list
//console.log(songKey.join('\n'));

// create array of totally true and not at all fictitious facts (17 choices)
const majorMinor = [
  '',
  ' minor'
];

// test major/minor array list
//console.log(majorMinor.join('\n'));

//create array of music modes

const chordArray = [
  'II',
  'ii',
  'III',
  'iii',
  'IV',
  'iv',
  'V',
  'v',
  'VI',
  'vi',
  'VII',
  'vii'
];

// test mode array list
// console.log(chordArray.join('\n'));

//decide if seventh chord
const isSeven = [
  '',
  '7'
];

// test seven chord
//console.log(sevenChordArray.join('\n'));


// create array of tempos between 90 and 180 at increments of 3
const tempo = [];

for (var i = 90; i <= 180; i += 3) {
   tempo.push(i);
};

const timeFlux = [
  'Let\'s make this one standard time',
  'Let\'s speed things up and give it a double time feel!',
  'Let\'s slow it down and give it a double time feel.'
]

// test year array function
//console.log(tempo.join('\n'));

// actual function start

function makeAnRNGSong() {
  //create random number from input array
  function rng(array) {
    return Math.floor(Math.random() * array.length);
  };
  //setup rng indexes
  let genre = songGenre[rng(songGenre)];
  let key = songKey[rng(songKey)];
  let majMin = majorMinor[rng(majorMinor)];
  let chordOne = [];
    if (majMin === ' minor') {
      chordOne.push('i');
    } else {
      chordOne.push('I');
    };
  let chordTwo = [chordArray[rng(chordArray)]];
  /*let chordTwo = [] {
    let chordOne = [];
      if (majMin === 'minor') {
        chordOne.push('i');
      } else {
        chordOne.push('I');
      };
      if
  }*/
  let chordThree = [chordArray[rng(chordArray)]];
  let chordFour = [chordArray[rng(chordArray)]];

  //check to try and make no two chords the same
  if (chordTwo.toLowerCase != chordThree.toLowerCase) {
    return
  } else {
    chordTwo = [];
    chordTwo.push(chordArray[rng(chordArray)]);
  };
  if (chordTwo.toLowerCase != chordFour.toLowerCase) {
    return
  } else {
    chordTwo = [];
    chordTwo.push(chordArray[rng(chordArray)]);
  };
  if (chordThree.toLowerCase != chordFour.toLowerCase) {
    return
  } else {
    chordThree = [];
    chordThree.push(chordArray[rng(chordArray)]);
  }
  if (chordFour.toLowerCase != chordTwo.toLowerCase) {
    return
  } else {
    chordFour = [];
    chordFour.push(chordArray[rng(chordArray)]);
  }

  let seven = isSeven[rng(isSeven)];
  let speed = tempo[rng(tempo)];
  let timeFluct = timeFlux[rng(timeFlux)];

  //put the final string together
  let makeASong = `Let's make a ${genre} song in the key of ${key}${majMin}, with a tempo of ${speed} BPM.\n`
  + `We'll use the the following chords:\n`
  + `${chordOne}\n`
  + `${chordTwo}\n`
  + `${chordThree}${seven}\n`
  + `${chordFour}\n`
  + `${timeFluct}`;
  alert (`${makeASong}`);
};
