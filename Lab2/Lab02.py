# 1. Name:
#      Benjamin Black
# 2. Assignment Name:
#      Lab 02: Authentication Program
# 3. Assignment Description:
#      This program reads username and password data from a JSON file,
#      prompts the user for credentials, and validates their authentication
# 4. What was the hardest part? Be as specific as possible.
#      I had tried messing around hashing the user info so that the data was not stored in plain text. Had never attempted something
#      like that before. I completed that idea but was not sure if it was appropriate to submit it with this assignment.
#      My code for this class has been getting pushed to my github @ https://github.com/Ether-G/CSE130 where I also post the messing around
#      code for this class.
# 5. How long did it take for you to complete the assignment?
#      Base assignment ~30 minutes, hashing version, ~1 hour.

import json

def load_credentials(filename):
    """
    Load credentials from a JSON file.
    Returns tuple of (usernames, passwords) lists or (None, None) if file cannot be opened.
    """
    try:
        with open(filename, 'r') as file:
            # Read JSON
            data = json.load(file)
            
            # Extract lists
            usernames = data['username']
            passwords = data['password']
            
            return usernames, passwords
            
    except (FileNotFoundError, json.JSONDecodeError, KeyError):
        print(f"Unable to open file {filename}.")
        return None, None

def authenticate_user(usernames, passwords):
    """
    Prompt for and validate user credentials.
    Returns True if authenticated, False otherwise.
    """
    if usernames is None or passwords is None:
        return False
        
    # Get credentialS
    username = input("Username: ")
    password = input("Password: ")
    
    # Check if the data even exists
    try:
        user_index = usernames.index(username)
        if passwords[user_index] == password:
            return True
    except ValueError:
        pass
    
    return False

def main():
    # Load creds from file
    usernames, passwords = load_credentials("Lab02.json")
    
    # Authenticate!!!
    if authenticate_user(usernames, passwords):
        print("You are authenticated!")
    else:
        print("You are not authorized to use the system.")

if __name__ == "__main__":
    main()