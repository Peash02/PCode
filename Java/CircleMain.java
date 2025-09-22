import java.util.Scanner;

class Circle 
{
	double radius;
	final double pi = 3.14;
	public Circle()
	{
		radius = 0;
	}
	public Circle(double r)
	{
		radius = r;
	}
	
	public double area(double radius)
	{
		return pi*radius*radius;
	}
	
	public double circumference(double radius)
	{
		return 2*pi*radius;
	}
}
public class CircleMain
{
	public static void main(String[] args)
	{
		double a,c,r;
		
		Scanner s = new Scanner(System.in);
		
		System.out.print("Enter the Radius:");
		r = s.nextDouble();
		
		Circle C = new Circle();
		
		a = C.area(r);
		c = C.circumference(r);
		
		System.out.println("The Circumference is "+c);
		System.out.println("The Area is "+a);
		
		s.close();
	}
}