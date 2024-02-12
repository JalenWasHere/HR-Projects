int score = 0;

Console.WriteLine("Answer the following MCQs:");

Console.WriteLine("Which of the following is NOT a valid type in C#?");
Console.WriteLine("A: bool");
Console.WriteLine("B: int");
Console.WriteLine("C: var");
Console.WriteLine("D: string");
string answer1 = Console.ReadLine()?.ToUpper()!;
if (answer1 == "C")
{
    score++;
}

Console.WriteLine("What happens if you execute the following line C#?");
Console.WriteLine("int x = 1.23;");
Console.WriteLine("A: x will be 1.23");
Console.WriteLine("B: x will be 1");
Console.WriteLine("C: x will be 1.0");
Console.WriteLine("D: you will get a compiler error");
string answer2 = Console.ReadLine()?.ToUpper()!;
if (answer2 == "D")
{
    score++;
}

Console.WriteLine("Consider the following line:");
Console.WriteLine("double d = 1.23;");
Console.WriteLine("What are TWO ways to convert variable d to an int?");
Console.WriteLine("A: int i = (int)d;");
Console.WriteLine("B: int i = int(d)");
Console.WriteLine("C: int i = 0 + d");
Console.WriteLine("D: int i = Convert.ToInt32(d)");

Console.WriteLine("Your first answer:");
string answer3first = Console.ReadLine()?.ToUpper()!;
Console.WriteLine("Your second answer:");
string answer3second = Console.ReadLine()?.ToUpper()!;

if (answer3first == "A" && answer3second == "D" || answer3first == "D" && answer3second == "A")
{
    score++;
}

Console.WriteLine($"Your score: {score} out of 3{(score == 3 ? ". Well done!" : ".")}");