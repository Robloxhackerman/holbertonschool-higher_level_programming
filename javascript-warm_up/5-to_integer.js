#!/usr/bin/node
const PEPE = process.argv[2];

if (parseInt(PEPE)) {
  console.log('My number: ' + parseInt(PEPE));
} else {
  console.log('Not a number');
}
