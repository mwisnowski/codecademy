const _ = {

  clamp(number, lower, upper){
    var lowerClampedValue = Math.max(number, lower);
    var clampedValue = Math.min(lowerClampedValue, upper);
    return clampedValue;
  },
  inRange(number, start, end){
    if(end === undefined){
      end = start
      start = 0
    }
    if(start > end){
      var temp = end
      end = start
      start = temp
    }
    var isInRange = start <= number && number < end
    return isInRange
  },
  words(string){
    var words = string.split(' ')
    return words
  },
  pad(string, length){
    if(string.length >= length) {
      return string;
    };
    const startPaddingLength = Math.floor((length - string.length) / 2);
    const endPaddingLength = length - string.length - startPaddingLength;
    const paddedString =' '.repeat(startPaddingLength) + string + ' '.repeat(endPaddingLength);
    return paddedString;
  },
  has(object, key) {
    const hasValue = object[key];
    if (hasValue != undefined) {
      return true;
    } return false;
  },
  invert (object) {
    let invertedObject = {};
    let originalValue;
    for (let key in object) {
      originalValue = object[key];
      invertedObject[originalValue] = key;
    }
    return invertedObject;
  },
  findKey (object, predicate) {
    for (let key in object){
      let value = object[key];
      let predicateReturnValue = predicate(value);
      if(predicateReturnValue){
        return key;
      };
      undefined
      return undefined;
    }
  },
  drop (array, n) {
    if(n === undefined) {
      n = 1;
    }
    var droppedArray = array.slice(n);
    return droppedArray;
  },
  dropWhile (array,predicate) {
    const cb = (element, index) => {
      return !predicate(element, index, array);
    }
    var dropNumber = array.findIndex(cb)
    var droppedArray = this.drop(array, dropNumber);
    return droppedArray;
  },

};




// Do not write or modify code below this line.
module.exports = _;
