#!/usr/bin/node
let len = process.argv.length;
let sorted = [];

if (process.argv[3]) {
  while (len > 2) {
    len--; sorted.push(process.argv[len]);
  }

  sorted = sorted.sort((a, b) => a - b);
  const res = sorted[sorted.length - 2];
  console.log(res);
} else if (process.argv[2]) {
  console.log(0);
} else {
  console.log(0);
}
