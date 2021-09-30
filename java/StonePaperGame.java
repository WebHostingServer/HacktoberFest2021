package JavaQuestions;

import java.util.Random;
import java.util.Scanner;
public class StonePaperGame {
    public static void main(String[] args) {
        System.out.println("Welcome to stone paper scissors");
        System.out.println(" 0 stands for Rock \n 1 Stands for Paper \n 2 Stands for Scissors");
        System.out.println("Enter Your Number");
        Random rn = new Random();
        int RandomNumber = rn.nextInt(3);
        Scanner sc = new Scanner(System.in);
        int userInput = sc.nextInt();
        if (userInput<=2){
        System.out.println(userInput +"=>Your Choice");
        System.out.println(RandomNumber +"=>Computer Choice");
        if(RandomNumber == 0)
            switch (userInput) {
                case 0:
                    System.out.println("Draw");
                    break;
                case 1:
                    System.out.println("You Lose");
                    break;
                case 2:
                    System.out.println("You Win");
                    break;
        
        } else if (RandomNumber == 1)
            switch (userInput) {
                case 0:
                    System.out.println("You Win");
                    break;
                case 1:
                    System.out.println("Draw");
                    break;
                case 2:
                    System.out.println("You Lose");
            } else if (RandomNumber == 2)
                switch (userInput) {
                    case 0:
                        System.out.println("You Win");
                        break;
                    case 1:
                        System.out.println("You Lose");
                        break;
                    case 2:
                        System.out.println("Draw");
                }
        }  else
            System.out.println("Enter number from 0-2 ");
    }
}
