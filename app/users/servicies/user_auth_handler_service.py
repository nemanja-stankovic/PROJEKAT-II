import time
from typing import Dict
import jwt
from app.config import settings

JWT_SUPER_USER_SECRET = settings.JWT_SUPER_USER_SECRET
JWT_CLASSIC_USER_SECRET = settings.JWT_CLASSIC_USER_SECRET

USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM

def signSuperUserJWT(user_id: str) -> Dict[str, str]:
    """
    It creates a JWT with a user_id, is_super_user, and expires field, and then signs it with the JWT_SUPER_USER_SECRET
    @param {str} user_id - The user's ID
    @returns A dictionary with a key of "access_token" and a value of the token.
    """
    payload = {
        "user_id": user_id,
        "is_super_user": "super_user",
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_SUPER_USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeSuperUserJWT(token: str) -> dict:
    """
    It decodes the token and returns the decoded token if the token has not expired, otherwise it returns an empty
    dictionary
    @param {str} token - The token to decode
    @returns A dictionary of the decoded token.
    """
    try:
        decoded_token = jwt.decode(token, JWT_SUPER_USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def signClassicUserJWT(user_id: str) -> Dict[str, str]:
    """
    It creates a JWT with a user_id, is_super_user, and expires claim, and signs it with the JWT_CLASSIC_USER_SECRET
    @param {str} user_id - The user's ID.
    @returns A dictionary with a key of "access_token" and a value of the token.
    """
    payload = {
        "user_id": user_id,
        "is_super_user": "super_user",
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, JWT_CLASSIC_USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeClassicUserJWT(token: str) -> dict:
    """
    It decodes the token and returns the decoded token if the token has not expired, otherwise it returns an empty
    dictionary
    @param {str} token - The token to decode
    @returns A dictionary of the decoded token.
    """
    try:
        decoded_token = jwt.decode(token, JWT_CLASSIC_USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}

def signJWT(user_id: str, role:str) -> Dict[str, str]:
    """
    It takes a user_id and role, and returns a JWT token that expires in 20 minutes
    @param {str} user_id - The user's ID
    @param {str} role - The role of the user. This is used to determine what the user can do.
    @returns A dictionary with a key of access_token and a value of the token.
    """
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    """
    It decodes the token and returns the decoded token if it's not expired, otherwise it returns an empty dictionary
    @param {str} token - The token to decode
    @returns A dictionary with the user's information.
    """
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}