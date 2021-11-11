let raceNumber = Math.floor(Math.random() * 1000);

const registeredEarly = false;

const runnerAge = 25;

if (registeredEarly && runnerAge > 18) {
  raceNumber += 1000;
}

if (registeredEarly && runnerAge > 18) {
  console.log(`${raceNumber}. Race begins at 9:30AM!`);
} else if(!registeredEarly && runnerAge > 18) {
  console.log(`${raceNumber}. Race begins at 11:00AM!`);
} else if(runnerAge < 18) {
  console.log(`${raceNumber}. Race begins at 12:30AM!`);
} else {
  console.log(`${raceNumber}, please visit the registration desk.`);
}
