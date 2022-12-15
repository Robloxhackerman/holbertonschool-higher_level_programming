#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const arg = process.argv;
let web = 'a';

request(arg[2], function (error, response, body) {
  web = body;

  fs.writeFile(arg[3], web, 'utf-8', (error) => {
    if (error) {
      console.log(error);
    }
  });
});
