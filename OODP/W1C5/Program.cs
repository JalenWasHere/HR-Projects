Console.WriteLine("What is the temperature of the water? (Celsius)");
string input_temp = Console.ReadLine()!;
float temperature = float.Parse(input_temp);

if (temperature <= 0) {
    Console.WriteLine($"At {temperature} degrees Celsius, the water will be solid");
} 
else if (temperature < 100)
{
    Console.WriteLine($"At {temperature} degrees Celsius, the water will be liquid");
}
else
{
    Console.WriteLine($"At {temperature} degrees Celsius, the water will be gas");
}
