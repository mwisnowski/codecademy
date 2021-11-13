// Write your code here:
let arr1 = ['this', 'not this', 'nor this'];
let arr2 = ['thing 1', 'thing 2', 'this'];

const justCoolStuff = (arr1, arr2) => arr1.filter(item => arr2.includes(item));
 console.log(justCoolStuff(arr1, arr2));

// Feel free to uncomment the code below to test your function

const coolStuff = ['gameboys', 'skateboards', 'backwards hats', 'fruit-by-the-foot', 'pogs', 'my room', 'temporary tattoos'];

const myStuff = [ 'rules', 'fruit-by-the-foot', 'wedgies', 'sweaters', 'skateboards', 'family-night', 'my room', 'braces', 'the information superhighway'];

console.log(justCoolStuff(myStuff, coolStuff))
// Should print [ 'fruit-by-the-foot', 'skateboards', 'my room' ]
