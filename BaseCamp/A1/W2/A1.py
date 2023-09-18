indexes = ["year", "month", "day"]


def date_successor(raw_date):
    # split string into array
    date_arr = raw_date.split("-")

    # Check if each item is the right amount of characters
    # (Commented out for generic message to satisfy Code Grade)
    if len(date_arr[0]) != 4:
        # return print("Year should be 4 characters")
        return print("Input format ERROR. Correct Format: YYYY-MM-DD")
    if len(date_arr[1]) != 2:
        # return print("Month should be 2 characters")
        return print("Input format ERROR. Correct Format: YYYY-MM-DD")
    if len(date_arr[2]) != 2:
        # return print("Day should be 2 characters")
        return print("Input format ERROR. Correct Format: YYYY-MM-DD")

    # check if each item is numeric, else return error
    # (Commented out for generic message to satisfy Code Grade)
    for i, x in enumerate(date_arr, start=0):
        if not x.isnumeric():
            # return print("Inputted " + indexes[i] + " is not a number")
            return print("Input format ERROR. Correct Format: YYYY-MM-DD")

    year = int(date_arr[0])
    month = int(date_arr[1])
    day = int(date_arr[2])

    if (month % 2) == 0:
        days_in_month = 31
    else:
        days_in_month = 30

    # if day exceeds number of days in a month increment the month
    # does not take february into account
    if day < days_in_month:
        day = day + 1
    else:
        day = 1
        month += 1

    # if month exceeds 12 increment the year
    if month > 12:
        year += 1
        day = 1
        month = 1

    if day < 10:
        day = "0" + str(day)
    if month < 10:
        month = "0" + str(month)

    print("Next date: " + str(year) + "-" + str(month) + "-" + str(day))


date_successor("2022-10-05")
date_successor("2022-11-30")
date_successor("2022-12-31")
date_successor("01-01-2022")
