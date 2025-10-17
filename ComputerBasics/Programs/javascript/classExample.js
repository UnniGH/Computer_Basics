// Define a class named 'Person'
class Person {
  // The constructor method is called when a new object is created
  constructor(name, age) {
    this.name = name; // Property
    this.age = age;   // Property
  }

  // A method of the Person class
  greet() {
    console.log(`Hello, my name is ${this.name} and I am ${this.age} years old.`);
  }

  // Another method
  celebrateBirthday() {
    this.age++;
    console.log(`${this.name} is now ${this.age} years old! Happy Birthday!`);
  }
}

// Create objects (instances) from the 'Person' class
const person1 = new Person("Alice", 30);
const person2 = new Person("Bob", 25);

// Call methods on the objects
person1.greet();           // Output: Hello, my name is Alice and I am 30 years old.
person2.greet();           // Output: Hello, my name is Bob and I am 25 years old.

person1.celebrateBirthday(); // Output: Alice is now 31 years old! Happy Birthday!
person1.greet();           // Output: Hello, my name is Alice and I am 31 years old.