import java.util.*;
public class Main
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
	    int n=sc.nextInt();
	    int[] arr=new int[n];
	    for(int i=0;i<n;i++)
	    {
	        arr[i]=sc.nextInt();
	    }
	    int k=sc.nextInt();
	    int left=0;
	    int max=0;
	    int sum=0;
	    for(int right=0;right<n;right++)
	    {
	        sum+=arr[right];
	        while(sum>=k && left<=right)
	        {
	            sum-=arr[left];
	            left++;
	        }
	        int length=right-left+1;
	        max=Math.max(max,length);
	    }
	    System.out.print(max);
	    
	}
}