#!/usr/bin/node
let PAPO = '';
let PEPE = 0;
if (parseInt(process.argv[2])) {
  PEPE = parseInt(process.argv[2]);
  for (let PEPE1 = 0; PEPE1 < PEPE; PEPE1++) {
    PAPO = '';
    for (let PEPE2 = 0; PEPE2 < PEPE; PEPE2++) {
      PAPO += 'X';
    }
    console.log(PAPO);
  }
} else {
  console.log('Missing size');
}
