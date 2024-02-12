bool canGoNorth, canGoEast, canGoSouth, canGoWest;

Console.WriteLine("For each direction, input Y/N if it is valid.");
Console.Write("North? Y/N: ");
canGoNorth = Console.ReadLine()!.ToUpper() == "Y";
Console.Write("East? Y/N: ");
canGoEast = Console.ReadLine()!.ToUpper() == "Y";
Console.Write("South? Y/N: ");
canGoSouth = Console.ReadLine()!.ToUpper() == "Y";
Console.Write("West? Y/N: ");
canGoWest = Console.ReadLine()!.ToUpper() == "Y";

Console.WriteLine("Give a bearing (a number) for the direction in which you are going.");
int bearing = int.Parse(Console.ReadLine()!);

bearing = (bearing % 360 + 360) % 360;

string direction;
if ((bearing <= 45 && bearing >= 0) || (bearing > 315 && bearing < 360))
    direction = "north";
else if (bearing > 45 && bearing <= 135)
    direction = "east";
else if (bearing > 135 && bearing <= 225)
    direction = "south";
else
    direction = "west";

if (canGoNorth)
    Console.WriteLine("    N\n    |");

string compassMiddle = "    |";

if (canGoEast)
{
    if (!canGoWest)
    {
        compassMiddle = "    |---E";
    }
    else
    {
        compassMiddle =  "W---|---E";
    }
}

if (canGoWest && !canGoEast)
{
    compassMiddle =  "W---|";
}
Console.WriteLine(compassMiddle);
if (canGoSouth)
{
    Console.WriteLine("    |\n    S");
}

if (!canGoNorth && direction == "north")
{
    Console.WriteLine($"\nYou can't go {direction}");
}
else if (!canGoSouth && direction == "south")
{
    Console.WriteLine($"\nYou can't go {direction}");
}
else if (!canGoEast && direction == "east")
{
    Console.WriteLine($"\nYou can't go {direction}");
}
else if (!canGoWest && direction == "west")
{
    Console.WriteLine($"\nYou can't go {direction}");
}
else
{
    Console.WriteLine($"\nYou are going {direction}");
}
