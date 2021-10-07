/*
Name: Ankit Choudhury
- Place: Rourkela, Odisha, India
- Bio: First Year student at college.
- GitHub: [treasure363](https://github.com/treasure363)

Program Description:
Enter a matrix and the output is the sum of all the border elements.
*/
import java.util.Scanner;
class Borderland{
    public static void main(String[] args){
        Scanner sr = new Scanner(System.in);
        System.out.println("Input array dimensions :)");
        int m = sr.nextInt(), n = sr.nextInt();
        int[][] a = accept(m, n);
        System.out.println("The entered matrix is: ");
        display(a, m, n);
        System.out.println("Sum of border elements: "+getBoundarySum(a, m, n));
        sr.close();
    } 
    public static long getBoundarySum(int a[][], int m, int n) 
    {
        long sum = 0;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                if (i == 0)
                    sum += a[i][j];
                else if (i == m - 1)
                    sum += a[i][j];
                else if (j == 0)
                    sum += a[i][j];
                else if (j == n - 1)
                    sum += a[i][j];
            }
        }
        return sum;
    }
    public static void display(int a[][], int m, int n){
        for(int i = 0; i<m; i++){
            for(int j=0; j<n; j++)
                System.out.print(a[i][j]+"\t");
            System.out.println();
        }
    }
    public static int[][] accept(int m, int n){
        Scanner sr = new Scanner(System.in);
        int[][] a = new int[m][n];
        for(int i=0; i<m; i++)
            for(int j=0; j<n; j++){
                System.out.println("Enter input for ("+i+","+j+")");
                a[i][j] = sr.nextInt();
            }
        sr.close();
        return a;
    }
} 