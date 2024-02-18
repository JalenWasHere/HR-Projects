Console.WriteLine("What is the amount to pay?");
int totalAmount = int.Parse(Console.ReadLine()!);
int leftAmount = totalAmount;

while (leftAmount > 0)
{
    Console.WriteLine($"{leftAmount} left to pay");
    Console.WriteLine("Pay how much?");
    Console.WriteLine("1: 5");
    Console.WriteLine("2: 10");
    Console.WriteLine("3: 20");
    Console.WriteLine("4: 50");
    string choice = Console.ReadLine()!;

    if (choice == "1")
    {
        leftAmount -= 5;
    } else if (choice == "2")
    {
        leftAmount -= 10;
    } else if (choice == "3")
    {
        leftAmount -= 20;
    } else if (choice == "4")
    {
        leftAmount -= 50;
    }
}

if (leftAmount < 0)
{
    int overpaidtotalAmount = Math.Abs(leftAmount);
    Console.WriteLine($"You paid {overpaidtotalAmount} too much. Give a tip? y/n");
    
    string choice = Console.ReadLine()!;
    if (choice == "y")
    {
        Console.WriteLine($"You have paid {totalAmount + overpaidtotalAmount}");
    }
    else
    {
        Console.WriteLine($"You have paid {totalAmount}");

    }
}
else
{
    Console.WriteLine($"You have paid {totalAmount}");
}
