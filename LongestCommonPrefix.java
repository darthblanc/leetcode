import java.util.ArrayList;

public class LongestCommonPrefix {
    public String longestCommonPrefix(String[] strs) {
        String firstCheck = strs[0];
        int size = 1;
        for (int i = 1; i < strs.length; i++) {
            if (strs[i].equals(firstCheck)) size++;
        }
        if (size==strs.length) return firstCheck;

        if (strs.length==1) return strs[0];
        String testElement = "";
        int min = Integer.MAX_VALUE;
        for (int i = 0; i < strs.length;i++) {
            if (strs[i].length() < min) {
                min = strs[i].length();
                testElement = strs[i];
                if (testElement.equals("")) return "";
            }
        }
        String compare = compareSubstrings(strs[0], strs[1], testElement);
        if (strs.length==2) return compare;
        ArrayList<String> collector = new ArrayList<>();
        String solution;
        for (int i = 0; i < strs.length; i++) {
            solution = compareSubstrings(strs[i], compare, testElement);
            if (solution.length() < compare.length()) compare = solution;
        }
        return compare;
    }

    public static String compareSubstrings(String str, String str1, String testElement) {
        String build = "";
        if (str.length()==1 && str1.length()==1) if (str.charAt(0)==str1.charAt(0)) return str;
        int length = 0;
        if (str.length()>=str1.length()) length = str1.length();
        if (str.length()<str1.length()) length = str.length();
        for (int i = 0; i < length; i++) {
            if (str.charAt(i)==str1.charAt(i)) build += str.charAt(i);
            else return build;
        }
        return build;
    }
}
