import java.util.*;

public class MinimumTimeDifference {
    public static void main(String[] args){
        List<String> timePoints = new ArrayList<>(){{
            add("22:40");
            add("18:20");
            add("12:41");
            add("11:59");
            add("00:00");
            add("23:59");
        }};
        System.out.println(findMinDifference(timePoints));
    }

    private static int findMinDifference(List<String> timePoints) {
        int min = Integer.MAX_VALUE;
        ArrayList<Integer> sortedTime = new ArrayList<>();
        for (String s: timePoints) {
            sortedTime.add(Integer.parseInt(s.substring(0,2))*60+Integer.parseInt(s.substring(3))); //convert time to minutes and add to arraylist
        }
        Collections.sort(sortedTime); //sort the time in minutes //time complexity (O)n log n
        System.out.println(sortedTime);
        for (int i = 0; i < sortedTime.size()-1; i++) {
            // this works fine because after sorting times are right beside their closest times
            // hence just look for the minimum time difference from here
            if (sortedTime.get(i+1)-sortedTime.get(i)<min) min = sortedTime.get(i+1)-sortedTime.get(i);
        }
        // lEdge is a conversion of the first element
        // if the last is > 18:00
        // then increase the first by 24 hrs
        int lEdge = 0;
        if (sortedTime.get(sortedTime.size()-1)>1080 && sortedTime.get(0)<720) lEdge = 1440 + sortedTime.get(0);
        else lEdge = sortedTime.get(0);
        //wrap is the distance from last element to the first element
        int wrap = Math.abs(lEdge - sortedTime.get(sortedTime.size()-1));
        //check for the minimum value between the already gotten minimum from the linear search and wrapped edge
        min = Math.min(min,wrap);
        return min;
    }
    // it is a great habit to check what others did, you learn more
}