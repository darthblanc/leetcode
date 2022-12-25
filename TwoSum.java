import java.util.Arrays;
import java.util.Scanner;

public class TwoSum {
    public static void main(String[] args){

    Scanner scanner = new Scanner(System.in);
    int target = scanner.nextInt();
    int[] nums = {2,5,5,11};

        System.out.println(Arrays.toString(twoSum(nums, target)));

}
    public static int[] twoSum(int[] nums, int target) {
        int[] solution = new int[2];
        outer:for (int i = 0; i < nums.length; i++) {
            for (int j = 1; j < nums.length; j++) {
                if (nums[i]==nums[j] && i ==j);
                else if (nums[i]+nums[j]==target) {
                    solution[0] = i;
                    solution[1] = j;
                    break outer;
                }
            }
        }
        return solution;
    }
}
