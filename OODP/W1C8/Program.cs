using System;

public class Program
{
    static int X = 0;
    static int Y = 0;

    static void Main()
    {
        AskDirection();
        Console.WriteLine($"Current position\nX:{X}, Y:{Y}");
    }

    static void AskDirection()
    {
        Console.WriteLine("What direction would you like to go?");
        Console.WriteLine("Up");
        Console.WriteLine("Down");
        Console.WriteLine("Right");
        Console.WriteLine("Left");
        string direction = Console.ReadLine()!.Trim().ToUpper();

        switch (direction)
        {
            case "UP":
                Y += 1;
                break;
            case "DOWN":
                Y -= 1;
                break;
            case "RIGHT":
                X += 1;
                break;
            case "LEFT":
                X -= 1;
                break;
            default:
                Console.WriteLine("Invalid direction");
                break;
        }
    }
}