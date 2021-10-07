/*
Name: Ankit Choudhury
- Place: Rourkela, Odisha, India
- Bio: First Year student at college.
- GitHub: [treasure363](https://github.com/treasure363)
*/
/*
Program Description:
Write a program to accept lower and upper range from user and print all GOLDBACH number within the range.
A number is GoldBach number  if it is a even integer  can be expressed  as the sum of two odd primes. 
If no such numbers exists then give appropriate messages. 
If a number is goldbach number print all possible combinations.
Example: 6=3+3, 10=3+7,10=5+5. So 6,10 are goldbach numbers.  
*/
import java.util.Scanner;
import java.util.Arrays;
public class GoldBachNumbers{
    public static void main(String args[]) {
        process();
    }
    public static void process(){
        Scanner ob =new Scanner(System.in);
        System.out.println("Enter the range to find GoldBach Number");
        System.out.print("Starting Point: ");
        int m = ob.nextInt();
        System.out.print("Endging Point: ");
        int n = ob.nextInt();
        boolean found = false;
        if(m <= n && m >= 0)
        {
            System.out.println("GOLDBACH numbers within the range "+m+" to "+n+" are as follows: ");
            boolean[] sieve = new boolean[n+2];
            Arrays.fill(sieve, true);
            sieve[0] = false;
            sieve[1] = false;
            for (int i = 2; i < n; i++) // Sieve of Eratosthenes
                if (sieve[i])
                    for (int j = i * 2; j < n; j += i)
                        sieve[j] = false;
            if (sieve.length>2)
                sieve[2] = false; //cancelling out even number
            for (int i = m; i < n+1; i++){
                int num = i;
                for (int j = 2; j < i; j++)
                    if(sieve[j]){
                        if (num - j >= 0)
                            if (sieve[num - j])
                                System.out.println(i+"="+j+"+"+(i-j));
                                found = true;
                    }
            }
            if(!found)
                System.out.println("NO GOLDBACH NUMBER FOUND BETWEEN THE RANGE "+m+" TO "+n);
        }
        else
            System.out.println("INVALID INPUT");
        ob.close();
    }
}