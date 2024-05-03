import time
import jwt

secret_jwt = "e9bf3fdd66a1dfc37de3d6aebb16fddb9f55b8b8f9780ff1c9b3acc9eb42904e7cb89eac3d8c92875566bcf363066420485006d2c6f6d2a8d515e3861fc2240f"


def create_token(token:str):
    return token

def encode_jwt(email:str, password:str):
    payload = {"email": email, "password": password, "exp": time.time() + (5*60)} # 5 min expiration time
    
    token =  jwt.encode(payload, secret_jwt, algorithm = "HS256")
    return create_token(token)

def decode_jwt(token:str):
    try:
        decoding = jwt.decode(token, secret_jwt, algorithm ="HS256")
        if time.time() <= decoding['exp']:
            return decoding
        else:
            return "Token is Expired!"
    except:
        return {}
