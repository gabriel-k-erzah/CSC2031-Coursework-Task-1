
#######
def username(value):
    """Length: 3–30 characters
Allowed characters: letters and underscores
Disallow reserved usernames: admin, root, superuser"""
    value = str(value)

    # iteration over the string to check for only letters and underscores
    check_char(value)
    # check for if the string entered is in range
    check_length(value)
    #check for name attempt and log, incase user tries to elevate
    check_reserved(value)

    return value

#helper methods
def check_char(value):
    for char in value:
        if not (char.isalpha() or char == "_"):
            raise ValueError("Username can only contain letters and underscores.")

def check_length(value):
    if len(value) < 3 or len(value) > 30:
        raise ValueError("Username must be between 3 and 30 characters.")
    return value

def check_reserved(name):
    reserved = {"admin", "root", "superuser"}
    name = str(name).strip().lower()
    if name in reserved:
        raise ValueError("Attempt logged.")
    return name

########

########
def email():
"""Validate format
Restrict domains. Only allow emails ending in .edu, .ac.uk, and .org"""
    pass


def password():
"""Implement a robust password policy that enforces:

Minimum length: 12 characters
At least:
One uppercase letter
One lowercase letter
One digit
One special character
Must not contain the username or email
Must not contain whitespace characters (e.g., spaces)
Must not be a common password in the list:
password123
admin
123456
qwerty
letmein
welcome
iloveyou
abc123
monkey
football"""
    pass

def confirm_password():


def BioorCommentField():
    pass


#jinja2.exceptions.TemplateSyntaxError: Encountered unknown tag 'end'.
# Jinja was looking for the following tags: 'endblock'. The innermost
# block that needs to be closed is 'block'.
