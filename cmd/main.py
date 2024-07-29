from langchain_anthropic import ChatAnthropic
import uvicorn
from re import S
from typing import Optional
import typing
from fastapi import FastAPI, Response, status
from pydantic import BaseModel
from adapters.interface.user import user_router

app = FastAPI()

app.include_router(router=user_router, prefix="/api")

if __name__ == "__main__":    
    uvicorn.run(app, host="0.0.0.0", port=8000)