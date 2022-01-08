from passlib.context import CryptContext
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
def get_password_hash(password):
    return bcrypt_context.hash(password)
print(get_password_hash('Test123#'))
print(get_password_hash('risoni'))