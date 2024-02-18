Write a program that asks the user for an amount (`int`) that needs to be paid. Then keep giving the user the option to pay:

- 1: 5
- 2: 10
- 3: 20
- 4: 50

If the user gives any other answer, just repeat the question. Keep asking the user, until the amount is paid.

If the user has paid more than the amount, ask the user if they want to give the rest as a tip (y/n; uppercase or lowercase shouldn't matter). If the user gives any other answer, keep repeating the question. Then print the amount that was paid.

For example:

```
What is the amount to pay?
105

105 left to pay
Pay how much?
1: 5
2: 10
3: 20
4: 50
>2

95 left to pay
Pay how much?
1: 5
2: 10
3: 20
4: 50
>4

45 left to pay
Pay how much?
1: 5
2: 10
3: 20
4: 50
>4

You paid 5 too much. Give a tip? y/n
>y

You have paid 110
```

If the answer to the last question was _n_, then the final print would be:

```
You have paid 105
```