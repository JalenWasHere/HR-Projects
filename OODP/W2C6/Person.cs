public class Person
{
    public string FirstName;
    public string LastName;

    public Person(string firstName, string lastName)
    {
        FirstName = firstName;
        LastName = lastName;
    }

    public string Introduce() => $"I am {FirstName} {LastName}";
}