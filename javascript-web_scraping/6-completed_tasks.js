#!/usr/bin/node

const request = require('request');
const arg = process.argv;
let info = '';
const mapi = {};

request(arg[2], function (error, response, body) {
  if (error) {
    console.log(error);
  }
  info = JSON.parse(body);

  for (let PEPE1 = 0; PEPE1 < info.length; PEPE1++) {
    const useMe = info[PEPE1].userId;

    if (info[PEPE1].completed) {
      mapi[useMe] = 0;

      for (let PEPE2 = 0; PEPE2 < info.length; PEPE2++) {
        if (info[PEPE1].userId === info[PEPE2].userId) {
          if (info[PEPE2].completed === true) {
            mapi[useMe] = mapi[useMe] + 1;
          }
        }
      }
    }
  }

  console.log(mapi);
});
