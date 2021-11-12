let input = "My name is Matt, and I hope this sentence has a lot of vowels!";
const vowels = ['a', 'e', 'i', 'o', 'u'];
const resultArray = [];

for (let i = 0; i < input.length; i++) {
  for (let j = 0; j < vowels.length; j++) {

    if(input[i] === vowels[j]) {
      if(input[i] === 'e') {
        resultArray.push('ee');
      } else if(input[i] === 'u') {
        resultArray.push('uu');
      } else {
        resultArray.push(input[i]);
      }
    }
  }
}
console.log(resultArray.join('').toUpperCase());
