import os
import sqlite3
from pathlib import Path

from flask import Flask, jsonify, request

DB_PATH = os.getenv("DB_PATH", "cars.db")
PORT = int(os.getenv("PORT", "8000"))

app = Flask(__name__)


def init_db():
    db_file = Path(DB_PATH)
    if db_file.parent != Path("."):
        db_file.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS cars (
                plate TEXT PRIMARY KEY,
                car_type TEXT NOT NULL,
                year INTEGER NOT NULL CHECK(year >= 1886)
            )
            """
        )
        conn.commit()


def fetch_all_cars():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT plate, car_type, year FROM cars ORDER BY plate"
        ).fetchall()
    return [dict(row) for row in rows]


init_db()


@app.get("/")
def index():
    return jsonify(
        {
            "message": "Car Rental API is running",
            "endpoints": {
                "health": "GET /health",
                "list_cars": "GET /cars",
                "add_car": "POST /cars",
                "delete_car": "DELETE /cars/<plate>",
            },
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/cars")
def list_cars():
    return jsonify(fetch_all_cars())


@app.post("/cars")
def add_car():
    data = request.get_json(silent=True) or {}

    plate = str(data.get("plate", "")).strip().upper()
    car_type = str(data.get("car_type", "")).strip()
    year = data.get("year")

    if not plate or not car_type or year is None:
        return (
            jsonify({"error": "plate, car_type, and year are required"}),
            400,
        )

    try:
        year = int(year)
    except (TypeError, ValueError):
        return jsonify({"error": "year must be an integer"}), 400

    if year < 1886:
        return jsonify({"error": "year must be 1886 or later"}), 400

    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO cars (plate, car_type, year) VALUES (?, ?, ?)",
                (plate, car_type, year),
            )
            conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"error": "car with this plate already exists"}), 409

    return jsonify({"message": f"Car {plate} added"}), 201


@app.delete("/cars/<plate>")
def delete_car(plate):
    normalized_plate = plate.strip().upper()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.execute(
            "DELETE FROM cars WHERE plate = ?",
            (normalized_plate,),
        )
        conn.commit()

    if cursor.rowcount == 0:
        return jsonify({"error": "no car found with that plate"}), 404

    return jsonify({"message": f"Car {normalized_plate} removed"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
