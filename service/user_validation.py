
def name_valid(user_name):

    if not user_name:
        return False,"User name not be empty" 
    for char in user_name:
        if char.isdigit():
            return False ,"User name not be digit"

    return True ,"Success"

def age_valid(user_age):

    if not user_age:
        return False, "Age should not be empty"

    if not user_age.isnumeric():
        return False, "Age must be a number"
    
    age = int(user_age)  
    if age < 19 or age > 100:  
        return False, "Age must be between 19 and 100"
    
    return True, "Success"

def address_valid(user_address):

    if not user_address:
        return False ,"Address not empty "

    return True ,"Success"


def email_valid(user_email):

    if not user_email:
        return False, "Email cannot be empty"

    if not user_email.endswith("@yash.com"):
        return False, "Email must end with @yash.com"

    if '@' not in user_email or user_email.index('@') == 0:
        return False, "Email must contain a valid username before the '@' symbol"

    return True, "Success"

def phone_valid(user_phone_number):

    size=len(user_phone_number)
    if(size>10 or size<10):
        return False ,"Number should greater than 0 and smaller than 10 "
    if (user_phone_number.isnumeric()):
        return True ,"Success"

    return False ,"Check phone number"

def password_valid(user_password):

    valid=False
    special_char="!@#$%^&*()_-+="

    if len(user_password) < 8:
        return False ,"Length of password must be greater than 8"
    elif any(char.isupper() for char in user_password) and any(char.islower() for char in user_password) and any(char.isdigit() for char in user_password) and any (char in special_char for char in user_password):
        return True ,"Success"

    return False ,"check password"
