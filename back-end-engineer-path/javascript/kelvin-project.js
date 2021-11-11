const kelvin = 293;
//The temperature in Kelvin is 293;
const celcius = kelvin - 273;
//The temparature in Cecius is 20;
let fahrenheit = celcius * (9 / 5) + 32;
//Fahrenheit is outdated and kind of bad unless measuring relative to humans
fahrenheit = Math.floor(fahrenheit);
//fahrenheit should be rounded down
let newton = celcius * (33 / 100);
//newton is another measurement
newton = Math.floor(newton);
console.log(`The tempurature is ${fahrenheit} degrees Fahrenheit`);
console.log(`The tempurature is ${newton} degrees newton`)
