from app.security.hashing import hash_password, verify_password

password = "Atlas123"

hashed = hash_password(password)

print("Hashed:", hashed)

print(
    verify_password(password, hashed)
)