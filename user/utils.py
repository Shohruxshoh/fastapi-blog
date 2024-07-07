import time

import jwt


def decodeJWT(token: str) -> dict:
    decoded_token = jwt.decode(token, '09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7',
                               algorithms=['HS256'])
    return decoded_token if decoded_token['exp'] >= time.time() else None
