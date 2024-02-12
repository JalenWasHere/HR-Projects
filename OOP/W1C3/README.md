Learning goals:

- reading `double`s from the console
    - Note: depending on your system settings, you need to use either a period `.` or a comma `,`
- operator precedence
- implicit conversion (`int` to `string`)
- implicit conversion (`int` to `double`)
- explicit conversion (`double` to `int`)
- explicit conversion (`string` to `double`). You can use for example:
    - `Convert.ToDouble()`
    - `double.Parse()`
    - `double.TryParse()`

Write a program that asks the user for a temperature in Celsius. Convert this to Fahrenheit by multiplying by 1.8 and adding 32; then print the result. Also print the truncated result.

For example:

```
What is the temperature in Celsius?>9797 C = 206.6 FTruncated that is 206 F
```