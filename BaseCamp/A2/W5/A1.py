import os
import sys

valid_lines = []
corrupt_lines = []

'''
The validate_data function will check the students.csv line by line for corrupt data.

- Valid lines should be added to the valid_lines list.
- Invalid lines should be added to the corrupt_lines list.

Example input: 0896801,Kari,Wilmore,1970-06-18,INF
This data is valid and the line should be added to the valid_lines list unchanged.

Example input: 0773226,Junette,Gur_ry,1995-12-05,
This data is invalid and the line should be added to the corrupt_lines list in the following format:

0773226,Junette,Gur_ry,1995-12-05, => INVALID DATA: ['0773226', 'Gur_ry', '']

In the above example the studentnumber does not start with '08' or '09',
the last name contains a special character and the student program is empty.

Don't forget to put the students.csv file in the same location as this file!
'''


def validate_data(line):
    invalid_values = []
    def append_invalid_line(array):
        corrupt_lines.append(line + ' => INVALID DATA: [' + array + ']')

    # todo destructuring
    values = line.split(",")
    student_nr = values[0]
    first_name = values[1]
    last_name = values[2]
    birth_date = values[3]
    study_program = values[4]

    if not validate_student_nr(student_nr):
        invalid_values.append("'" + student_nr + "'")
    if not validate_name(first_name):
        invalid_values.append("'" + first_name + "'")
    if not validate_name(last_name):
        invalid_values.append("'" + last_name + "'")
    if not validate_birth_date(birth_date):
        invalid_values.append("'" + birth_date + "'")
    if not validate_study_program(study_program):
        invalid_values.append("'" + study_program + "'")

    if not invalid_values:
        valid_lines.append(line)
    else:
        append_invalid_line(",".join(invalid_values))


def validate_student_nr(student_nr):
    if not student_nr:
        return False
    if not student_nr[0] == "0":
        return False
    if not student_nr[1] in ["8", "9"]:
        return False
    if not len(student_nr) == 7:
        return False

    return True


def validate_name(name):
    if not name.replace(' ', '').isalpha():
        return False
    else:
        return True


def validate_birth_date(birth_date):
    date_arr = birth_date.split("-")
    if len(date_arr[0]) != 4:
        return False
    if len(date_arr[1]) != 2:
        return False
    if len(date_arr[2]) != 2:
        return False

    for i in date_arr:
        if not i.isnumeric():
            return False

    year = int(date_arr[0])
    month = int(date_arr[1])
    day = int(date_arr[2])

    if day == 0 or day > 31:
        return False
    if month == 0 or month > 12:
        return False
    if year < 1960 or year > 2004:
        return False

    return True


def validate_study_program(study_program):
    if study_program not in ["INF", "TINF", "CMD", "AI"]:
        return False

    return True


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('...')
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))
    print('...')


if __name__ == "__main__":
    main('students.csv')
