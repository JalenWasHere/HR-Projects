The assignment is to create a program that works a lot like an origami fortune teller. It asks the user to choose a color (red/blue/green/yellow) and a number from 1 to 8 (inclusive). Keep repeating the question if the user inputs an invalid answer.  
Add the chosen number and the color word length together, and calculate the remainder of dividing it by 4. You'll need this result to be between 1 to 4, but the remainder of dividing by 4 is between 0 and 3, therefore you'll need to add 1 to the remainder.

Put the resulting integer in a variable called `fortuneNumber`. The program does the rest for you.

For example:

```
Pick a color (red/blue/green/yellow):
>orange
Pick a color (red/blue/green/yellow):
>red
Pick a number (1-8):
>0
Pick a number (1-8):
>5
You will be loved and be happy!
```