Console.WriteLine("Hello. Please enter your last name.");
string last_name = Console.ReadLine();

Console.WriteLine("What is the initial of your first name ?");
char initial = Convert.ToChar(Console.ReadLine());

Console.WriteLine($"Welcome to the course, {initial} {last_name}. We will watch your career with great interest.");
