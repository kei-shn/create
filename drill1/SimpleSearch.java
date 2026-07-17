public class SimpleSearch {

    public static void main(String[] args) {
        int[] numbers = { 10, 25, 45, 70, 95 };
        int target = 70;

        int resultIndex = findTargetIndex(numbers, target);

        if (resultIndex != -1) {
            System.out.println("Target " + target + " found at index: " + resultIndex);
        } else {
            System.out.println("Target " + target + " was not found.");
        }
    }

    public static int findTargetIndex(int[] arr, int searchKey) {

        for (int i = 0; i < arr.length; i++) {

            if (arr[i] == searchKey) {
                return i;
            }
        }

        return -1;
    }
}