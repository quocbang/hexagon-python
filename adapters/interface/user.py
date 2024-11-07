from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from adapters.infrastructure.repository.auth.user import AuthImplement
from adapters.infrastructure.repository.error import RecordNotFound, RepositoryError
from adapters.interface.model.api import APIErrorResponse, APISuccessResponse
from adapters.interface.model.user import CreateUserRequest, CreateUserResponse, GetUserResponse
from domain.auth.entities import Auth, User


user_router = APIRouter(
  prefix="/users",
  tags=["auth"]
)

@user_router.post("", status_code=status.HTTP_200_OK)
def create_user(req: CreateUserRequest, auth: Annotated[AuthImplement, Depends(AuthImplement)]):
  u = User(email=req.email, full_name=req.full_name, provider=req.provider)
  id = auth.create_user(u)
  if not id:
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="can not create user")
  
  return JSONResponse(status_code=status.HTTP_200_OK, content=APISuccessResponse(message="OK", data=CreateUserResponse(id=u.id).__dict__).__dict__)  

@user_router.get("/{id}", status_code=status.HTTP_200_OK)
def get_user(id: str, auth: Annotated[AuthImplement, Depends(AuthImplement)]):
  try:    
    u = auth.get_user_by_id(id)    
    
    return JSONResponse(status_code=status.HTTP_200_OK, content=APISuccessResponse(message="OK", data=GetUserResponse(id= u.id,email=u.email, full_name=u.full_name, provider=u.provider).__dict__).__dict__)  
  except RepositoryError as err:
    resp_err = APIErrorResponse
    if isinstance(err, RecordNotFound):             
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=resp_err(status_code=err.code, message=err.message).__dict__)
        
    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=resp_err(status_code=err.code, message=err.message).__dict__)