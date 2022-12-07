#!/usr/bin/node

const num = parseInt(process.argv[2]);
const res = factorializer(num);
console.log(res);

function factorializer (num) {
  if (num === 1 || !num) {
    return 1;
  } else if (num < 0) {
    return -1;
  } else {
    return (num * factorializer(num - 1));
  }
}
