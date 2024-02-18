Learning goals:

- expression-bodied methods (`void` and non-`void`)

In this assignment you will create expression-bodied methods. These work the same as regular methods, but they are written differently: there are no curly brackets `{ }`; instead there is an arrow `=>` and the method is written all in one line. See for an example [here](https://learning.oreilly.com/library/view/programming-c-10/9781098117801/ch03.html#expression_bodied_method).

Write two expression-bodied methods: `Name` and `DisplayName`.

- `Name` takes two `string` parameters (the first and last name of a person), and returns a `string` with the full name of the person. For example: `Name("John", "Doe")` -> `"John Doe"`.
- `DisplayName` takes two `string` parameters (the first and last name of a person). It returns nothing, but prints the full name of the person. It should call `Name` to get the full name.

In the `Main`, ask the user for their first and last name. Then call `DisplayName`.