# The @wraps function, imported from functools, is used in Python decorators to 
# ensure that the decorated function retains its original metadata, such as its 
# name, docstring, and other attributes. Without @wraps, the decorated function
# will lose these attributes and take on the metadata of the wrapper function 
# inside the decorator.
from functools import wraps

# Database for this software
users_db = {
    "edwin": "password123",  # username: password
    "joesph": "qwerty",
    "ideation axis": "letmein"
}

# Global variable to track logged-in user
current_user = None

# Authentication decorator
def login_required(func):
    """
    This decorator checks if the current_user is logged in
    before executing the decorated function. If the user is not logged in,
    it prints an error message and returns None. Otherwise, it executes the decorated
    """
    @wraps(func)
    def check_status(*args, **kwargs):
        if not current_user:
            print("You need to log in first!")
            return None
        return func(*args, **kwargs)
    return check_status

# Login Function
def login(username, password):
    """
    This functrion log the user in if the username and password are correct
    """
    global current_user
    if username in users_db and users_db[username] == password:
        current_user = username
        print(f"Login successful! Welcome, {username}.")
    else:
        print("Login failed! Incorrect username or password.")

# Logout Function
def logout():
    global current_user
    if current_user:
        print(f"Goodbye, {current_user}!")
        current_user = None
    else:
        print("No user is logged in.")

# Protected function that requires login
# The @login_required decorator is used on top of the view_sensitive_data()
# function to enforce access control. This means that only authenticated 
# users (those who are logged in) are allowed to access this function
@login_required
def view_sensitive_data():
    print(f"Ideation Axix Bank \n Ye'llo valued customer {current_user}: Your bank balance is GHC1500.")

# Usage Example
if __name__ == "__main__":
    # Trying to access sensitive data without login
    view_sensitive_data()
    
    # Logging in
    login("edwin", "password123")
    
    # Trying again after login
    view_sensitive_data()
    
    # Logging out
    logout()
    
    # Trying to access sensitive data after logout
    view_sensitive_data()
