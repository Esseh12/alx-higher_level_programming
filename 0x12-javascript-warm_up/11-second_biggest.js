#!/usr/bin/node

const process = require('process');
const processLength = process.argv.length;

if (processLength < 3) {
  console.log('0');
} else if (processLength === 3) {
  console.log('0');
} else {
  const args = process.argv.map(Number)
    .slice(2, process.argv.length)
    .sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
