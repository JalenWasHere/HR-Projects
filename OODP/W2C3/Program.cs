using System;

class Program
{
    public static void Main()
    {
        Console.Write("Enter your first name: ");
        string firstName = Console.ReadLine();

        Console.Write("Enter your last name: ");
        string lastName = Console.ReadLine();

        DisplayName(firstName, lastName);
    }

    public static string Name(string firstName, string lastName) => $"{firstName} {lastName}";

    public static void DisplayName(string firstName, string lastName) => Console.WriteLine(Name(firstName, lastName));
}