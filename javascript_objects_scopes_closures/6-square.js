#!/usr/bin/node
const Squirt = require('./5-square');
module.exports = class Square extends Squirt{
    constructor(size){
        super(size, size);
    }

    charPrint(c='X'){
        super.print(c)
    }
};