from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
import datetime
from config import Config

config = Config()

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')
# Create a password hashing context using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

ALGORITHM = 'HS256'
EXPIRES_IN=15


def create_jwt_token(username):
  expires = datetime.datetime.utcnow() + datetime.timedelta(minutes=EXPIRES_IN)
  data={ }
  data['username'] = username
  data['exp'] = expires
  auth_token = jwt.encode(data, config.SECRET_KEY, algorithm=ALGORITHM)
  return auth_token


def verify_jwt_token(token):
  """Verifies the JWT Token"""
  token_dict = jwt.decode(token, config.SECRET_KEY, algorithms=ALGORITHM)
  return token_dict.get("username")

#password
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)