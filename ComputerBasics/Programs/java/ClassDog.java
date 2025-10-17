// Define a class named 'Dog'
class Dog {
    // Attributes (fields) of the Dog class
    String name;
    String breed;

    // Method to make the dog bark
    void bark() {
        System.out.println(name + " says Woof! Woof!");
    }

    // Method to display the dog's details
    void displayDetails() {
        System.out.println("Name: " + name + ", Breed: " + breed);
    }
}

// Main class to demonstrate the Dog class
public class ClassDog {
    public static void main(String[] args) {
        // Create an object (instance) of the Dog class
        Dog myDog = new Dog();

        // Assign values to the object's attributes
        myDog.name = "Buddy";
        myDog.breed = "Golden Retriever";

        // Call methods on the object
        myDog.displayDetails(); // Output: Name: Buddy, Breed: Golden Retriever
        myDog.bark();           // Output: Buddy says Woof! Woof!

        // Create another object of the Dog class
        Dog anotherDog = new Dog();
        anotherDog.name = "Max";
        anotherDog.breed = "Labrador";

        anotherDog.displayDetails(); // Output: Name: Max, Breed: Labrador
        anotherDog.bark();           // Output: Max says Woof! Woof!
    }
}