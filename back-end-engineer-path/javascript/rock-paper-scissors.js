const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();
  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
    return userInput;
  } else {
    console.log('Error!');
  }
}

function getComputerChoice() {
  switch (Math.floor(Math.random() * 3)) {
    case 0:
      return 'rock';
      break;
    case 1:
      return 'paper';
      break;
    case 2:
      return 'scissors';
      break;
  }
}

function determineWinner(userChoice,computerChoice) {
  if (userChoice === computerChoice) {
    return 'It\'s a tie';
  } else if (userChoice === 'rock') {
    if (computerChoice === 'paper') {
      return 'Computer wins!';
    } else {
      return 'You won!';
    }
  } else if (userChoice === 'paper') {
    if (computerChoice === 'scissors') {
      return 'Computer wins!';
    } else {
      return 'You win!';
    }
  } else if (userChoice === 'scissors') {
    if (computerChoice === 'rock') {
      return 'Computer wins!';
    } else {
      return 'You win!';
    }
  } else if (userChoice === 'bomb'){
      return 'You win!';
    }
};

const playGame = () => {
  const userChoice = getUserChoice('bomb');
  const computerChoice = getComputerChoice();
  console.log('You threw: ' + userChoice);
  console.log('The computer threw: ' + computerChoice);
  console.log(determineWinner(userChoice, computerChoice));
};

playGame();
