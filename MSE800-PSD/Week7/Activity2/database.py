import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "aquarium.db"


def create_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn


def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS aquarium_fish")
    cursor.execute("DROP TABLE IF EXISTS fish_categories")
    # One table stores fish categories, and one table stores each fish.
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS fish_categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category_name TEXT NOT NULL UNIQUE
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS aquarium_fish (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category_id INTEGER NOT NULL,
            color TEXT NOT NULL,
            appearance TEXT NOT NULL,
            size TEXT NOT NULL,
            age INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES fish_categories(id)
        )
        """
    )
    conn.commit()
    conn.close()
