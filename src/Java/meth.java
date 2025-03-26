import java.util.Scanner;
public class meth {
    public static void main(String args[]) {

        Scanner scanner = new Scanner(System.in);
        String name  = "manish";

        happy(name);
        int num = scanner.nextInt();
        // double res = square(num);
        System.out.println(square(num));
        scanner.close();
        
    }
    static void happy(String name){
        System.out.printf("Happy Birthday to %s\n",name);}
    static double square(int number){
            return number * number;
        }
    }
    
   

