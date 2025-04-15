import os
from hashlib import sha256

def hash_password(password, salt=None):
    """
    Takes in a password and returns the SHA256 hashed value for that specific password.
    Optionally, accepts a salt to improve security.
    
    Inputs:
        password: the password we want
        salt: a random string to add to the password before hashing for added security
    
    Outputs:
        the hashed form of the input password, and the salt used
    """
    if not salt:
        salt = os.urandom(16).hex()  # Generate a random salt if not provided
    salted_password = password + salt
    return sha256(salted_password.encode()).hexdigest(), salt


def store_user_login(email, password):
    """
    Hashes the password and stores the hashed password and salt in the dictionary.
    """
    password_hash, salt = hash_password(password)
    stored_logins[email] = (password_hash, salt)


def login(email, stored_logins, password_to_check):
    """
    Returns True if the hash of the password we are checking matches the one in stored_logins
    for a specific email. Otherwise, returns False.
    """
    stored_password_hash, stored_salt = stored_logins.get(email, (None, None))
    if stored_password_hash:
        # Check if the hash of the password to check matches the stored hash
        return stored_password_hash == hash_password(password_to_check, stored_salt)[0]
    return False


# Sample test data
stored_logins = {}

# Store some users
store_user_login("example@gmail.com", "password")
store_user_login("test@example.com", "securepass")

# Test login functionality
print(login("example@gmail.com", stored_logins, "password"))  # True
print(login("example@gmail.com", stored_logins, "wrongpass"))  # False
print(login("test@example.com", stored_logins, "securepass"))  # True
print(login("test@example.com", stored_logins, "password"))  # False
