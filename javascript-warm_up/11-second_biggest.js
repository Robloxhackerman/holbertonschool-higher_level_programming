#!/usr/bin/node
let len = process.argv.length;
let sorted = [];

if (process.argv[3]) {
  while (len > 2) {
    len--; sorted.push(process.argv[len]);
  } // copy paste of given nums

  sorted = sorted.sort((a, b) => a - b); // sorting for easier comparison
  const res = sorted[sorted.length - 2]; // process.argv.length - 4 works
  console.log(res);
} else if (process.argv[2]) {
  console.log(process.argv[2]);
} else {
  console.log(0);
}