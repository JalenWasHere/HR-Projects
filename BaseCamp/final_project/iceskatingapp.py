import os
import sys
import json
import sqlite3

from skater import Skater
from track import Track
from event import Event

from queries.insert_event_query import insert_event_query
from queries.insert_skaters_query import insert_skaters_query
from queries.create_tables_query import create_tables_query
from functions.get_skaters import get_skaters

DATABASE_NAME = 'iceskatingapp.db'


def init():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    create_tables(cursor)
    insert_initial_data(cursor)
    # clear_database(cursor)

    conn.commit()
    conn.close()


def create_tables(cursor):
    for query in create_tables_query():
        cursor.execute(query)

def clear_database(cursor):

    try:
        # Get a list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        # Iterate through each table and delete all rows
        for table in tables:
            table_name = table[0]
            cursor.execute(f"DELETE FROM {table_name};")
            print(f"All rows deleted from table: {table_name}")

        print("Database cleared successfully.")

    except Exception as e:
        print(f"Error clearing database: {e}")


def insert_initial_data(cursor):
    with open('events.json', 'r') as file:
        events = json.load(file)
        skaters_list = get_skaters(events)
        for index, skater in enumerate(skaters_list):
            skaters_query = insert_skaters_query(skater)
            cursor.execute(skaters_query)
            print(f"[Skaters: {index}] Succesfully added row!")
        for index, event in enumerate(events):
            event_query = insert_event_query(event)
            cursor.execute(event_query)
            print(f"[Events: {index}] Succesfully added row!")



def main():
    init()


if __name__ == "__main__":
    main()
