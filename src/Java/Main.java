public class Main {
    public static void main(String args[]) {
        int n = 18;
        for (int i = 2; i < n; i++) {
            for (int j = 3; j < n; j++) {
                int val1 = (int)Math.pow(i, j);
                int val2 = (int)Math.pow(j, i);
                if (val1 + val2 == n) {
                    System.out.println(i + " " + j);
                }
            }
        }
    }
}
