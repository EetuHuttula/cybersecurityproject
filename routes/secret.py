import secrets
import string

def generate_csrf_token():
    """Generate a secure random CSRF token"""
    return secrets.token_urlsafe(32)

def validate_csrf_token(token_from_session, token_from_form):
    """Compare CSRF tokens using constant-time comparison"""
    if not token_from_session or not token_from_form:
        return False
    return secrets.compare_digest(token_from_session, token_from_form)

def set_csrf_token(session):
    """Generate and set CSRF token in session"""
    csrf_token = generate_csrf_token()
    session['csrf_token'] = csrf_token
    session.modified = True
    return csrf_token
