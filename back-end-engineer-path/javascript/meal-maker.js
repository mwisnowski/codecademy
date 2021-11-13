const menu = {
  _courses: {
    appetizers:[],
    mains:[],
    desserts:[],
  },
  get appetizers() {
    return this._courses.appetizers;
  },
   get mains() {
    return this._courses.mains;
  },
   get desserts() {
    return this._courses.desserts;
  },
  set appetizers(appetizers) {
  this._courses.appetizers = appetizers;
  },
  set mains(mains) {
  this._courses.mains = mains;
  },
  set desserts(desserts) {
  this._courses.desserts = desserts;
  },
  get courses() {
    return {
      appetizers: this.appetizers,
      mains: this.mains,
      desserts: this.desserts,
    };
  },
  addDishToCourse(courseName, dishName, dishPrice) {
    const dish = {
      name: dishName,
      price: dishPrice
    };
    return this._courses[courseName].push(dish);
  },
  getRandomDishFromCourse(courseName) {
    const dishes = this._courses[courseName];
    const randomIndex = Math.floor(Math.random() * dishes.length)
    return dishes[randomIndex];
  },
  generateRandomMeal(){
    const appetizer = this.getRandomDishFromCourse('appetizers');
    const main = this.getRandomDishFromCourse('mains');
    const dessert = this.getRandomDishFromCourse('desserts');
    const totalPrice = appetizer.price + main.price + dessert.price;
    return `You have chosen ${appetizer.name} for your appetizer, ${main.name} for your entrée, and ${dessert.name} for dessert. Your total will be ${totalPrice}`
  }
};
menu.addDishToCourse('appetizers', 'chicken wings', 8.50);
menu.addDishToCourse('appetizers', 'pretzel bites', 6.50);
menu.addDishToCourse('appetizers', 'chips and salsa', 4.50);
menu.addDishToCourse('mains', 'hamburger', 10.50);
menu.addDishToCourse('mains', 'tacos', 9.50);
menu.addDishToCourse('mains', 'pulled pork sandwich', 12.50);
menu.addDishToCourse('desserts', 'cookie pie', 8.50);
menu.addDishToCourse('desserts', 'sundae', 10.50);
menu.addDishToCourse('desserts', 'brownie supreme', 8.50);

let meal = menu.generateRandomMeal();
console.log(meal);
