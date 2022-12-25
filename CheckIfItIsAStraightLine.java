import java.util.ArrayList;
import java.util.Date;

public class CheckIfItIsAStraightLine {

    public static void main(String[] args) {
        //int[][] coordinates = {{1,2},{2,3},{3,4},{4,5},{5,6},{6,7}};
        //int[][] coordinates = {{1,-8},{2,-3},{1,2}};
        //int[][] coordinates = {{1,1},{2,2},{2,0}};
        //int[][] coordinates = {{0,0},{0,1},{0,-1}};
        // int[][] coordinates = {{-4,-3},{1,0},{3,-1},{0,-1},{-5,2}};
        int[][] coordinates = {{-3, -2}, {-1, -2}, {2, -2}, {-2, -2}, {0, -2}};
        System.out.println(checkStraightLine(coordinates));
    }

    public static boolean checkStraightLine(int[][] coordinates) {
        ArrayList<Double> arrayList =  new ArrayList<>();
        for (int i = 0; i < coordinates.length-1; i++) {
            if((coordinates[i][0] - coordinates[i+1][0])==0) arrayList.add(Double.MAX_VALUE);
            else {
                if (((double) coordinates[i][1] - (double) coordinates[i + 1][1]) / ((double) coordinates[i][0] - (double) coordinates[i + 1][0]) == -0)
                    arrayList.add(0.0);
                else
                    arrayList.add(((double) coordinates[i][1] - (double) coordinates[i + 1][1]) / ((double) coordinates[i][0] - (double) coordinates[i + 1][0]));
            }
            // System.out.println(arrayList);
        }

        System.out.println(arrayList);

        for (int i = 1; i < arrayList.size(); i++) {
            if (! arrayList.get(0).equals(arrayList.get(i))){
                return false;
            }
        }
        return true;
    }
}
