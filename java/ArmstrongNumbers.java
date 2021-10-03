import java.util.Scanner;

/**
 * This simple algorithm displays all Armstrong numbers up until a user-entered value N
 * Example:
 * User enters: 200
 * Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153
 * @author Tiago Ribeiro (https://github.com/Tiago-S-Ribeiro)
 */
public class checkArmstrongNumbers {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        if(n <= 0){

        }else{
            for(int i= 0; i< n; i++){
                if(checkArmstrong(i) == true && i < n){
                    System.out.println(i);
                }
            }
        }
    }

    public static boolean checkArmstrong(int n){
        int digitos = digitCount(n);
        int digito, sum = 0, copy = n;
        while (n != 0) {
            digito = n % 10;
            sum += Math.pow(digito, digitos);
            n /= 10;
        }
        if(sum == copy){
            return true;
        }
        return false;
    }

    public static int digitCount(int num){
        int digits = 0;
        while (num != 0) {
            num /= 10;
            digits++;
        }
        return digits;
    }
}