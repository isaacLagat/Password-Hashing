import hashlib

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password


# example of password
password = "my_secure_password"
hashed_password = hash_password(password)
print("Hashed password:",hashed_password)