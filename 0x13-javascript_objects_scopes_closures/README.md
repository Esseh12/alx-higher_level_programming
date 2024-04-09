# JavaScript Objects
## Overview
JavaScript is a versatile programming language that supports various data types and structures. One of the fundamental data structures in JavaScript is the object.

Objects in JavaScript are collections of key-value pairs, where each key is a unique identifier (also known as a property) and each value can be of any data type, including other objects, functions, arrays, and primitives.

Working with Objects
Creating Objects
Objects in JavaScript can be created using object literals or the new Object() syntax:

## javascript
// Using object literals
const person = {
  name: 'John',
  age: 30,
  isAdmin: false
};

// Using the new Object() syntax
const car = new Object();
car.brand = 'Toyota';
car.model = 'Camry';
car.year = 2020;
Accessing Object Properties
You can access object properties using dot notation (object.property) or bracket notation (object['property']):

## javascript
console.log(person.name);  // Output: John
console.log(car['model']); // Output: Camry
Modifying Object Properties
Object properties can be modified directly:

## javascript
person.age = 35;
car.year = 2021;
Adding New Properties
You can add new properties to an object dynamically:

## javascript
person.email = 'john@example.com';
car.color = 'blue';
Removing Properties
You can delete properties from an object using the delete operator:

## javascript
delete person.isAdmin;
delete car['color'];
