For this assignment you are going to expand your carparking program to handle file reading and writing.

Two new additions need to be added to the existing program from week 09 which will be explained in depth below.

##### Extend Class `CarParkingMachine`:

###### Attributes/Fields:

- `id` (string) - to identify this machine.

###### Extra:

When initializing a car parking machine you should load all non checked-out cars (checked-in but not checked-out) from the log file for this specific machine (example 'North'). Be sure to not check-in these cars again (as this will create new log lines), but only load them in the car parking machine instance/object.

  

##### Class `CarParkingLogger`:

###### Info:

Create a new class named CarParkingLogger which contains (at least) a method to log a car check-in and a method to log a car check-out. The class should use an `id` to identify for which parking machine this logger is.  
Every check-in and check-out should write a line to a logfile named 'carparklog.txt' which is shared by all car parking machines. The lines should be written in a specific format as shown in the following examples:

###### Attributes/Fields:

- `id` (string) - to identify this machine.

###### Methods:

- `get_machine_fee_by_day` that receives the `car_parking_machine_id` as `str` (case-insensitive) and a `search_date` as `str` with format (DD-MM-YYYY). It should return the total parking fee for a specific car parking machine on a specific day rounded up to two decimals.
- `get_total_car_fee` that receives the `license_plate` as `str` and returns the total fee independent of the car parking machine used and should be rounded up to two decimals

###### Examples:

Car parking machine North with a parking fee rate of 2 euro per hour checks in a car with license\_plate SG-123-B on February 9 at 14:33:54 (hours, minutes, seconds)  
  
This should result in the following log line:  
`09-02-2022 14:33:54;cpm_name=North;license_plate=SG-123-B;action=check-in`

Car parking machine North checks the same car out at 16:50:02  
  
This should result in the following log line:  
`09-02-2022 16:50:02;cpm_name=North;license_plate=SG-123-B;action=check-out;parking_fee=6`  

###### Extra:

Hint: use the datetime module to modify your datetime to the correct format.

To test your code, use the test file from the assignment of week 09. **Make sure to use `os.getcwd()` to get the current absolute directory `sys.path[0]` will not work**