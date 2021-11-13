// Write your code here:
const shoutGreetings = arr => {
  let shoutArray = [];
  for (let i=0; i < arr.length; i++){
    shoutArray.push(arr[i].toUpperCase() + '!')
  }
  return shoutArray
}

// Feel free to uncomment out the code below to test your function!

const greetings = ['hello', 'hi', 'heya', 'oi', 'hey', 'yo'];

console.log(shoutGreetings(greetings))
// Should print [ 'HELLO!', 'HI!', 'HEYA!', 'OI!', 'HEY!', 'YO!' ]
