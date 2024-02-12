Console.WriteLine("What is the temperature in Celsius?");
string input_celcius = Console.ReadLine();
double temp_celcius = 0;

if (double.TryParse(input_celcius, out double doubleValue))
{
    temp_celcius = doubleValue;
}
else
{
    Console.WriteLine("Invalid celcius format");
}

double temp_fahrenheit = (temp_celcius * 1.8) + 32;
Console.WriteLine($"${temp_celcius} C = {temp_fahrenheit} F");
Console.WriteLine($"Truncated that is {(int)Math.Floor(temp_fahrenheit)} F");
