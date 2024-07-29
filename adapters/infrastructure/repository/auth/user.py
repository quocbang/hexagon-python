from uuid import uuid1
from adapters.infrastructure.repository.error import RecordNotFound, RepositoryError
from domain.auth.entities import Auth, User

# TODO: implement connect with database later
class AuthImplement(Auth):
  def create_user(self, u: User) -> str:
    print(f"created user with email: {u.email}, name: {u.full_name}, provider:{u.provider}")
    return str(uuid1())
  
  def get_user_by_email(self, email: str) -> User:
    return User(id=str(uuid1()), email=email, full_name="Thong Quoc Bang", provider="google")
  
  def get_user_by_id(self, id: str) -> User:    
    if id == 'record_not_found':
      raise RecordNotFound(code="RECORD_NOT_FOUND", message="record not found")
    elif id == 'orm_error':
      raise RepositoryError(code="ORM_ERR_CODE", message="connection is closed")
  
    return User(id=id, email="bangthong@teqnological.asia", full_name="Thong Quoc Bang", provider="google")