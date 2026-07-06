import re
from datetime import datetime


def validate_name(name):
    """Validate contact name."""
    if not name.strip():
        raise ValueError("Name cannot be empty.")
    return name.strip()


def validate_phone(phone):
    """Validate phone number (7-15 digits, optional leading +)."""
    pattern = r"^\+?\d{7,15}$"

    if not re.match(pattern, phone):
        raise ValueError(
            "Invalid phone number. Use 7-15 digits (optional +)."
        )

    return phone


def validate_email(email):
    """Validate email address."""
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if not re.match(pattern, email):
        raise ValueError("Invalid email address.")

    return email


def validate_birthday(birthday):
    """Validate birthday in YYYY-MM-DD format."""
    try:
        datetime.strptime(birthday, "%Y-%m-%d")
        return birthday
    except ValueError:
        raise ValueError("Birthday must be in YYYY-MM-DD format.")


def validate_tags(tags):
    """
    Convert comma-separated tags into a list.
    Example:
    family, friend, office
    =>
    ['family', 'friend', 'office']
    """
    if not tags.strip():
        return []

    return [tag.strip() for tag in tags.split(",") if tag.strip()]