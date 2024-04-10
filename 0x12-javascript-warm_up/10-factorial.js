#!/usr/bin/node

const process = require('process');
const integer = parseInt(process.argv[2]);

if (isNaN(integer)) {
  console.log(1);
} else if (isNaN(integer) === false) {
  function factorial (n) {
    if (n === 0 || n === 1) {
      return 1;
    } else {
      return n * factorial(n - 1);
    }
  }
  const Result = factorial(integer);
  console.log(Result);
}
