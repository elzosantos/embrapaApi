from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import JWTError, jws
from datetime import datetime, timedelta
from app.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
import json

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token():
    expire = (datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)).timestamp()
    encoded_jwt = jws.sign({"exp": expire}, SECRET_KEY, {'exp': ACCESS_TOKEN_EXPIRE_MINUTES}, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token):
    try:
        payload = jws.verify(token, SECRET_KEY, algorithms=ALGORITHM)
        payload = json.loads(payload)
        print(payload)
        expiration_time = datetime.fromtimestamp(int(payload["exp"]))
        print(expiration_time)

        if expiration_time < datetime.now():
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expirado. Por favor, solicite um novo token.",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido.",
            headers={"WWW-Authenticate": "Bearer"},
        )
