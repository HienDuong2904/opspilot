from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def hash_password(password: str) -> str:
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(hash_password: str, password: str) -> bool:
    ph = PasswordHasher()
    try:
        return ph.verify(hash=hash_password, password=password)
    except VerifyMismatchError:
        return False
