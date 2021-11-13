let story = 'Last weekend, I took literally the most beautiful bike ride of my life. The route is called "The 9W to Nyack" and it actually stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it basically took me an entire day. I stopped at Riverbank State Park to take some extremely artsy photos. It was a short stop, though, because I had a really long way left to go. After a quick photo op at the very popular Little Red Lighthouse, I began my trek across the George Washington Bridge into New Jersey.  The GW is actually very long - 4,760 feet! I was already very tired by the time I got to the other side.  An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautiful park along the coast of the Hudson.  Something that was very surprising to me was that near the end of the route you actually cross back into New York! At this point, you are very close to the end.';


let overusedWords = ['really', 'very', 'basically'];

let unnecessaryWords = ['extremely', 'literally', 'actually' ];

let storyWords = story.split(' ');
console.log('============\nLet me tell you a story:\n\n' + storyWords.join(' ') + '\n');

// log original word count
console.log('============\nThe original story had ' + storyWords.length + ' words, but let\'s get rid of some unnecessary words.\n============\n');


// let's now get rid of some unnecessary words
let betterWords = storyWords.filter(word => !unnecessaryWords.includes(word));
console.log(betterWords.join(' ') + '\n' + '\n============\nThe story contains ' + betterWords.length + ' words after removing unnecessary words. Though there\'s still some overused ones in there.\n============\n');

//let's now get rid of the overused words and make not of how many times they appeared
console.log('Some facts about the story:\n')
overusedWords.forEach(function(overused) {
  let overusedCount = 0;
  betterWords.filter(function(storyWord) {
    if (overused === storyWord) {
      overusedCount++;
    }
  });
  if (overusedCount != 1) {
  console.log('The Word \"' + overused.toUpperCase() + '\" was used ' + overusedCount + ' times');
} else {
  console.log('The Word \"' + overused.toUpperCase() + '\" was used ' + overusedCount + ' time');
}
});

//let's check the sentence count for the story
let sentenceCount = 0;
betterWords.forEach(word => {
  if (word[word.length-1] === '.' || word[word.length-1] === '!') {
    sentenceCount++;
  }
});

console.log('There are ' + sentenceCount + ' sentences in the story.\n');

//removing and replacing the overused words
console.log('========================\n Let\'s clean this story up a bit by changing some overused words\n============\n');

//We'll start with the getting and storing a count of the  overused words
let overusedWordCount = overusedWords.map(function(){
  return 0;
});
let removedWordCount = 0;

//next, let's filter out every other instance of the overused words
let lessOverusedWords = betterWords.map(function(storyWord) {
  if (!overusedWords.includes(storyWord)) {
    return storyWord;
  } else {
    let pos = overusedWords.indexOf(storyWord);
    if (overusedWordCount[pos] < 1) {
      overusedWordCount[pos]++;
      return storyWord;
    } else { ///Add alternative word
      overusedWordCount[pos] = 0;
      removedWordCount++;
      ///Here we could pull from an array of alternative words
      return 'fairly';
     }
  }
});

console.log(lessOverusedWords.join(' ') + '\n')
console.log(removedWordCount + ' overused words were removed \n');

overusedWords.forEach(function(overused) {
  let overusedCount = 0;
  lessOverusedWords.filter(function(storyWord) {
    if (overused === storyWord) {
      overusedCount++;
    }
  });
  if (overusedCount != 1) {
  console.log('The Word \"' + overused.toUpperCase() + '\" is now used only ' + overusedCount + ' times\n');
} else {
  console.log('The Word \"' + overused.toUpperCase() + '\" is now used only ' + overusedCount + ' time\n');
}
});

//finding the most commonly used word
console.log('============\n Now, just for fun, let\'s tally up some of the most commonly used words\n============\n');
// we'll want to to remove puntuation and capitalisation so the contents can be parsed

// start with an array of accepted characters so we can filter out punctuation
const acceptedChars = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

// make everything lower case
let noCaps = story.toLowerCase();

// then create an array of individual characters
let noCapsChars = noCaps.split('');

/// which will allow us to filter out punctuation characters
let noPunctChars = noCapsChars.filter(char => acceptedChars.includes(char));

/// with no caps or punctuation, let's recreate the story
let noPunctStory = noPunctChars.join('');

// next let's replace double spaces with single spaces to eliminate blank entries in word arrays
let noPunctSentences = noPunctStory.split('  ');
let noDoubleSpaces = noPunctSentences.join(' ');

// and create an array of story words
let noPunctWords = noDoubleSpaces.split(' ');

// to then create an array of individual words
let noDupes = [];
noPunctWords.forEach(function(word) {
  if (!noDupes.includes(word)) {
    noDupes.push(word);
  }
});

// With the words indivualized, we can then get a count
let instanceCount =[];
noDupes.forEach(function(countWord) {
  let count = 0;
  noPunctWords.forEach(function(storyWord) {
    if (countWord === storyWord) {
      count++;
    }
  });
  // create a 2D array to store each word and its count
  instanceCount.push([count, countWord]);
});

// then let's sort the array by decending word count
instanceCount.sort(function(a, b) {
  return b[0] - a[0];
});

/// and now, we have the words used at least 6 times
console.log('Words used at least 6 times:\n'.toUpperCase())
for (let i = 0; instanceCount[i][0] > 6; i++) {
  console.log('The word \"' + instanceCount[i][1].toUpperCase() + '\" was used ' + instanceCount[i][0] + ' times')
}
