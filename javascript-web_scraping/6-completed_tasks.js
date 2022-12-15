#!/usr/bin/node

const request = require('request')
const arg = process.argv;
let info = '';
let mapi = new Map();
let counter = 0;

request(arg[2], function(error, response, body) {
    info = JSON.parse(body);

    

    for (const x of info) {
        if (x.completed === true) {
            mapi.set(x.userId, mapi.get(x.userId) + 1 )
        }
    }
    console.log(mapi)
});