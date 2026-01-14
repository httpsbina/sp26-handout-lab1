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
    count = 0
    
    foundUpper = False
    foundLower = False
    foundDigit = False
    foundSpecial = False
    
    Digit = ['1','2','3','4','5','6','7','8','9','0']
    Special = ['!','@','#','$','%','^','&','*']

    for x in password:
        count += 1
        if x.islower():
            foundLower = True
        if x.isupper():
            foundUpper = True
        if x in Digit:
            foundDigit = True 
        if x in Special:
            foundSpecial = True
    if count >= 8:
        return True
    return False
