public class DataTypesExample {

    public static void main(String[] args) {
        // Primitive Data Types

        // Integer types
        byte myByte = 10;
        short myShort = 1000;
        int myInt = 50000;
        long myLong = 15000000000L; // 'L' suffix for long literal

        // Floating-point types
        float myFloat = 3.14f; // 'f' suffix for float literal
        double myDouble = 3.1415926535;

        // Character type
        char myChar = 'A';

        // Boolean type
        boolean myBoolean = true;

        // Reference Data Types

        // String (for text)
        String myString = "Hello, Java!";

        // Array
        int[] intArray = {10, 20, 30, 40, 50}; // Array of integers
        String[] stringArray = {"Apple", "Banana", "Cherry"}; // Array of Strings

        // Printing the values
        System.out.println("Primitive Data Types:");
        System.out.println("byte: " + myByte);
        System.out.println("short: " + myShort);
        System.out.println("int: " + myInt);
        System.out.println("long: " + myLong);
        System.out.println("float: " + myFloat);
        System.out.println("double: " + myDouble);
        System.out.println("char: " + myChar);
        System.out.println("boolean: " + myBoolean);

        System.out.println("\nReference Data Types:");
        System.out.println("String: " + myString);

        System.out.println("\nArray Examples:");
        System.out.print("int array: ");
        for (int i = 0; i < intArray.length; i++) {
            System.out.print(intArray[i] + " ");
        }
        System.out.println(); // New line

        System.out.print("String array: ");
        for (String fruit : stringArray) { // Enhanced for loop
            System.out.print(fruit + " ");
        }
        System.out.println();
    }
}