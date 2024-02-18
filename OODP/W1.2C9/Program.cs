int attack = 50;
double critChance = 0.33;
int bossHP = 1000;

Random random = new Random();

while (bossHP > 0)
{
    Console.WriteLine($"Boss HP: {bossHP}");
    double randomValue = random.NextDouble();

    if (randomValue < critChance)
    {
        bossHP -= attack * 2;
        Console.WriteLine($"Damage: {attack * 2}");
    }
    else
    {
        bossHP -= attack;
        Console.WriteLine($"Damage: {attack}");
    }
}

Console.WriteLine("Boss defeated");
