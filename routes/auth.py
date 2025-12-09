from flask import Blueprint, render_template, request, redirect, session
import sqlite3

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    # IDENTIFICATION AND AUTHENTICATION FAILURES - no password verification
    if request.method == "POST":
        username = request.form["username"]
        db = sqlite3.connect("database.db")
        user = db.execute("SELECT id, role FROM users WHERE username = ?;", (username,)).fetchone()
        db.close()
        if user:
            session["user_id"] = user[0]
            session["username"] = username
            session["role"] = user[1]
            return redirect("/")
        else:
            return "User not found", 401
    return render_template("login.html")

@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

# FIXED VERSION (commented):
# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():
#     csrf_token = request.form.get('csrf_token')
#     if request.method == "POST":
#         if not csrf_token or csrf_token != session.get('csrf_token'):
#             return "CSRF token missing or invalid", 400
#         username = request.form["username"]
#         password = request.form["password"]
#         db = sqlite3.connect("database.db")
#         user = db.execute("SELECT id, role FROM users WHERE username = ? AND password = ?;", (username, password)).fetchone()
#         db.close()
#         if user:
#             session["user_id"] = user[0]
#             session["username"] = username
#             session["role"] = user[1]
#             return redirect("/")
#         else:
#             return "Invalid credentials", 401
#     return render_template("login.html")
