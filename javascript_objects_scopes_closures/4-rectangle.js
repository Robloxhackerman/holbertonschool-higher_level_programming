#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (PAPO = 'X') {
    for (let PEPE1 = 0; PEPE1 < this.height; PEPE1++) {
      let PEPE2 = 0;
      for (; PEPE2 < this.width; PEPE2++) {
        process.stdout.write(PAPO);
      }
      if (PEPE2 === this.width) {
        console.log('');
      }
    }
  }

  rotate () {
    const PEPE = this.width;
    this.width = this.height;
    this.height = PEPE;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
};
