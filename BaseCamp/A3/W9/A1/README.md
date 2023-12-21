Create an application for a car park that has paid parking. The main functionality of this terminal application is to register incoming and departing cars (check-in and check-out) from a car park while it keeps track of the current capacity and calculates the owed parking fee when a car leaves the car park.

The classes that need to be programmed for this assignment are described below.

##### Class `CarParkingMachine`:

###### Attributes/Fields:

- `capacity` (int, default 10) - how many cars can be parked at the car park at the same time.
- `hourly_rate` (float, default 2.50) - used to calculate the parking fee.
- `parked_cars` (dict => key: license\_plate, value: ParkedCar object) - keeps track of which cars are currently in the car park

###### Methods:

- `init` (constructor) that receives the `capacity`, `hourly_rate` and sets the `parked_cars` dict as `empty`.
- `check_in` that receives the `license_plate` as `str`, the `check_in` as `datetime object` that the car is parked (optional, default = current time).
    - If the maximum capacity is reached it should return False and not check-in the car.
- `check_out` that receives the `license_plate` as `str` and returns the owed parking fee total
    - (by calling the `get_parking_fee method`).
    - should return a decimal number (float)
- `get_parking_fee` that receives the `license_plate` as `str` and calculates/returns the parking fee
    - (hourly\_rate \* whole parking hours rounded-up, with max of 24 hours).

  

##### Class `ParkedCar`:

###### Attributes/Fields:

- `license_plate` (str) - license plate of the car
- `check_in` (datetime) - datetime object of the time checked-in

###### Methods:

- `init` (constructor) that receives the license\_plate and check-in

  

###### Extra:

Additional research is required on how to handle datetime objects to calculate the difference between the check-in and check-out time and how to round-up in hours. Hint: import the datetime module (datetime and timedelta objects)

In order to test your class, use the provided unit test file and complete the test functions with your own code.

###### Default menu:

```
[I] Check-in car by license plate[O] Check-out car by license plate[Q] Quit program
```

  

###### Input example (check-in):

```
ILicense: AA-123-BQ
```

###### Output example (check-in - OK):

`License registered`

###### Output example (check-in - Capacity reached):

`Capacity reached!`

  

###### Input example (check-out):

```
ILicense: AA-123-BOLicense: AA-123-BQ
```

###### Output example (check-out - OK):

`Parking fee: 2.50 EUR`

###### Output example (check-out - Not found):

`License AA-321-B not found!`