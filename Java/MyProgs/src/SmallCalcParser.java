/**
@version 1.0 2013-12-19
@author Sergey Botyan
*/
import java.util.Scanner;

public class SmallCalcParser
{
	public static void main(String[] args)	{

	    System.out.print("Insert expression: ");
		
		Scanner in = new Scanner(System.in);
		String expression = in.nextLine();
		in.close();
		
		//Check the sign type
		String sign_type = "";
		if (expression.contains("+"))
		{
			sign_type = "+";
		}
		else if (expression.contains("-"))
		{
			sign_type = "-";
		}
		else if (expression.contains("*"))
		{
			sign_type = "*";
		}		
		else if (expression.contains("/"))
		{
			sign_type = "/";
		}
		
		// Parse the expression
	    int sign_position = expression.indexOf(sign_type);
	    String sign = expression.substring(sign_position, sign_position + 1);
	    String number_first = expression.substring(0, sign_position);
	    String number_second = expression.substring(sign_position +1, expression.length());
	    int num_first = Integer.parseInt(number_first);
	    int num_second = Integer.parseInt(number_second);
	    
	    System.out.println(num_first);
	    System.out.println(sign);
	    System.out.println(num_second);
	    
	    int result = 0;
	    if (sign.equals("+"))
	    	{
	    	result = num_first + num_second;
	    	}
	    else if (sign.equals("-"))
	    	{
	    	result = num_first - num_second;
	    	}
	    else if (sign.equals("/"))
	    	{
	    	result = num_first / num_second;
	    	}
	    else if (sign.equals("*"))
	    	{
	    	result = num_first * num_second;
	    	}
	    
	    System.out.println("Result is: " + result);
	}

}

