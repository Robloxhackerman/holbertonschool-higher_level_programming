#!/usr/bin/node
exports.esrever = function (list) {
  const listita = [];

  for (let PEPE1 = list.length - 1; PEPE1 >= 0; --PEPE1) {
    listita.push(list[PEPE1]);
  }
  return listita;
};
