// Create array of artists (14 options total)
const punkArtist = [
  'Green Day',
  'We Are the Union',
  'The Offspring',
  'Catbite',
  'Travis Barker (of The Aquabats)',
  'Beach Bunny',
  'VIAL',
  'Avril Lavigne',
  'Kill Lincoln',
  'Sum 41',
  'Goldfinger',
  'Millencolin',
  'Meet Me @ the Altar',
  'Paramore'
];
// test punkArtist array list
//console.log(punkArtist.join('\n'));

// create array of totally true and not at all fictitious facts (17 choices)
const facts = [
  'has been active since',
  'has been inactive since',
  'released a ska song in',
  'released a noise EP in',
  'released a post-hardcore, midwest-emo, farmer concept album in',
  'was headliner for Vans Warped Tour in',
  'was banned from Warped Tour in',
  'formed after playing Tony Hawk\'s Pro Skater in',
  'released their first single in',
  'won the Nickelodeon Kids\' Choice Award for Favorite Music Group in',
  'has been a guest artist on every Pop Punk single since',
  'released their most well-known song in',
  'sold out in',
  'sold their own bootleg merch until',
  'hasn\'t been allowed to perform in Seattle since',
  'performed on Saturday Night Live in',
  'didn\'t know they had a bassist until',
];

// test facts array list
//console.log(facts.join('\n'));

// create of years from 1984 - 2021 (37 total)
const year = [];

for (var i = 1984; i <= 2021; i++) {
   year.push(i);
};
// test year array function
//console.log(year.join('\n'));

// actual function start

function funFact() {
  //create random number from input array
  function rng(array) {
    return Math.floor(Math.random() * array.length);
  };
  //setup rng indexes
  let artist = punkArtist[rng(punkArtist)];
  let fact = facts[rng(facts)];
  let when = year[rng(year)];

  //put the final string together
  let factString = `${artist} ${fact} ${when}`;
  alert (`${factString}!`);
};
