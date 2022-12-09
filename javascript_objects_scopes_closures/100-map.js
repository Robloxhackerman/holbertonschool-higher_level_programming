#!/usr/bin/node
const list = require('./100-data.js').list;
const listMe = list.map((x, idx) => x * idx);
console.log(list);
console.log(listMe);
