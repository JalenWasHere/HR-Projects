List<string> tasks = new List<string>();

Console.WriteLine($"Amount of tasks: {tasks.Count}");
foreach (string task in tasks)
{
    Console.WriteLine(task);
}

tasks.Add("Mow lawn");
tasks.Add("Pay taxes");

Console.WriteLine($"Amount of tasks: {tasks.Count}");
foreach (string task in tasks)
{
    Console.WriteLine(task);
}

tasks.Remove("Mow lawn");
tasks.Add("Shopping");

Console.WriteLine($"Amount of tasks: {tasks.Count}");
foreach (string task in tasks)
{
    Console.WriteLine(task);
}