import bleach

#---------------------------------------------------------username checks-----------------------------------------------

def username(value):
    """Length: 3–30 characters
    Allowed characters: letters and underscores
    Disallow reserved usernames: admin, root, superuser"""
    value = bleach.clean(str(value)).strip()

    # iteration over the string to check for only letters and underscores
    check_char(value)
    # check for if the string entered is in range
    check_length(value)
    #check for name attempt and log, incase user tries to elevate
    check_reserved(value)

    return value

#--------------------------------------------username helper methods----------------------------------------------------

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

#-----------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------email checks-------------------------------------------------

def email(value):
    """Validate format
    Restrict domains. Only allow emails ending in .edu, .ac.uk, and .org
    only check after the @
    """
    value = bleach.clean(str(value)).strip().lower()
    check_format(value)
    check_domain(value)
    return value

#------------------------------------------------------email helper methods----------------------------------------------

def check_format(value):
    #sanity check
    if "@" not in value or value.count("@") != 1:
        raise ValueError("Enter a valid email address.")
    return value

def check_domain(value):
    allowed_domains = ("edu", "ac.uk", "org")

    #only checks for the domain
    domain = value[value.index("@") + 1:]

    #manual check for domain
    match = False
    for allowed in allowed_domains:
        if domain.endswith(allowed):
            match = True
            break

    #output error for post @
    if not match:
        raise ValueError("Email must end with .edu, .ac.uk, or .org.")

    #output error message for pre @
    if not domain.replace(".", "").isalpha():
        raise ValueError("Invalid characters in email domain.")

    return value

#-----------------------------------------------------------------------------------------------------------------------


"""
def password():
Implement a robust password policy that enforces:

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
football
    pass
"""

#def confirm_password():

"""def confirm_password():
"""

"""def bio_or_comment():
    pass"""



#jinja2.exceptions.TemplateSyntaxError: Encountered unknown tag 'end'.
# Jinja was looking for the following tags: 'endblock'. The innermost
# block that needs to be closed is 'block'.
