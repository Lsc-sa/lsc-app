import re

def evaluate_password_strength(password):
    """
    Evaluate password strength and return the strength level with suggestions.
    Levels: 'strong', 'average', 'easy'
    """
    length_criteria = len(password) >= 8
    upper_criteria = re.search(r'[A-Z]', password) is not None
    lower_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    suggestions = []
    if not length_criteria:
        suggestions.append("Password should be at least 8 characters long.")
    if not lower_criteria:
        suggestions.append("Include at least one lowercase letter.")
    if not upper_criteria:
        suggestions.append("Include at least one uppercase letter.")
    if not digit_criteria:
        suggestions.append("Include at least one digit.")
    if not special_criteria:
        suggestions.append("Include at least one special character (e.g., !@#$%^&*).")

    if length_criteria and upper_criteria and digit_criteria and special_criteria:
        return 'strong', []
    elif length_criteria and (upper_criteria or digit_criteria):
        return 'average', suggestions
    else:
        return 'weak', suggestions