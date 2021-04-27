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
   
    app.post('/total', async (req, result) => {
  
      try{
        let categories = req.body.categories;
        promises = [];
        categories.forEach(element => {
          let supportingStike = 2;
          if(element == 'za')supportingStike = 1;
          if(element == 'przeciw')supportingStike = 0;
          promises.push(dbAllAsPromise("SELECT COUNT(*) FROM tweets t join users u on u.id = t.user_id WHERE category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike, db));
        });
        let data = await Promise.all(promises);
        result.send(data.map((e) => e[0]['COUNT(*)']));
      }
      catch (error) { throw error; }
    });
  };