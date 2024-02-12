from datetime import datetime

def insert_skaters_query(skater) -> str:
    date_obj = datetime.strptime(skater["dateOfBirth"], "%Y-%m-%d").date()
    return (f'''
        INSERT INTO skaters (first_name, last_name, nationality, gender, date_of_birth)
        VALUES
        (
            '{skater["firstName"]}',
            '{skater["lastName"]}',
            '{skater["country"]}',
            '{skater["gender"]}',
            {date_obj}
        );
    ''')
