Console.WriteLine("What is your age?");
string first_age = Console.ReadLine()!;

Console.WriteLine("What is the age of the student next to you?");
string second_age = Console.ReadLine()!;

if (int.Parse(first_age) > int.Parse(second_age)){
    Console.WriteLine("You are older");
}
else if (int.Parse(first_age) == int.Parse(second_age)){
    Console.WriteLine("Your ages are equal");
} else {
    Console.WriteLine("You are younger");
}
