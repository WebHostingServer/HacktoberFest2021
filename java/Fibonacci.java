import static java.lang.System.exit;
import java.util.Scanner;

/**
 *
 * @author Tiago Ribeiro (https://github.com/Tiago-S-Ribeiro)
 */
public class fibonacciNumber {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        if (n < 0) {

        } else {
            elemFibonaci(n);
        }
    }

    public static void elemFibonaci(int n) {
        if (n == 0 || n == 1) {
            System.out.println("Fibonacci number!");
            exit(0);
        }

        int n1 = 0, n2 = 1, n3;
        for (int i = 2; i < n; ++i) {
            n3 = n1 + n2;
            if (n == n3) {
                System.out.println("Fibonacci number!");
                exit(0);
            }
            n1 = n2;
            n2 = n3;
        }
        System.out.println("Not a Fibonacci number!");
    }
}