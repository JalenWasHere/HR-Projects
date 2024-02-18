string color = "";
int number = 0;
while (color == "")
{
    Console.WriteLine("Pick a color (red/blue/green/yellow):");
    string input_color = Console.ReadLine()!;

    if (
        input_color == "red" 
        || input_color == "blue" 
        || input_color == "green" 
        || input_color == "yellow"
        )
    {
        color = input_color;
    }
}