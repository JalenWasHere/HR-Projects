string pin = "1234";
int attemptsLeft = 3;
bool success = false;
for (int i = attemptsLeft; attemptsLeft > 0 && !success;)
{
    Console.WriteLine("Enter your PIN");
    Console.WriteLine($"{attemptsLeft} attempts left");
    string enteredPin = Console.ReadLine()!;

    if (enteredPin == pin)
    {
        Console.WriteLine("Correct!");
        success = true;
    }
    else
    {
        attemptsLeft--;
    }
}

if (attemptsLeft == 0)
{
    Console.WriteLine("Your pass is confiscated.");
}