from flask import Blueprint, session

admin_bp = Blueprint('admin', __name__)

@admin_bp.route("/admin")
def admin():
    # BROKEN ACCESS CONTROL - no role check
    return """
    <h1>Admin Page</h1>
    <p>Welcome, admin! Here you can manage the application.</p>
    <p><a href="/">Back to Home</a></p>
    """

# FIXED VERSION (commented):
# @admin_bp.route("/admin")
# def admin():
#     if session.get("role") != "admin":
#         return "Access denied", 403
#     return """
#     <h1>Admin Page</h1>
#     <p>Welcome, admin! Here you can manage the application.</p>
#     <p><a href="/">Back to Home</a></p>
#     """
