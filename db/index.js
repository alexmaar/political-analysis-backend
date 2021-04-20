const sqlite3 = require('sqlite3').verbose();
let db;

module.exports = {
  connectDatabase: function connectDatabase() {
    // open database in memory
    db = new sqlite3.Database('db/tweets.db', (err) => {
      if (err) {
        return console.error(err.message);
      }
      console.log('Connected to the SQlite database.');
    });
    return db;
  },
  
  // tego nie uzywamy, bo laczymy sie z bazą raz na poczatku, i to polączenie jest caly czas
  closeDatabaseConnection: function closeDatabaseConnection() {
    // close the database connection
    db.close((err) => {
      if (err) {
        return console.error(err.message);
      }
      console.log('Close the database connection.');
    });
  }
};