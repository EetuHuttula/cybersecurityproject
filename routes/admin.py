from flask import Blueprint, session, render_template

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/admin")
def admin():
    # BROKEN ACCESS CONTROL - no role check
    username = session.get('username', 'Unknown')
    return f"""
    <h1>Admin Page</h1>
    <p>Welcome, {username}! Here you can manage the application.</p>
    <p><a href="/">Back to Home</a></p>
    """

# FIXED VERSION (commented):
# @admin_bp.route("/admin")
# def admin():
#     if session.get("role") != "admin":
#         return "Access denied", 403
#     username = session.get('username', 'Unknown')
#     return f"""
#     <h1>Admin Page</h1>
#     <p>Welcome, {username}! Here you can manage the application.</p>
#     <p><a href="/">Back to Home</a></p>
#     """
