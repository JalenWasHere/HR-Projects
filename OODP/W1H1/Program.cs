Console.WriteLine("How many seconds?");
int totalSeconds = int.Parse(Console.ReadLine()!);

int hours = totalSeconds / 3600;
int minutes = (totalSeconds % 3600) / 60;
int remainingSeconds = totalSeconds % 60;

Console.WriteLine($"Hours: {hours}");
Console.WriteLine($"Minutes: {minutes}");
Console.WriteLine($"Seconds left: {remainingSeconds}");
