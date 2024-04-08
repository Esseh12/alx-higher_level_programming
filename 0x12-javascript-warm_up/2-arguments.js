#!/usr/bin/node

const process = require('process');
const processLength = process.argv.length;

if (processLength === 2) {
  console.log('No argument');
} else if (processLength === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
