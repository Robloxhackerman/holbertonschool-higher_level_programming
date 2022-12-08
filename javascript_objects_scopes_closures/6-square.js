#!/usr/bin/node
const Square = require('./5-square');
module.exports = class Square extends Square{
    constructor(size){
        super(size, size);
    }

    charPrint(c='X'){
        super.print(c)
    }
};