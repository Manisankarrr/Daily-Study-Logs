import java.util.*;

public class Ternary {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();

        // String grade = (score >= 60) ? "Pass" : "Fail";
        // System.out.println("Your grade is: " + grade);

        String num = (score % 2 == 0) ? "Even" : "Odd";
        System.out.println("The number is: " + num);

        sc.close();
    }
    
}
