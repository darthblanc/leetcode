import java.util.ArrayList;
import java.util.Scanner;

public class RomanToInteger {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String s = scanner.next();
        System.out.println(romanToInt(s));
    }

    private static int romanToInt(String s) {
        ArrayList<Integer> storage = new ArrayList<>();
        int solution = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'M') storage.add(1000);
            if (s.charAt(i) == 'D') storage.add(500);
            if (s.charAt(i) == 'C') storage.add(100);
            if (s.charAt(i) == 'L') storage.add(50);
            if (s.charAt(i) == 'X') storage.add(10);
            if (s.charAt(i) == 'V') storage.add(5);
            if (s.charAt(i) == 'I') storage.add(1);
        }
        for (int i = 0; i < storage.size() - 1; i++) {
            if (storage.get(i) >= storage.get(i + 1)) solution += storage.get(i);
            if (storage.get(i) < storage.get(i + 1)) solution -= storage.get(i);

        }
        solution+=storage.get(storage.size()-1);
        return solution;
    }
}
