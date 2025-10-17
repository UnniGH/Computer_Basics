import java.util.Scanner; // Import the Scanner class

public class UserInput {
    public static void main(String[] args) {
        // Create a Scanner object to read input from the console
        Scanner scanner = new Scanner(System.in);

        // Prompt the user for their name
        System.out.print("Enter your name: ");
        String name = scanner.nextLine(); // Read the entire line of input as a String

        // Prompt the user for their age
        System.out.print("Enter your age: ");
        int age = scanner.nextInt(); // Read the next integer from the input

        // Print the collected information
        System.out.println("Hello, " + name + "! You are " + age + " years old.");

        // Close the scanner to release system resources
        scanner.close();
    }
}