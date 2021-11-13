const team = {
  _players: [
    {
      firstName: 'Joe',
      lastName: 'Robinson',
      age: 32
    },
    {
      firstName: 'Jesse',
      lastName: 'Rodriguez',
      age: 29
    },
    {
      firstName: 'Alex',
      lastName: 'Jackson',
      age: 26
    },
  ],
  _games: [
    {
      opponents: 'Golden Saints',
      teamPoints: 42,
      opponentPoints: 28
    },
    {
      opponents: 'Sea Dogs',
      teamPoints: 21,
      opponentPoints: 24
    },
    {
      opponents: 'Stormwatch',
      teamPoints: 35,
      opponentPoints: 7
    },
  ],
  get players() {
    return this._players;
  },
  get games() {
    return this._games;
  },
  addPlayer(firstName, lastName, age) {
    let player = {
      firstName: firstName,
      lastName: lastName,
      age: age
    };
    this.players.push(player);
  },
  addGame(opponents, teamPoints, opponentPoints) {
    let game = {
      opponents,
      teamPoints,
      opponentPoints
    };
    this.games.push(game);
  }
};
team.addPlayer ('Geoff', 'Carson', 28);
team.addPlayer ('Benny', 'Jones', 44);
team.addPlayer ('Major', 'Banks', 36);
console.log(team._players);

team.addGame ('Rainfall', 14, 42);
team.addGame ('Tallymen', 28, 35);
team.addGame ('Distinguished Gentlemen', 38, 35);
console.log(team._games);
