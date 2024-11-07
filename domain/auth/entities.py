from abc import ABC, abstractmethod
from typing import Optional
from pydantic import BaseModel

class User(BaseModel):    
  id: Optional[str]
  email: str
  full_name: str
  provider: str


class Auth:  
  @abstractmethod
  def create_user(u: User) -> str:
    pass
  
  @abstractmethod
  def get_user_by_email(email: str) -> User:
    pass
  
  @abstractmethod
  def get_user_by_id(id: str) -> User:
    pass