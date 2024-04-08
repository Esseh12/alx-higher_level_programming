#!/usr/bin/node

// a script that prints x times “C is fun”

const process = require('process');
const integer = parseInt(process.argv[2]);

if (process.argv[2] === undefined) {
  console.log('Missing number of occurrences');
} else if (integer > 0) {
  const stringToRepeat = 'C is fun\n';
  const result = stringToRepeat.repeat(integer);
  console.log(result);
} else if (integer < 0) {
  process.exit();
}
