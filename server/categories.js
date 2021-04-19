module.exports = (app, db) => {
  app.get('/categories', (req, result) => {
    let political_parties = [];
    let categories = [];
    let supporting_strike_options = [];
    db.all("SELECT DISTINCT supporting_strike FROM users", [], (err, rows) => {
      if (err) {
        throw err;
      }
      db.all("SELECT DISTINCT category FROM users", [], (err, rows) => {
        if (err) {
          throw err;
        }
        db.all(" SELECT DISTINCT political_party FROM users", [], (err, rows) => {
          if (err) {
            throw err;
          }
          political_parties = rows.map(row => row.political_party);
          result.send({ categories, political_parties, supporting_strike_options });
        });
        categories = rows.map(row => row.category);
      });
      supporting_strike_options = rows.map(row => row.supporting_strike);
    });
  });
};