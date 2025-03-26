public class Variablescope {

    static int x = 3;//  Class variable for Constant and OOPs
    public static void main(String[] args) {
        int x = 1;//Local variable
        System.out.println("x in main: " + x);
        method1();
    }
    static void method1() {
        int x = 2; //Local variable
        System.out.println("x in method: " + x);
    }
}