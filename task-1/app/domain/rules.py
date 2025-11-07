import bleach
from app.domain.logger import log_event


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
            # log then raise error
            log_event("warning", "Invalid username character", username=value, bad_char=ch)
            raise ValueError("Username can only contain letters and underscores.")


def check_length(value):
    if len(value) < 3 or len(value) > 30:
        # log then raise error
        log_event("warning", "Username length violation", username=value, length=len(value))
        raise ValueError("Username must be between 3 and 30 characters.")


def check_reserved(name):
    reserved = {"admin", "root", "superuser"}
    name = str(name).strip().lower()
    if name in reserved:
        #log then raise error
        log_event("warning", "Reserved username attempt", username=norm)
        raise ValueError("Attempt logged.")


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
    # sanity check
    if "@" not in value or value.count("@") != 1:
        # log then raise error
        log_event("warning", "Invalid email format", email=value)
        raise ValueError("Enter a valid email address.")
    return value


def check_domain(value):
    allowed_domains = ("edu", "ac.uk", "org")
    # only checks for the domain
    domain = value[value.index("@") + 1:]
    # manual check for domain
    match = False
    for allowed in allowed_domains:
        if domain.endswith(allowed):
            match = True
            break
    # output error for post @
    if not match:
        # log then raise error
        log_event("warning", "Disallowed email domain", email=value, domain=domain)
        raise ValueError("Email must end with .edu, .ac.uk, or .org.")

    # output error message for pre @
    if not domain.replace(".", "").isalpha():
        # log then raise error
        log_event("warning", "Dirty chars in email domain", email=value, domain=domain)
        raise ValueError("Invalid characters in email domain.")


#-----------------------------------------------------------------------------------------------------------------------

#-----------------------------------------password checks---------------------------------------------------------------
def password(value, *, username_value=None, email_value=None):
    """
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
  """
    value = bleach.clean(str(value)).strip()

    password_policy(value)
    no_username_or_email(value, username_value, email_value)
    whitespace(value)
    common_password(value)

    return value


#--------------------------------------------password helper methods----------------------------------------------------
def password_policy(value):
    # length check password must be longer than 12 characters
    if len(value) < 12:
        raise ValueError("Password must be at least 12 characters long.")

    #complexity check based off password policy
    if not (any(char.isupper() for char in value)
            and any(char.islower() for char in value)
            and any(char.isdigit() for char in value)):
        raise ValueError("Password must contain at least one uppercase letter, one lowercase letter, and one digit.")


def no_username_or_email(password_value, username_value, email_value):
    """checks that the password entered does not contain the username or email"""
    password_value = bleach.clean(str(password_value)).lower()
    username_value = bleach.clean(str(username_value)).lower()
    email_value = bleach.clean(str(email_value)).lower()

    # check if password contains username or email
    if username_value in password_value or email_value in password_value:
        raise ValueError("Password cannot contain username or email.")


def whitespace(value):
    """checks that the password entered does not contain whitespace characters"""
    if " " in value:
        raise ValueError("Password cannot contain whitespace characters.")


def common_password(value):
    """checks that the password entered is not a common password after cleaning"""
    value = bleach.clean(str(value)).lower()
    common_passswords = ["password123", "admin", "123456", "qwerty", "letmein", "welcome", "iloveyou", "abc123",
                         "monkey", "football"]

    if value in common_passswords:
        raise ValueError("Password is too common.")


#------------------------------------------- confirm password ----------------------------------------------------------
def confirm_password(password_entered, password_confirmation):
    """checks that the password entered matches the password confirmation"""
    if password_entered != password_confirmation:
        raise ValueError("Passwords do not match.")


def bio_or_comment(value):
    """an optional field to allow the user to tell them about themselves e.g courses studied, hobbies, etc.
    sanitisation checks will be done in the form:
    Ensure secure handling of user-generated content:
    Whitelist of safe HTML tags:
    <b> (bold)
    <i> (italic)
    <u> (underline)
    <em> (emphasis)
    <strong> (strong emphasis)
    <a> (anchor links — with safe attributes like href and title)
    <p> (paragraph)
    <ul>, <ol>, <li> (lists)
    Enable autoescaping if and where needed in Jinja2 templates
    Display sanitized bio content safely in the browser
    """
    if not value:
        return ""
    allowed_tags = ["b", "i", "u", "em", "strong", "a", "p", "ul", "ol", "li"]
    allowed_attrs = {"a": ["href", "title"]}

    # strip=True removes disallowed tags (not escape them just remove those bad tags entirely)
    sanitized = bleach.clean(str(value), tags=allowed_tags, attributes=allowed_attrs, strip=True)
    return sanitized
