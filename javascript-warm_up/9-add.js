#!/usr/bin/node
function add(a, b) {
    return a + b;
}
let PAPOTE = add(process.argv[2], process.argv[3]);
console.log(PAPOTE);