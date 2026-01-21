"""
Please implement these stub functions to match the documentation.
Make sure to implement tests in the tests directory.
"""


def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    is_valid = True
    
    if len(password) < 8:
        print("Password must be at least 8 characters long")
        is_valid = False
    
    found_upper = False
    for c in password:
        if c.isupper():
            found_upper = True
            break
    if not found_upper:
        print("Password must contain at least one uppercase letter")
        is_valid = False
    
    found_lower = False
    for c in password:
        if c.islower():
            found_lower = True
            break
    if not found_lower:
        print("Password must contain at least one lowercase letter")
        is_valid = False
    
    found_digit = False
    for c in password:
        if c.isdigit():
            found_digit = True
            break
    if not found_digit:
        print("Password must contain at least one digit")
        is_valid = False
    
    special_chars = '!@#$%^&*'
    found_special = False
    for c in password:
        if c in special_chars:
            found_special = True
            break
    if not found_special:
        print("Password must contain at least one special character (!@#$%^&*)")
        is_valid = False
    
    return is_valid
