Learning goals:

- `switch` statements

Write a program which asks for a direction, either up, down, right or left (case should not matter). Use a `switch` statement in your solution.

Given an X and Y position which start at x = 0 and y = 0, if the user enters:

- _Up_ -> increase y by 1
- _Down_ -> reduce y by 1
- _Right_ -> increase x by 1
- _Left_ -> decrease x by 1  
  If any other value is given, print "Invalid direction", otherwise print the current `x and y` values.

Example 1:

```
What direction would you like to go?
Up
Down
Right
Left
>up
Current position
X:0, Y:1
```

```
Example 2:
What direction would you like to go?
Up
Down
Right
Left
>spin
Invalid direction
Current position
X:0, Y:0
```