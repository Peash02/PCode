package Java;
import java.util.Scanner;
public class Ass1
{
    public static void main(String[]args)
    {
        double weight_earth,weight_planet;
        
        Scanner s = new Scanner(System.in);
        
        System.out.print("Enter the cargo weight on Earth(in kg):");
        weight_earth = s.nextDouble();
        
        System.out.println("S.No \t Planet \t Relative Gravity");
        System.out.println("1 \t Mercury \t 0.38");
        System.out.println("2 \t Venus   \t 0.91");
        System.out.println("3 \t Mars   \t 0.38");
        System.out.println("4 \t Jupiter \t 2.34" );
        System.out.println("5 \t Saturn \t 1.06");
        System.out.println("6 \t Uranus \t 0.92");
        System.out.println("7 \t Neptune \t 1.19");
        System.out.print("Select a Destination Planet(1-7):");
        
        short x = s.nextShort();
        switch(x)
        {
            case 1:
                weight_planet = weight_earth * 0.38;
                System.out.print("The Cargo weight on Mercury will be:" + weight_planet +" kg");
                break;
            case 2:
                weight_planet = weight_earth * 0.91;
                System.out.print("The Cargo weight on Venus will be:" + weight_planet +" kg");
                break;
            case 3:
                weight_planet = weight_earth * 0.38;
                System.out.print("The Cargo weight on Mars will be:" + weight_planet +" kg");
                break;
            case 4:
                weight_planet = weight_earth * 2.34;
                System.out.print("The Cargo weight on Jupiter will be:" + weight_planet +" kg");
                break;
            case 5:
                weight_planet = weight_earth * 1.06;
                System.out.print("The Cargo weight on Saturn will be:" + weight_planet +" kg");
                break;
            case 6:
                weight_planet = weight_earth * 0.92;
                System.out.print("The Cargo weight on Uranus will be:" + weight_planet +" kg");
                break;
            case 7:
                weight_planet = weight_earth * 1.19;
                System.out.print("The Cargo weight on Neptune will be:" + weight_planet +" kg");
                break;
            default:
                System.out.print("Invalid Number Entered!");
        }
    s.close();
    }
}