Random random = new Random();

for (int i = 0; i < 10; i++)
{
    int min = 1;
    int max = 6;
    int diceRoll = random.Next(min, max + 1);
    Console.WriteLine(diceRoll);
}