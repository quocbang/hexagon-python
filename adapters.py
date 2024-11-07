from domain.auth.entities import Auth, User


class Server():  
  AuthRepo: Auth    
  
  def __init__(self, auth_impl):
    self.AuthRepo = auth_impl
  
def new_adapters():
  a = Auth()
  
  u = User(email="bangthong@teqnological.asia", full_name="Thong Quoc Bang", provider="google")
  id = a.create_user(u)
  
  
  userInfo = a.get_user_by_email()
  
  print(userInfo)
  print(id)