from math import dist
from dotenv import dotenv_values


class db():
  host: str
  port:  int
  user: str
  password: str
  db_name: str

class Config():
  database: db 
  
def load_config() -> Config:  
  dict = dotenv_values(".env")
  
  print(dict)