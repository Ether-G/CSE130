import json
import hashlib

def hash_password(password):
    """
    Convert a password string into a SHA-256 hash
    """
    # Encode the password as bytes and create the hash
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def load_credentials(filename):
    """
    Load credentials from a JSON file.
    Returns tuple of (usernames, hashed_passwords) lists or (None, None) if file cannot be opened.
    """
    try:
        with open(filename, 'r') as file:
            # Read JSON data and parse it
            data = json.load(file)
            
            # Extract username and password lists
            usernames = data['username']
            hashed_passwords = data['hashed_password']
            
            return usernames, hashed_passwords
            
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print(f"Unable to open file {filename}.")
        return None, None

def authenticate_user(usernames, hashed_passwords):
    """
    Prompt for and validate user credentials.
    Returns True if authenticated, False otherwise.
    """
    if usernames is None or hashed_passwords is None:
        return False
        
    # Get the creds like before
    username = input("Username: ")
    password = input("Password: ")
    
    # Hash the input password
    hashed_input = hash_password(password)
    
    # Check if username exists and if the now hashed password matches
    try:
        user_index = usernames.index(username)
        if hashed_passwords[user_index] == hashed_input:
            return True
    except ValueError:
        pass
    
    return False

def main():
    # Load Creds
    usernames, hashed_passwords = load_credentials("Lab02_hashed.json")
    
    # Authenticate!!!
    if authenticate_user(usernames, hashed_passwords):
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

if __name__ == "__main__":
    main()