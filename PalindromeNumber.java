import java.util.ArrayList;
import java.util.Objects;
import java.util.Scanner;

public class PalindromeNumber {

    public static void main (String[] args){
        Scanner scan =  new Scanner (System.in);
        String s = scan.next();

        System.out.println(verifyPalindrome(s));
    }
    public static boolean verifyPalindrome(String x){
        String y = String.valueOf(x);
        String[] arr = y.split("");
        ArrayList<String> booleanStore = new ArrayList<>();
        int length;
        if (arr.length%2==0) length= arr.length/2;
        else length= (arr.length/2)+1;
        for (int i = 0; i < length; i++) {
            if (!Objects.equals(arr[i], arr[arr.length - 1 - i])) booleanStore.add("false");
        }
        return !booleanStore.contains("false");
    }

}