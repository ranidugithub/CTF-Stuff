The Fibonacci sequence is a series of numbers where the next term is the sum of the previous two terms.

- Formula: fn=f(n-1)+f(n-2)
- The first two terms of the Fibonacci sequence is 0 followed by 1
- 0 1 1 2 3 5 8 13 21 34

we can add three static variables to take the input first.
![](images/Pasted%20image%2020240703201541.png)

using System;

public class Fibonacci
{
    static int p1 = 0, p2 = 1, p3;
    
    public static void Main(string[] args)
    {
        // Prompt the user to provide input
        Console.WriteLine("Please provide input value");
        
        // Read user input and convert it to an integer
        int count = Int32.Parse(Console.ReadLine());
        
        // Print the first two Fibonacci numbers
        Console.Write(p1 + " " + p2);
        
        // Loop to generate the Fibonacci sequence
        for (int i = 2; i < count; i++)
        {
            p3 = p1 + p2; // Calculate the next number
            Console.Write(" " + p3); // Print the next number
            p1 = p2; // Update p1
            p2 = p3; // Update p2
        }
        
        // Print a new line at the end
        Console.WriteLine();
    }
}

