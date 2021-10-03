import java.util.Scanner;
/**
 * This simple algorithm, sums the even digits in a user-inserted N value
 * For example:
 * User input: 36781
 * Output: 14
 * (Because 6+8 = 14)
 * @author Tiago Ribeiro (https://github.com/Tiago-S-Ribeiro)
 */
public class exercicioA {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        long number = input.nextLong();
        isTherePairs(number);
    }

    public static void isTherePairs(long number) {
        long helperVar, sum = 0;
        while (number > 0){
            helperVar = number % 10;
            if (helperVar % 2 == 0) {
                sum += helperVar;
                number = number / 10;
            }else{
                number = number / 10;
            }
        }
        System.out.println(sum);
    }
}