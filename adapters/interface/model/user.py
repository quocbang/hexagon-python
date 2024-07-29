from pydantic import BaseModel


class CreateUserRequest(BaseModel):
  email: str
  full_name: str
  provider: str

class CreateUserResponse(BaseModel):
  id: str
  
class GetUserResponse(BaseModel):
  id: str
  email: str
  full_name: str
  provider: str