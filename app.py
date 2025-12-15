from flask import Flask
import os
import sqlite3
from dotenv import load_dotenv
# Import blueprints
from routes.main import main_bp
from routes.auth import auth_bp
from routes.notes import notes_bp
from routes.admin import admin_bp

load_dotenv()

app = Flask(__name__)
# weak secret key
app.config['SECRET_KEY'] = 'super-secret-key-123'
app.config['DEBUG'] = True
# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(notes_bp)
app.register_blueprint(admin_bp)

@app.route("/error-test")
def error_test():
    x = 1 / 0 
    return "This will show us sensitive data"

if __name__ == "__main__":
    app.run(debug=True)

#
# Security misconfiguration
#
# FIXED VERSION (commented):
# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', os.urandom(32).hex())
# app.config['DEBUG'] = os.getenv('FLASK_ENV') == 'development'
# if __name__ == "__main__":
#     app.run(debug=False)