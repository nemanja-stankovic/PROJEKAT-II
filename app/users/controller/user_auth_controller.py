from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.users.servicies import decodeClassicUserJWT, decodeSuperUserJWT


class JWTSuperUserBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTSuperUserBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        If the token is valid, return the token. If not, raise an exception
        @param {Request} request - Request - The request object.
        @returns The token.
        """
        credentials: HTTPAuthorizationCredentials = await super(JWTSuperUserBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        raise HTTPException(status_code=403, detail="Invalid authorization code.")


    def verify_jwt(self, jwtoken: str) -> dict:
        """
        It takes a JWT token as a string, decodes it, and returns a dictionary with a key of "valid" and a value of True if
        the token is valid, and a key of "role" and a value of the role of the user if the token is valid
        @param {str} jwtoken - The JWT token that you want to verify.
        @returns A dictionary with a key of valid and a value of True or False.
        """
        try:
            payload = decodeSuperUserJWT(jwtoken)
        except:
            payload = None
        if payload:
            if payload.get("role") != None:
                return {"valid": True, "role" : payload["role"]}
        return {"valid": False}
class JWTClassicUserBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTClassicUserBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        """
        If the credentials are valid, return the credentials. If not, raise an exception
        @param {Request} request - The request object.
        @returns The token itself.
        """
        credentials: HTTPAuthorizationCredentials = await super(JWTClassicUserBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        """
        It takes a JWT token as a string, decodes it, and returns a dictionary with a key of "valid" and a value of True if
        the token is valid, and a key of "role" and a value of the role of the user if the token is valid
        @param {str} jwtoken - The JWT token to verify
        @returns A dictionary with a key of valid and a value of True or False.
        """
        try:
            payload = decodeClassicUserJWT(jwtoken)
        except:
            payload = None
        if payload:
            if payload.get("role") != None:
                return {"valid": True, "role" : payload["role"]}
        return {"valid": False}

# class JWTBearer(HTTPBearer):
#     def __init__(self, role:str, auto_error: bool = True):
#         super(JWTBearer, self).__init__(auto_error=auto_error)
#         self.role = role
#
#     async def __call__(self, request: Request):
#         credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
#         if credentials:
#             if not credentials.scheme == "Bearer":
#                 raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
#             payload = self.verify_jwt(credentials.credentials)
#             if not payload.get("valid"):
#                 raise HTTPException(status_code=403, detail="Invalid token or expired token.")
#             if payload.get("role") != self.role:
#                 raise HTTPException(status_code=403, detail="User with provided role is not permitted to access this "
#                                                             "route.")
#             return credentials.credentials
#         else:
#             raise HTTPException(status_code=403, detail="Invalid authorization code.")
#
#     def verify_jwt(self, jwtoken: str) -> dict:
#         is_token_valid: bool = False
#         try:
#             payload = decodeJWT(jwtoken)
#         except:
#             payload = None
#         if payload:
#             is_token_valid = True
#         return {"valid": is_token_valid, "role": payload["role"]}
