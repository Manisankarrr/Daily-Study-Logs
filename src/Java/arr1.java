import java.util.*;


public class arr1{
    public static void main(String[] args) {
        // String[] fruits = {"Apple", "Banana", "Cherry"};
        
        // fruits[0] = "Grapes";//replace with Apple
        // //int n = fruits.length;
        // Arrays.sort(fruits);
        // //Arrays.fill(fruits,"Apple");
        // // for (int i = 0; i < n; i++) {
        // //     System.out.print(fruits[i]+" ");
        // // }
        // for(String i: fruits){
        //     System.out.print(i+" ");
        // }

        Scanner sc = new Scanner(System.in);
        System.out.println("Enter size: ");
        int n = sc.nextInt();
        sc.nextLine();        
        // String[] food = new String[n];
        // System.out.printf("Enter food %d name: ",n);
        // for(int i=0;i<n;i++){

        //     food[i] = sc.nextLine();
        // }
        // for(String i: food){
        //     System.out.println(i);
        // }

        boolean found = false;
        int num[] = new int[n];
        System.out.println("Enter target number: ");  // Read target number from user input
        int target = sc.nextInt();
        sc.nextLine(); // Consume newline character after reading target number

        for(int i=0;i<n;i++)
        {
            System.out.printf("Enter number %d: ",i+1);
            num[i] = sc.nextInt();
        }

        for(int i=0;i<n;i++)
        {
            if(target == num[i])
            {
                System.out.printf("Element %d found at index: %d",target,i);
                found = true;
                break;
            }
        }
        if(!found){
            System.out.printf("Element %d not found in array",target);
        }












        
        sc.close();

    }
}