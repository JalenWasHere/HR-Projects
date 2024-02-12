bool permission = false;

do
{
    Console.WriteLine("Really delete this file? (y/n)");
    string choice = Console.ReadLine()!;
    if (choice == "y")
    {
        permission = true;
    }

} while (permission == false);

Console.WriteLine("File deleted");