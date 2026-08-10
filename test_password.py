from backend.utils.security import verify_password

hashed_password = "$argon2id$v=19$m=65536,t=3,p=4$BalhjModBHF6Ro9+TI4AHA$2RqcEYRGtw+8yqccqmy0tC+ZTYpyo8ClEc3LFaVQnLA"

result = verify_password(
    "Chakri123",
    hashed_password
)

print("Verification:", result)