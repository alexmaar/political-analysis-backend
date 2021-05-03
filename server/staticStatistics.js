function dbAllAsPromise(query, db) {
  return new Promise(function (resolve, reject) {
    db.all(query, [], function (err, rows) {
      if (err) reject("Read error: " + err.message)
      else {
        resolve(rows)
      }
    })
  });
}

module.exports = (app, db) => {

  app.post('/total-count', async (req, result) => {

    try {
      let categories = req.body.categories;
      let dateRange = req.body.dateRange;
      let attribute = req.body.attribute;
      let start, end;

      if (dateRange.length !== 2) {
        start = "2020-11-23";
        end = "2022-11-23";
      }
      else {
        start = dateRange[0].slice(0, 10);
        end = dateRange[1].slice(0, 10);
      }

      let promises = [];

      categories.forEach(element => {
        let supportingStike = 2;
        if (element == 'za') supportingStike = 1;
        if (element == 'przeciw') supportingStike = 0;

        switch (attribute) {
          case "tweets":
            promises.push(dbAllAsPromise("SELECT COUNT(*) as result FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + start + "\") AND date(\"" + end + "\") ", db));
            break;
          case "likes":
            promises.push(dbAllAsPromise("SELECT SUM(t.likes_count) as result FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + start + "\") AND date(\"" + end + "\")", db));
            break;
          case "retweets":
            promises.push(dbAllAsPromise("SELECT SUM(t.retweets_count) as result FROM tweets t join users u on u.id = t.user_id WHERE (category='" + element + "' OR political_party='" + element + "' OR supporting_strike=" + supportingStike + ") AND t.date BETWEEN date(\"" + start + "\") AND date(\"" + end + "\")", db));
            break;
          default:
            break;
        }
      });

      let data = await Promise.all(promises);
      result.send(data.map((e) => e[0].result));
    }
    catch (error) { throw error; }
  });
}