#!/usr/bin/node
const dict = requiere('./101-data.js').dict;
const mapMe = {};
for (const [key, value] of dict) {
  mapMe.set(key, value);
}
