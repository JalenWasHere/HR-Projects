Create the three MCQs as shown below. Write them exactly as they are shown, and in that order.

Ask the user for an answer: A, B, C or D (uppercase or lowercase). The first two have one correct answer that each award one point. The last MCQ has two correct answers, which give one point if both have been answered correctly. You will need to figure out the correct answers yourself.  
If the user answers anything else than A, B, C or D (again, uppercase or lowercase), simply mark the answer as incorrect.

The three MCQs and an example of the user answering them:

```
Answer the following MCQs
Which of the following is NOT a valid type in C#?
A: bool
B: int
C: var
D: string
>a
What happens if you execute the following line C#?
int x = 1.23;
A: x will be 1.23
B: x will be 1
C: x will be 1.0
D: you will get a compiler error
>b
Consider the following line:double d = 1.23;
What are TWO ways to convert variable d to an int?
A: int i = (int)d;
B: int i = int(d)
C: int i = 0 + d
D: int i = Convert.ToInt32(d)
Your first answer:
>c
Your second answer:
>d
Your score: X out of 3.
```

Where _X out of 3_ is the amount of MCQs answered correctly. If all MCQs have been answered correctly, the final line would be:

```
Your score: X out of 3. Well done!
```