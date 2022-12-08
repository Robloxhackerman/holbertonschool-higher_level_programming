#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let CSGO = 0;
  for (let PEPE1 = 0; PEPE1 < list.length; PEPE1++) {
    if (list[PEPE1] === searchElement) {
      ++CSGO;
    }
  }
  return CSGO;
};
