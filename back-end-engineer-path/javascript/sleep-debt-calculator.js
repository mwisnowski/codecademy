const getSleepHours = day => {
  day = day.toLowerCase()
  if (day === 'monday') {
    return 8;
  } else if  (day === 'tuesday') {
    return 7.5;
  } else if  (day === 'wednesday') {
    return 7.5;
  } else if  (day === 'thursday') {
    return 6;
  } else if  (day === 'friday') {
    return 8;
  } else if  (day === 'saturday') {
    return 8.5;
  } else if (day === 'sunday') {
    return 9;
  }
}

const getActualSleepHours = () => getSleepHours('Monday') + getSleepHours('Tuesday') + getSleepHours('Wednesday') +getSleepHours('Thursday') + getSleepHours('friday') + getSleepHours('saturday') + getSleepHours('sunday');

const getIdealSleepHours = () => {
  const idealHours = 8;
  return idealHours * 7;
}

console.log('You got ' + getActualSleepHours() + ' hours of sleep this week');
console.log('It would be ideal if you got ' + getIdealSleepHours() + ' hours of sleep this week');

const calculateSleepDebt = () => {
  const actualSleepHours = getActualSleepHours();
  const idealSleepHours = getIdealSleepHours();
  if (actualSleepHours === idealSleepHours) {
    console.log('You had ' + actualSleepHours + ' hours of sleep, you got enough sleep tshi week!');
  } else if (actualSleepHours > idealSleepHours) {
    console.log('You got ' + (actualSleepHours - idealSleepHours) + ' hours more than enough sleep this week!');
  } else {
    console.log('You needed ' + (idealSleepHours - actualSleepHours) + ' more hours of sleep this week...');
  }
};

calculateSleepDebt();
