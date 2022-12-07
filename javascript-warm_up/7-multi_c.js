#!/usr/bin/node
try {
  const PEPE = parseInt(process.argv[2]);
  for (let PEPE1 = 0; PEPE1 < PEPE; PEPE1++) {
    console.log('C is fun');
  }
} catch (error) {
  console.log('Missing number of occurrences');
}
