#!/usr/bin/node

const process = require('process');

const string = process.argv[2];
const integer = parseInt(string);
if (process.argv[2] === undefined) {
  console.log('Not a number');
} else if (isNaN(process.argv[2]) !== true) {
  console.log('My number:' + ' ' + integer);
} else {
  console.log('Not a number');
}
