def job_offer_template(first_name, last_name, job_title, annual_salary, starting_date):
    print(validate_name(first_name))


def validate_name(name):
    if not name.isalpha():
        return print("Name may only contain alphabetic characters")
    if len(name) < 2:
        return print("Name is too short")
    if len(name) > 10:
        return print("Name is too long")


job_offer_template("J@len", "Doe", "Web-Developer", 60000, "2024-01-01")
