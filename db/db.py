import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")  # Add this in your .env and in Render secrets

conn = psycopg2.connect(DB_URL)
cur = conn.cursor()

def init_db():
    with conn:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS word_counts (
                word TEXT PRIMARY KEY,
                count INTEGER NOT NULL
            )
        """)

def increment_word(word: str) -> int:
    word = word.lower()
    with conn:
        cur.execute("SELECT count FROM word_counts WHERE word = %s", (word,))
        row = cur.fetchone()
        if row:
            count = row[0] + 1
            cur.execute("UPDATE word_counts SET count = %s WHERE word = %s", (count, word))
        else:
            count = 1
            cur.execute("INSERT INTO word_counts (word, count) VALUES (%s, %s)", (word, count))
    return count

def get_word_count(word: str) -> int:
    word = word.lower()
    with conn:
        cur.execute("SELECT count FROM word_counts WHERE word = %s", (word,))
        row = cur.fetchone()
        return row[0] if row else 0