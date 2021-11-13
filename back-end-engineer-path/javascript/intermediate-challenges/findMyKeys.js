// Write your code here:

function findMyKeys(arr) {
  let index = 0;
  for ( let i= 0; i < arr.length; i++) {
    if (arr[i] === 'keys') {
      index = i
      break
    }
  }
  return index
}

// Feel free to comment out the code below to test your function

const randomStuff = ['credit card', 'screwdriver', 'receipt', 'gum', 'keys', 'used gum', 'plastic spoon'];

console.log(findMyKeys(randomStuff))
// Should print 4
