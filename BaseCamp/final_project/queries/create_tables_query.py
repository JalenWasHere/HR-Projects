def create_tables_query():
    return [
        '''
            CREATE TABLE IF NOT EXISTS skaters (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                nationality TEXT,
                gender TEXT,
                date_of_birth DATE
                )
        ''',
        '''
            CREATE TABLE IF NOT EXISTS tracks (
                id INTEGER PRIMARY KEY,
                name TEXT,
                city TEXT,
                country TEXT,
                outdoor INTEGER,
                altitude INTEGER
                )
        ''',
        '''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY,
                name TEXT,
                track_id INTEGER,
                date DATE,
                distance INTEGER,
                duration REAL,
                laps INTEGER,
                winner TEXT,
                category TEXT
                )
        ''',
        '''
            CREATE TABLE IF NOT EXISTS event_skaters (
                event_id INTEGER,
                skater_id INTEGER,
                FOREIGN KEY (event_id) REFERENCES events (id),
                FOREIGN KEY (skater_id) REFERENCES skaters (id),
                PRIMARY KEY (event_id, skater_id)
            )
        '''
    ]
