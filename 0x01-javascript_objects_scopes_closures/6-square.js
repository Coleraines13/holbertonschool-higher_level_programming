#!/usr/bin/node
module.exports = class Square extends require('/5-square.js') {
  constructor(size) {
    super(size, size);
  }


  charPrint(c) {
    const x = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
};
