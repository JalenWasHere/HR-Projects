from datetime import datetime


def job_offer_template(more_letters, type, first_name, last_name, job_title, annual_salary, starting_date,
                       with_feedback, feedback):
    if type == "Job Offer":
        if more_letters == "No":
            return
        if isinstance(validate_name(first_name), str):
            return print(validate_name(first_name))
        if isinstance(validate_name(last_name), str):
            return print(validate_name(last_name))
        if isinstance(validate_job_title(job_title), str):
            return print(validate_job_title(job_title))
        if isinstance(validate_salary(annual_salary), str):
            return print(validate_salary(annual_salary))
        if isinstance(validate_starting_date(starting_date), str):
            return print(validate_starting_date(starting_date))

        print('Here is the final letter to send:')
        print('Dear ' + first_name + ' ' + last_name + ',')
        print('After careful evaluation of your application for the '
              'position of ' + job_title + ', we are glad to offer you the job. Your salary will be '
              + str(annual_salary) + ' euro annually. Your start date will be on ' + starting_date + '. Please do not '
              'hesitate to contact us with any questions.')

        print('Sincerely,')
        print('HR Department of XYZ')


def rejection_template(more_letters, type, first_name, last_name, job_title, with_feedback, feedback):
    if type == "Rejection":
        if more_letters == "No":
            return
        if isinstance(validate_name(first_name), str):
            return print(validate_name(first_name))
        if isinstance(validate_name(last_name), str):
            return print(validate_name(last_name))
        if isinstance(validate_job_title(job_title), str):
            return print(validate_job_title(job_title))

        print('Here is the final letter to send:')
        print('Dear ' + first_name + ' ' + last_name + ',')
        print('After careful evaluation of your application for the '
              'position of ' + job_title + ', at this moment we have decided to proceed with another candidate.')
        if not with_feedback == "No":
            print("Here we would like to provide you our feedback about the interview.")
            print(feedback)
        print(
            "We wish you the best in finding your future desired career. Please do not hesitate to contact us with "
            "any questions. ")
        print('Sincerely,')
        print('HR Department of XYZ')


def validate_name(name):
    if not name.isalpha():
        return "Input error"
    if len(name) < 2:
        return "Input error"
    if len(name) > 10:
        return "Input error"

    return True


def validate_job_title(job_title):
    if len(job_title) < 10:
        return "Job title is too short"

    return True


def validate_salary(salary):
    salary = salary.replace(".", "")
    salary = salary.replace(",", ".")
    salary = float(salary)
    if not isinstance(salary, float):
        return "Salary is not a valid number"
    if salary < 20000.00 or salary > 80000.00:
        print("Salary must be within the 20k to 80k range")

    return True


def validate_starting_date(date):
    date = date.replace("-", "/")
    datetime_object = datetime.strptime(date, '%Y/%m/%d')
    if not datetime_object:
        return "Invalid date"
    if not datetime_object.year == 2021 or datetime_object.year == 2022:
        print("Invalid date")


job_offer_template("Yes", "Job Offer", "John", "Hartman", "Junior Python Programmer", "30.500,50", '2021-01-01', "No",
                   "No")
rejection_template("Yes", "Rejection", "David", "Johanson", "Junior C++ Programmer", "No", "No")
rejection_template("Yes", "Rejection", "David", "Chan", "Software Tester", "Yes",
                   "You have sufficient testing knowledge but we expected to see more experience in web application testing techniques.")
rejection_template("Yes", "Rejection", "A", "Doe", "Software Engineer", "No", "No")
