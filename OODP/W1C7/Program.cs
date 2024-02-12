Console.WriteLine("You have one chance to guess this six-letter word:Le..th");
Console.WriteLine("HINT: this word is used to find the LENGTH of a string!");
string answer = "Length";
string inputGuess = Console.ReadLine()!;

if (inputGuess == answer)
{
    Console.WriteLine("Correct!");
} else if (inputGuess != answer && string.Equals(inputGuess, answer, StringComparison.OrdinalIgnoreCase))
{
    Console.WriteLine("Kind of correct; the case was just wrong");
} else if (inputGuess.Length != answer.Length)
{
    Console.WriteLine("Incorrect! That is not even a six-letter word!");
}
else
{
    Console.WriteLine("Incorrect!");
}
