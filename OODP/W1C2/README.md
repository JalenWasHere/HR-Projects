Learning goals:

- `int`; `double`
- `+`; `-`; `*`; `/`; `%`
- operator precedence
- `string` to `int` conversion. You can use for example:
    - `Convert.ToInt32()`
    - `int.Parse()`
    - `int.TryParse()`
- `int` to `string` conversion (you can use any method, such as `+` or `ToString()`)

Convert this Python code to C#:

```
age = int(input("What is your age? "))print("You are " + str(age) + ". That's old enough to program!")print("Last year you were " + str(age-1))print("Next year you will be " + str(age+1))print("At double your age you will be " + str(age*2))print("Next year, double your age will be " + str((age+1) * 2))print("Half your age is " + str(age / 2.0)) #This should be a double in C#print("Half your age (rounded down) is " + str(int(age / 2)))print("The last digit of your age is " + str(age % 10))
```