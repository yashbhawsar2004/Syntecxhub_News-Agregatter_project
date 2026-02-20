def save_to_json(articles, filename="news.json"):
    import json
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(articles, f, indent=4)


def save_to_sqlite(articles, db_name="news.db"):
    import sqlite3
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS news (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, source TEXT, date TEXT, url TEXT)"
    )

    for article in articles:
        cursor.execute(
            "INSERT INTO news (title, source, date, url) VALUES (?, ?, ?, ?)",
            (article["title"], article["source"], article["date"], article["url"])
        )

    conn.commit()
    conn.close()