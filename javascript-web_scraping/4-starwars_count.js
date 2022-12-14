#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    throw err;
  } else {
    if (response.statusCode === 200) {
      const data = JSON.parse(body).results;
      let count = 0;
      for (const each of data) {
        for (const chars of each.characters) {
          if (chars.endsWith('/18/')) {
            ++count;
          }
        }
      }
      return console.log(count);
    }
  }
});
