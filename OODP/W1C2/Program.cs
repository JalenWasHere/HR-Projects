Console.WriteLine("What is your age?");
int age = Convert.ToInt32(Console.ReadLine());
Console.WriteLine($"You are {age}. That's old enough to program!");
Console.WriteLine($"Last year you were {age - 1}");
Console.WriteLine($"Next year you will be {age + 1}");
Console.WriteLine($"At double your age you will be {age * 2}");
Console.WriteLine($"Next year, double your age will be {(age + 1) * 2}");

Console.WriteLine($"Half your age is {age / 2.0}"); // This will be a double in C#
Console.WriteLine($"Half your age (rounded down) is {Convert.ToInt32(age / 2)}");
Console.WriteLine($"The last digit of your age is {age % 10}");
