import secrets
from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Save to a file
with open("secret.key", "wb") as f:
    f.write(key)

print("Key generated and saved to secret.key")