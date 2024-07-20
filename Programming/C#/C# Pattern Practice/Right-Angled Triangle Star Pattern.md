
First Lets code Right-Angled Triangle Star Pattern, Letter pattern, and number pattern using C#.

Lets talk about the logic here. since pattern is same and only character is changing logic for the all three codes will be the same.

so as the below image star pattern example, in the first row, we print one start. In the second row we print two stars and it continuous until fourth row..
![](Images/Pasted%20image%2020240720210443.png)

Below is the final code for the Right-Angled Triangle Star Pattern. Lets break it down.
![](Images/Pasted%20image%2020240720220536.png)

```
public class starPattern{
    public static void Main(string[]args)
    {
        ...
    }
}

```

- `public class starPattern`: This declares a public class named `starPattern`.
- `public static void Main(string[]args)`: This is the entry point of the program. When you run the program, the code inside the `Main` method gets executed.

```
int row, col, num;
```

- `int row, col, num;`: These are integer variables. `row` and `col` are used for the loop counters, and `num` will store the number entered by the user.

```
Console.WriteLine("Please enter the number : ");
num = Convert.ToInt32(Console.ReadLine());
```

- `Console.WriteLine("Please enter the number : ");`: This line prints a message asking the user to enter a number.
- `num = Convert.ToInt32(Console.ReadLine());`: This line reads the user input, converts it from a string to an integer, and stores it in the `num` variable.

```
for(row=1; row<=num; row++)
{
    for(col=1; col<=row; col++)
    {
        Console.Write("* ");
    }
    Console.WriteLine();
}
```

- `for(row=1; row<=num; row++)`: This outer loop runs from 1 to the number entered by the user (`num`). Each iteration of this loop represents a new row.
- `for(col=1; col<=row; col++)`: This inner loop runs from 1 to the current row number (`row`). Each iteration of this loop prints a single star followed by a space.
- `Console.Write("* ");`: This prints a star followed by a space.
- `Console.WriteLine();`: After the inner loop completes (i.e., all stars for the current row are printed), this line moves the cursor to the next line, starting a new row.

When you run the program, it:

1. Prompts the user to enter a number.
2. Reads the number entered by the user.
3. Uses nested loops to print a pattern of stars. The number of rows is equal to the number entered by the user, and each row contains one more star than the previous row.

This will be same for the Letter and numbers as below. just change the character.

![](Images/Pasted%20image%2020240720221209.png)

![](Images/Pasted%20image%2020240720221235.png)

