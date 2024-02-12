import re


def convert_to_seconds(time_str):
    if not isinstance(time_str, str):
        return float('inf')

    parts = re.split(r'[:.]', time_str)

    if len(parts) == 2:
        return float(parts[0]) * 60 + float(parts[1])
    elif len(parts) == 3:
        return int(parts[0]) * 60 + float(parts[1]) + float(parts[2]) / 1000
    else:
        return float('inf')


def insert_event_query(event) -> str:
    times_seconds = [convert_to_seconds(result['time']) for result in event["results"]]
    min_time_index = times_seconds.index(min(times_seconds))
    fastest_time = event["results"][min_time_index]

    return (f'''
        INSERT INTO events (name, track_id, date, distance, duration, laps, winner, category)
        VALUES
        (
            '{event["title"]}',
            {event["id"]},
            '{event["start"]}',
            '{event["distance"]["name"]}',
            '{fastest_time["time"]}',  -- Assuming duration is a placeholder; replace it with the actual value
            {event["distance"]["lapCount"]},
            {fastest_time["skater"]["id"]},    -- Assuming winner is a placeholder; replace it with the actual value
            '{event["category"]}'
        );
    ''')
