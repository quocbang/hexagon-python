class RepositoryError(Exception):
  def __init__(self, message: str, code: str):
        self.message = message
        self.code = code
  def __str__(self) -> str:
      return f'code: {self.code}, message: {self.message}'
    
class RecordNotFound(RepositoryError):
  pass