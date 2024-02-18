Learning goals:

- creating objects from classes
- calling methods of objects

Create two `Square` objects; first with a `Side` of 5, then with a `Side` of 10.

For the first object, print the following in this order:

- the `Side`
- the result of calling the `Area` method
- the result of calling the `Perimeter` method

Then do the same for the other object.

So the output should be:  
_Side: 5  
Area: 25  
Perimeter: 20  
Side: 10  
Area: 100  
Perimeter: 40_

NOTE: the program already contains a class `Square`. You do not need to create it, just use it.

```csharp
class Square
{
    public int Side;
    public Square(int side)
    {
        this.Side = side;
    }
    public int Area() => this.Side * this.Side;
    public int Perimeter() => 4 * this.Side;
}
```