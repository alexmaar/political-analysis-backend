function dbAllAsPromise(query, db) {
  return new Promise(function(resolve, reject) {
    db.all(query, [], function(err, rows)  {
        if(err) reject("Read error: " + err.message)
        else {
            resolve(rows)
        }
    })
  });
}

module.exports = (app, db) => {
  app.get('/categories', async (req, result) => {
    try{
      const political_parties_promise = dbAllAsPromise("SELECT DISTINCT political_party FROM users", db);
      const categories_promise = dbAllAsPromise("SELECT DISTINCT category FROM users", db);
      const supporting_strike_options_promise = dbAllAsPromise("SELECT DISTINCT supporting_strike FROM users", db);
      let [political_parties, categories, supporting_strike_options] = await Promise.all([political_parties_promise, categories_promise, supporting_strike_options_promise]);
      political_parties = political_parties.map(row => row.political_party);
      categories = categories.map(row => row.category);
      supporting_strike_options = supporting_strike_options.map(row => row.supporting_strike);

      result.send({ categories, political_parties, supporting_strike_options });
    }
    catch (error) { throw error; }
  });
};