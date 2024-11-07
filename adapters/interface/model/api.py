import typing


class APIErrorResponse:
  def __init__(self, status_code: int, message: str, info: typing.Union[typing.Any, None] = None):
    self.status_code = status_code
    self.message = message
    self.info = info
  
class APISuccessResponse:
  def __init__(self, message, data: typing.Any):
        self.message = message
        self.data = data

  def __str__(self):
      return self.message