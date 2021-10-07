/*
Name: Ankit Choudhury
- Place: Rourkela, Odisha, India
- Bio: First Year student at college.
- GitHub: [treasure363](https://github.com/treasure363)
*/

/*
Program Description:
A Composite Magic number is a positive integer which is composite as well as a magic number.
Composite number : A composite number is a number which has more than 2 factors.
For example : 10
Factors are : 1,2,5,10.
Magic number : A magic number is a number in which the eventual sum of the
digits is equal to 1.
For example:- 28 = 2+ 8 =10 = 1+0=1
Accept 2 positive integers m and n, where m is less than n as user input. Display the number of
composite magic integers that are in the range between m and n (both inclusive) and output them
along with the frequency, in the format specified below.
Test your program with the sample data and some random data:

Example 1:
INPUT:
m=10
n=100
OUTPUT:
THE COMPOSITE MAGIC INTEGERS ARE :
10,28,46,55,64,82,91,100
FREQUENCY OF COMPOSITE MAGIC INTEGERS IS :8

Example 2:INPUT:
m=1200
n=1300
OUTPUT:
THE COMPOSITE MAGIC INTEGERS ARE :
1207,1216,1225,1234,1243,1252,1261,1270,1288
FREQUENCY OF COMPOSITE MAGIC INTEGERS IS :9

Example 3:
INPUT:
m=120
n=99
OUTPUT:
INVALID INPUT
*/
import java.util.Scanner;
public class CompositeMagicNumbers{
    public static void main(String args[]) {
        process();
    }
    public static void process(){
        Scanner ob =new Scanner(System.in);
        System.out.println("Enter the range to find Composite Magic Number");
        System.out.print("Starting Point: ");
        int m = ob.nextInt();
        System.out.print("Ending Point: ");
        int n = ob.nextInt();
        if(m <= n && m >= 0)
        {
            String ans = "";
            for(int i = m; i <= n; i++)
            {
                int sum = sum_of_digits(i);
                String num = Integer.toString(sum);
                int len = num.length();
                while (len > 1)
                {
                    sum = sum_of_digits(sum);
                    num = Integer.toString(sum);
                    len = num.length();
                }
                if (sum == 1 && !prime(i))
                {
                    num = Integer.toString(i);
                    ans += num + ", ";
                }
            }
            if (ans.length()>=2){
                System.out.println("THE COMPOSITE MAGIC INTEGERS ARE :");
                System.out.println(ans.substring(0,ans.length()-2));
            }
            else
                System.out.println("NONE FOUND IN THE RANGE "+m+" TO "+n);
        }
        else
            System.out.println("INVALID INPUT");
        ob.close();
    }
    public static int sum_of_digits(int n)
    {
        int sum = 0;
        while(n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }
    public static boolean prime(int n)
    {
        for(int i=2; i*i <= n; i++)
            if(n % i == 0)
                return false;
        return true;
    }
}