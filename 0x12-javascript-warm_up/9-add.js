#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const process = require('process');
const integer1 = parseInt(process.argv[2]);
const integer2 = parseInt(process.argv[3]);

console.log(add(integer1, integer2));
