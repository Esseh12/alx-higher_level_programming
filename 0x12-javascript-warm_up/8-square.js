#!/usr/bin/node

// a script that prints x times “C is fun”

const process = require('process');
const integer = parseInt(process.argv[2]);

if (isNaN(integer)) {
  console.log('Missing size');
} else if (integer > 0) {
// const stringToRepeat = 'C is fun\n';
// const result = stringToRepeat.repeat(integer);
// console.log(result);
  let result = '';
  const stringToRepeat = 'X';
  for (let i = 0; i < integer; i++) {
    if (i < integer - 1) {
      console.log(stringToRepeat.repeat(integer));
    } else {
      result += stringToRepeat.repeat(integer); // Don't add a new line for the last repetition
    }
  }
  console.log(result);
} else if (integer < 0) {
  process.exit();
}
