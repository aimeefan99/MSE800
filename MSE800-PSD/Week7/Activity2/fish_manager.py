from database import create_connection


def get_total_fish():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM aquarium_fish")
    total = cursor.fetchone()[0]
    conn.close()
    return total


def get_or_create_category(category_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM fish_categories WHERE category_name = ?",
        (category_name,),
    )
    row = cursor.fetchone()

    if row is None:
        cursor.execute(
            "INSERT INTO fish_categories (category_name) VALUES (?)",
            (category_name,),
        )
        conn.commit()
        category_id = cursor.lastrowid
    else:
        category_id = row[0]

    conn.close()
    return category_id


def add_fish(fish, capacity):
    total = get_total_fish()
    if total + 1 > capacity:
        print("Not enough space in the aquarium.")
        return False

    category_id = get_or_create_category(fish.category)
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO aquarium_fish (name, category_id, color, appearance, size, age)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (fish.name, category_id, fish.color, fish.appearance, fish.size, fish.age),
    )
    conn.commit()
    conn.close()
    return True


def view_fish():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT fish_categories.category_name, COUNT(aquarium_fish.id)
        FROM fish_categories
        LEFT JOIN aquarium_fish ON aquarium_fish.category_id = fish_categories.id
        GROUP BY fish_categories.id, fish_categories.category_name
        ORDER BY fish_categories.category_name
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows


def view_all_fish_details():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT aquarium_fish.name,
               fish_categories.category_name,
               aquarium_fish.color,
               aquarium_fish.appearance,
               aquarium_fish.size,
               aquarium_fish.age
        FROM aquarium_fish
        JOIN fish_categories ON aquarium_fish.category_id = fish_categories.id
        ORDER BY aquarium_fish.id
        """
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
