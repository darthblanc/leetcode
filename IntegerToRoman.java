import java.util.Scanner;

public class IntegerToRoman {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        long start = System.currentTimeMillis();
        System.out.println(intToRoman(num));
        System.out.print(System.currentTimeMillis()-start);
//        I             1
//        V             5
//        X             10
//        L             50
//        C             100
//        D             500
//        M             1000
//        I can be placed before V (5) and X (10) to make 4 and 9.
//        X can be placed before L (50) and C (100) to make 40 and 90.
//        C can be placed before D (500) and M (1000) to make 400 and 900.
        //  TH     H     T      U
        //1 <= num <= 3999
    }
    public static String intToRoman(int num) {
        String newNum = String.valueOf(num);
        String rv = "";
        for (int i = 0; i < newNum.length(); i++) {
            if (newNum.charAt(i)=='1' && newNum.length()-i == 4) rv+='M';
            if (newNum.charAt(i)=='1' && newNum.length()-i == 3) rv+='C';
            if (newNum.charAt(i)=='1' && newNum.length()-i == 2) rv+='X';
            if (newNum.charAt(i)=='1' && newNum.length()-i == 1) rv+='I';
            if (newNum.charAt(i)=='4' && newNum.length()-i == 3) rv+="CD";
            if (newNum.charAt(i)=='4' && newNum.length()-i == 2) rv+="XL";
            if (newNum.charAt(i)=='4' && newNum.length()-i == 1) rv+="IV";
            if (newNum.charAt(i)=='5' && newNum.length()-i == 3) rv+='D';
            if (newNum.charAt(i)=='5' && newNum.length()-i == 2) rv+='L';
            if (newNum.charAt(i)=='5' && newNum.length()-i == 1) rv+='V';
            if (newNum.charAt(i)=='9' && newNum.length()-i == 3) rv+="CM";
            if (newNum.charAt(i)=='9' && newNum.length()-i == 2) rv+="XC";
            if (newNum.charAt(i)=='9' && newNum.length()-i == 1) rv+="IX";
            else if (newNum.charAt(i)!='0') {
                rv+=specialCase(newNum.substring(i,i+1),newNum.length()-i);
            }
        }
        return rv;
    }
// [3] 465
    private static String specialCase(String newNum, int i) {
        int rv = Integer.parseInt(newNum);
        if (rv > 1 && rv < 4){
            if (i == 4) return generateMs(rv);
            if (i==3) return generaeCs(rv);
            if (i==2) return generateXs(rv);
            if (i==1) return generateIs(rv);
        }
        if (rv > 5 && rv < 9){
            if (i==3) return "D" + generaeCs(rv-5);
            if (i==2) return "L" + generateXs(rv-5);
            if (i==1) return "V" + generateIs(rv-5);
        }
        return "";
    }

    private static String generateIs(int rv) {
        String rev = "";
        for (int i = 0; i < rv; i++) {
            rev += "I";
        }
        return rev;
    }

    private static String generateXs(int rv) {
        String rev = "";
        for (int i = 0; i < rv; i++) {
            rev += "X";
        }
        return rev;
    }

    private static String generaeCs(int rv) {
        String rev = "";
        for (int i = 0; i < rv; i++) {
            rev += "C";
        }
        return rev;
    }

    private static String generateMs(int rv) {
        String rev = "";
        for (int i = 0; i < rv; i++) {
            rev += "M";
        }
        return rev;
    }
}
