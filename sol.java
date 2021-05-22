// this is a solution to the colorful stones problems
import java.util.Scanner;

public class Solution {

    public static int get_stone_pos(String s, String t) {

        int pos = 1;
        int index = 0;

        for (int i = 0; i < t.length(); i++) {
            if (s.charAt(index) == t.charAt(i)) {
                pos++;
                index++;
            }
        }
        return pos;
    }

    public static void main (String args []) {
        // getting the input strings
        Scanner sc = new Scanner(System.in);
        String stones = sc.nextLine();
        String instructions = sc.nextLine();

        // pass to the funciont
        System.out.println(get_stone_pos(stones, instructions));

    }
}