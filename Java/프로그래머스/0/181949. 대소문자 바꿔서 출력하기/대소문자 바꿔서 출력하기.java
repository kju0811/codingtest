import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder result = new StringBuilder();
        
        if (a.length() < 1 || a.length() >20) {
            System.out.print("str 길이 초과");
            return;
        }
        
        for (char c : a.toCharArray()) {
            if (Character.isLowerCase(c)) {
                result.append(Character.toUpperCase(c));
            } else if (Character.isUpperCase(c)) {
                result.append(Character.toLowerCase(c));
            }
        }
        
        System.out.print(result.toString());
    }
}