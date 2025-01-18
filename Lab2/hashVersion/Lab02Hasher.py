import json
import hashlib

def hash_password(password):
    """
    Convert a password string into a SHA-256 hash
    """
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Read the OG JSON
with open('Lab02.json', 'r') as file:
    data = json.load(file)

# Creating a new hashed JSON (passwords only)
new_data = {
    'username': data['username'],
    'hashed_password': [hash_password(pwd) for pwd in data['password']]
}

# WRITE IT!
with open('Lab02_hashed.json', 'w') as file:
    json.dump(new_data, file, indent=2)

print("Hashed JSON file has been created as 'Lab02_hashed.json'")