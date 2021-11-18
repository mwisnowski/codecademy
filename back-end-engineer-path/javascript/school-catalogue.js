
// step 1: make a school class
class School {
  // step 2: set school constructor
  constructor(name, level, numberOfStudents) {
    // step 3: set school properties
    this._name = name;
    this._level = level;
    this._numberOfStudents = numberOfStudents;
  }
  //step 4: create getters for above constructor
  get name () {
    return this._name;
  }
  get level() {
    return this._level;
  }
  get numberOfStudents() {
    return this._numberOfStudents;
  }
  // step 5: set number of students
  set numberOfStudents(newNumberOfStudents) {
    if(typeof studentNumber === number) {
      this._numberOfStudents = studentNumber;
    } else {
      console.log('Invalid input: numberOfStudents must be set to a Number.');
    }
  }
  // step 6: create quickfact method
  quickFacts() {
    console.log(`${this.name} educates ${this.numberOfStudents} students at the ${this.level} school level.`);
  }
  // step 7: create substitute teacher picker
  static pickSubstituteTeacher(substituteTeachers) {
    let subNum = Math.floor(Math.random() * substituteTeachers.length);
    return substituteTeachers[subNum];
  }
}

// step 8: create primary school sub-class
class PrimarySchool extends School {
  // step 9: create PrimarySchool constructor
  constructor(name, numberOfStudents, pickupPolicy) {
    //step 10: fill in PrimarySchool constructor super
    super(name, 'primary', numberOfStudents);
    // step 11: add pickupPolicy
    this._pickupPolicy = pickupPolicy;
  }

  //step 12: set pickupPolicy getter
  get pickupPolicy() {
    return this._pickupPolicy;
  }
}

// step 13: create HighShcool subclass
class HighSchool extends School {
  constructor(name, numberOfStudents, sportsTeams) {
    super(name, 'high', numberOfStudents);
    this._sportsTeams = sportsTeams;
  }
  get sportsTeams() {
    return this._sportsTeams;
  }
}

// step 14 create PrimarySchool student
const lorraineHansbury = new PrimarySchool('Lorraine Hansbury', 514, 'Students must be picked up by a parent, guardian, or a family member over the age of 13.');

//console.log(lorraineHansbury);
//step 15: call quickfacts on lorraineHansbury
lorraineHansbury.quickFacts();

//step 16: call in a substitute teacher
const sub = School.pickSubstituteTeacher(['Jamal Crawford', 'Lou Williams', 'J. R. Smith', 'James Harden', 'Jason Terry', 'Manu Ginobli']);

//step 17: create alSmith high school
const alSmith = new HighSchool('Al E. Smith', 415, ['Baseball', 'Basketball', 'Volleyball', 'Track and Field']);

// step 18: list the sports teams at al smith
console.log(alSmith.sportsTeams.join(', '));
