from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)
db_file = "database.db"

# DB初期化（テーブル作成）
def init_db():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            text TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

@app.route("/", methods=["GET", "POST"])
def home():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["text"]
        c.execute("INSERT INTO posts (name, text) VALUES (?, ?)", (name, text))
        conn.commit()
    
    c.execute("SELECT name, text FROM posts ORDER BY id DESC")
    posts = [{"name": row[0], "text": row[1]} for row in c.fetchall()]
    conn.close()
    
    return render_template("index.html", posts=posts)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
