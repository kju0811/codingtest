import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        if (a.length() < 1 || a.length() > 1000000) {
            System.out.print("str 길이 초과");
        }
        System.out.print(a);
    }
}