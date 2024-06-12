import random
import string

def generate_password():
    while True:
        password = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        
        if (any(c.islower() for c in password) and 
            any(c.isupper() for c in password) and 
            any(c.isdigit() for c in password)):
            
            if all(password.count(char) <= 3 for char in password):
                
                def has_sequential(s):
                    for i in range(len(s) - 3):
                        if s[i:i+4].isalpha() and ''.join(sorted(s[i:i+4])) in string.ascii_lowercase + string.ascii_uppercase:
                            return True
                        if s[i:i+4].isdigit() and ''.join(sorted(s[i:i+4])) in '0123456789':
                            return True
                    return False
                
                if not has_sequential(password):
                    return password

print(generate_password())

# Please create a password with the criteria given

# Have at least 10 characters
# Have upper and lowercase letters and at least one number
# Have no more than 3 repeated characters
# Have no more than 3 sequentials letters
# Have no more than 3 consecutive numbers
# Not contain any of your personal information
# Be different from your previous 5 passwords
# Not contain commonly used words
