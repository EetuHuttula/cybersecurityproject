from flask import Flask
import sqlite3

# Import blueprints
from routes.main import main_bp
from routes.auth import auth_bp
from routes.notes import notes_bp
from routes.admin import admin_bp

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