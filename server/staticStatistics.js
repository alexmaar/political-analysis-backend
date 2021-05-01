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
        let dateRange = req.body.dateRange;
        promises = [];
        categories.forEach(element => {
          let supportingStike = 2;
          if(element == 'za')supportingStike = 1;
          if(element == 'przeciw')supportingStike = 0;
          if (dateRange.length === 2){
            promises.push(dbAllAsPromise("SELECT COUNT(*) FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + dateRange[0].slice(0, 10) + "\") AND date(\"" + dateRange[1].slice(0,10) + "\") ", db));
          }
          else{
            promises.push(dbAllAsPromise("SELECT COUNT(*) FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ")", db));
          }
        });
        let data = await Promise.all(promises);
        result.send(data.map((e) => e[0]['COUNT(*)']));
      }
      catch (error) { throw error; }
    });

    app.post('/total-likes', async (req, result) => {
  
      try{
        let categories = req.body.categories;
        let dateRange = req.body.dateRange;
        promises = [];
        categories.forEach(element => {
          let supportingStike = 2;
          if(element == 'za')supportingStike = 1;
          if(element == 'przeciw')supportingStike = 0;
          if (dateRange.length == 2){
            promises.push(dbAllAsPromise("SELECT SUM(t.likes_count) as likes FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + dateRange[0].slice(0, 10) + "\") AND date(\"" + dateRange[1].slice(0,10) + "\")", db));
          }
          else {
            promises.push(dbAllAsPromise("SELECT SUM(t.likes_count) as likes FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ")", db));
          }
        });
        
        let data = await Promise.all(promises);
        result.send(data.map((e) => e[0].likes));
      }
      catch (error) { throw error; }
    });

    app.post('/total-retweets', async (req, result) => {
  
      try{
        let categories = req.body.categories;
        let dateRange = req.body.dateRange;
        promises = [];
        categories.forEach(element => {
          let supportingStike = 2;
          if(element == 'za')supportingStike = 1;
          if(element == 'przeciw')supportingStike = 0;
          if (dateRange.length == 2){
            promises.push(dbAllAsPromise("SELECT SUM(t.retweets_count) as likes FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + dateRange[0].slice(0, 10) + "\") AND date(\"" + dateRange[1].slice(0,10) + "\")", db));
          }
          else {
            promises.push(dbAllAsPromise("SELECT SUM(t.retweets_count) as likes FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ")", db));
          }
        });
        let data = await Promise.all(promises);
        result.send(data.map((e) => e[0].likes));
      }
      catch (error) { throw error; }
    });
  };