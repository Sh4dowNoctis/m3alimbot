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
            CREATE TABLE IF NOT EXISTS pull_counts (
                name TEXT PRIMARY KEY,
                count INTEGER NOT NULL DEFAULT 0
            );
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
    
def get_pull(name):
    with conn:
        cur.execute("SELECT count FROM pull_counts WHERE name = %s", (name,))
        result = cur.fetchone()
        return result[0] if result else 0

def increment_pull(name):
    with conn:
        cur.execute("INSERT INTO pull_counts (name, count) VALUES (%s, 1) ON CONFLICT(name) DO UPDATE SET count = pull_counts.count + 1", (name,))

def reset_pulls():
    with conn:
        cur.execute("UPDATE pull_counts SET count = 0")