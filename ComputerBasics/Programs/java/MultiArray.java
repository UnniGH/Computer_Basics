public class MultiArray {
    public static void main(String[] args) {
        int[][] matrix = {
            {1, 2, 3, 10},
            {4, 5, 6, 11},
            {7, 8, 9, 12}
        };

        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.printf("%4d", matrix[i][j]); // Adjust %4d for desired spacing
            }
            System.out.println(); // New line after each row
        }
    }
}