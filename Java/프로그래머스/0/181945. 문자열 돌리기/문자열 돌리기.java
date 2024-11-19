import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        if(a.length() < 1 || a.length() > 10) {
            System.out.print("str 길이 초과");
        }
        
        for (int i =0; i < a.length(); i++) {
            System.out.println(a.charAt(i));
        }
    }
}