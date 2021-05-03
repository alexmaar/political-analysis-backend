const express = require("express");
const sqlite = require('../db/index');

const PORT = process.env.PORT || 3001;

const app = express();
// connect db
const db = sqlite.connectDatabase();

// paring body
app.use(express.urlencoded({ extended: true }));
// Parse JSON bodies (as sent by API clients)
app.use(express.json());

// test endpoint
app.get("/api", (req, res) => {
    res.json({ message: "Hello from server !"});
});

// endpoint /categories - zwraca wszystkie możliwe kategorię
require('./categories')(app, db);
require('./staticStatistics')(app, db);
require('./tweetsCount')(app, db);

app.listen(PORT, () => {
  console.log(`Server listening on ${PORT}`);
});