#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let PAPO = '';
    for (let PEPE1 = 0; PEPE1 < this.height; PEPE1++) {
      PAPO = '';
      for (let PEPE2 = 0; PEPE2 < this.width; PEPE2++) {
        PAPO += 'X';
      }
      console.log(PAPO);
    }
  }

  rotate () {
    let PEPE = this.width;
    this.width = this.height;
    this.height = PEPE;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
