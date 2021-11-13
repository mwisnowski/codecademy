// Write your code here:
function isTheDinnerVegan(arr) {
  const isVegan = (food) => {
    if (food.source === 'plant') {
      return true;
    } else {
      return false;
    }
  }
    for ( let i =0; i < arr.length; i++) {
      if (!isVegan(arr[1])){
        return false;
      }
    }
    return true
}







// Feel free to comment out the code below to test your function

const dinner = [{name: 'hamburger', source: 'meat'}, {name: 'cheese', source: 'dairy'}, {name: 'ketchup', source:'plant'}, {name: 'bun', source: 'plant'}, {name: 'dessert twinkies', source:'unknown'}];

console.log(isTheDinnerVegan(dinner))
// Should print false
