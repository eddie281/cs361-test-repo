def check_pwd(password: str) -> bool:
    """
    Returns True if the password meets all the criteria:
    - Length between 8 and 20 characters
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one symbol from ~`!@#$%^&*()_+-=
    Otherwise returns False.
    """
    if not (8 <= len(password) <= 20):
        return False

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    allowed_symbols = "~`!@#$%^&*()_+-="
    has_symbol = any(c in allowed_symbols for c in password)

    return has_lower and has_upper and has_digit and has_symbol
