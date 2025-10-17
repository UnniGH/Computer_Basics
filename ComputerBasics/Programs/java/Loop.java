public class Loop {
    public static void main(String[] args) {

        System.out.println("For Loop Output:");
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteration: " + i);
        }

        int count = 1;
        System.out.println("While Loop Output:");
        while (count <= 5) {
            System.out.println("Count: " + count);
            count++; // Increment the counter
        }

        int num = 1;
        System.out.println("Do-While Loop Output:");
        do {
            System.out.println("Number: " + num);
            num++; // Increment the number
        } while (num <= 5); // Condition checked after the first execution

    }
}