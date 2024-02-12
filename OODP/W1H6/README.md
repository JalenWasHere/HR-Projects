First ask the user for each cardinal direction (north, east, south and west) if these are valid directions (Y/N) to go to. Then print a compass with the valid directions.

Then ask the user for a bearing (angle), which is a number in degrees, so from 0 to 360 (exclusive). If the user gives a lower or higher number, normalize it so that it's within the range of 0 and 360. So for example, if the user gives 500, you should make it 140 (as 500 - 360 = 140).

With this (corrected) number, determine the direction: north, east, south or west:

- between 315 (exclusive) and 45 (inclusive) degrees: north
- between 45 (exclusive) and 135 (inclusive) degrees: east
- between 135 (exclusive) and 225 (inclusive) degrees: south
- between 225 (exclusive) and 315 (inclusive) degrees: west

Then print either _You are going north"_ (if the direction is valid) or _You can't go north_ (if it isn't).

Example outputs:
```
For each direction, input Y/N if it is valid.
North? Y/N
>Y
East? Y/N
>Y
South? Y/N
>Y
West? Y/N
>Y
Give a bearing (a number) for the direction in which you are going.
>700
From here you can go:
    N
    |
W---|---E
    |
    S
```
```
You are going north
For each direction, input Y/N if it is valid.
North? Y/N
>N
East? Y/N
>Y
South? Y/N
>Y
West? Y/N
>N
Give a bearing (a number) for the direction in which you are going.
>-100
From here you can go:

    |---E
    |
    S
```
You can't go west
