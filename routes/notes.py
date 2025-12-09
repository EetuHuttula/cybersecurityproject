from flask import Blueprint, render_template, request, redirect, session
import sqlite3

notes_bp = Blueprint('notes', __name__)

@notes_bp.route("/new")
def new():
    return render_template("new.html")

@notes_bp.route("/send", methods=["POST"])
def send():
    # SQL INJECTION VULNERABILITY + CSRF vulnerability
    message = request.form["content"]
    user_id = session.get("user_id")
    if not user_id:
        return "Not logged in", 401
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    db.executescript("INSERT INTO notes (user_id, note) VALUES (" + str(user_id) + ", '" + message + "');")
    db.close()
    session["message"] = "Note sent successfully!"
    return redirect("/")

@notes_bp.route("/notes/<int:note_id>")
def note_detail(note_id):
    # BROKEN ACCESS CONTROL - no ownership check
    db = sqlite3.connect("database.db")
    db.row_factory = sqlite3.Row
    note = db.execute("""
        SELECT notes.id, notes.note, users.username 
        FROM notes 
        JOIN users ON notes.user_id = users.id 
        WHERE notes.id = ?;
    """, (note_id,)).fetchone()
    db.close()
    if note is None:
        return "Note not found", 404
    return render_template("note_detail.html", note=note)

# FIXED VERSION (commented):
# @notes_bp.route("/send", methods=["POST"])
# def send():
#     csrf_token = request.form.get('csrf_token')
#     if not csrf_token or csrf_token != session.get('csrf_token'):
#         return "CSRF token missing or invalid", 400
#     message = request.form["content"]
#     user_id = session.get("user_id")
#     if not user_id:
#         return "Not logged in", 401
#     db = sqlite3.connect("database.db")
#     db.execute("INSERT INTO notes (user_id, note) VALUES (?, ?);", (user_id, message))
#     db.commit()
#     db.close()
#     session["message"] = "Note sent successfully!"
#     return redirect("/")

# @notes_bp.route("/notes/<int:note_id>")
# def note_detail(note_id):
#     db = sqlite3.connect("database.db")
#     db.row_factory = sqlite3.Row
#     note = db.execute("""
#         SELECT notes.id, notes.note, users.username, notes.user_id
#         FROM notes 
#         JOIN users ON notes.user_id = users.id 
#         WHERE notes.id = ?;
#     """, (note_id,)).fetchone()
#     db.close()
#     if note is None:
#         return "Note not found", 404
#     if note['user_id'] != session.get("user_id") and session.get("role") != "admin":
#         return "Access denied", 403
#     return render_template("note_detail.html", note=note)
