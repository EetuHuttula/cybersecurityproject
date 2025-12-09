from flask import Blueprint, render_template, session
import sqlite3

main_bp = Blueprint('main', __name__)

@main_bp.route("/")
def index():
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    cur = db.execute("""
        SELECT notes.id, notes.note, users.username 
        FROM notes 
        JOIN users ON notes.user_id = users.id
    """)
    notes = cur.fetchall()
    user = session.get("username")
    db.close()
    message = session.pop("message", None)
    return render_template("index.html", notes=notes, message=message, user=user)
