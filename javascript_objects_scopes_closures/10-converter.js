#!/usr/bin/node
exports.converter = function (base) {
  function myConverter (coso) {
    return coso.toString(base);
  }
  return myConverter;
};
