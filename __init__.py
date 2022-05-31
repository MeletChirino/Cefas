import jwt
import time

if __name__ == "__main__":
    secret = 'my_secret'
    payload_ = {
            'user': 'Melet',
            'email': 'melet.chirino@gmail.com',
            'cedula': 1047478102,
            'expiration_date': time.time() + 2*60,
            }
    token = jwt.encode(
            payload = payload_,
            key = secret
            )
    print(f"token = {token}")
    decode_info = jwt.decode(token, key = secret, algorithms = ['HS256', ])
    print(f"info = {decode_info}")
    if decode_info['expiration_date'] < time.time():
        print("expired")
    else:
        print("well done")
