#!/usr/bin/env python3
""" A script that implements an encryption on user password """

import bcrypt


def hash_password(password: str) -> bytes:
    """ encrypt password using bcrypt """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """ An is_valid function """
    return bcrypt.checkpw(password.encode(), hashed_password)
