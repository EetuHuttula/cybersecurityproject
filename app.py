from flask import Flask
#from os import getenv
import sqlite3
from dotenv import load_dotenv
# Import blueprints
from routes.main import main_bp
from routes.auth import auth_bp
from routes.notes import notes_bp
from routes.admin import admin_bp

#load_dotenv()

app = Flask(__name__)
# weak secret key
app.secret_key = "your_secret_key_here"

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(admin_bp)

if __name__ == "__main__":
    app.run(debug=True)

#
# Security misconfiguration
#
# FIXED VERSION (commented):
# app.secret_key = getenv("SECRET_KEY")
# if __name__ == "__main__":
#     app.run(debug=False)