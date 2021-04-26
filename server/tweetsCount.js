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
    app.get('/tweetsCount/', async (req, result) => {
        const parameters = req.query.categories;
        const cat =eval(parameters);
        const injectedString = cat.map(c => `'${c}'`).join(', ');

      try{
          

        // const tags = req.params.tags;
        // const startDate = req.params.startDate;
        // const endDate = req.params.endDate;

        const countTotalPromise = dbAllAsPromise(`SELECT category, count(t.id) as count FROM tweets as t join users as u on u.id = t.user_id GROUP BY category HAVING category in (${injectedString})`, db);
        let countTotal = await Promise.all([countTotalPromise]);
        console.log(countTotal);
        countTotal = countTotal[0].filter(row => row.category != null);

        result.send({ countTotal});
      }
      catch (error) { throw error; }
    });
  };