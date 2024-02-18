using System;

class Program
{
    public static void Main()
    {
        Square square1 = new Square(5);
        Console.WriteLine("Side: " + square1.Side);
        Console.WriteLine("Area: " + square1.Area());
        Console.WriteLine("Perimeter: " + square1.Perimeter());

        Square square2 = new Square(10);
        Console.WriteLine("Side: " + square2.Side);
        Console.WriteLine("Area: " + square2.Area());
        Console.WriteLine("Perimeter: " + square2.Perimeter());
    }
}

