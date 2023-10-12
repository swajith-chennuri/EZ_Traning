import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class PalindromicSubstring {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String string = scanner.nextLine();
        int[] result = findPalindromicSubstrings(string);
        System.out.println("The maximum length of a palindromic substring = " + result[0]);
        System.out.println("The total number of palindromic substrings = " + result[1]);
    }

    public static int[] findPalindromicSubstrings(String string) {
        int maxLength = 0;
        List<String> palindromicSubstrings = new ArrayList<>();
        for (int i = 0; i < string.length(); i++) {
            for (int j = i + 1; j <= string.length(); j++) {
                String subString = string.substring(i, j);
                String reverseSubString = new StringBuilder(subString).reverse().toString();
                if (subString.equals(reverseSubString)) {
                    palindromicSubstrings.add(subString);
                    if (subString.length() > maxLength) {
                        maxLength = subString.length();
                    }
                }
            }
        }
        int[] result = {maxLength, palindromicSubstrings.size()};
        return result;
    }
}
