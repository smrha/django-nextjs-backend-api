from ninja import NinjaAPI, Schema

api = NinjaAPI()

class UserSchema(Schema):
    username: str
    is_authenticated: bool

@api.get("/hello")
def hello(request):
    return "Hello World!"

@api.get("/me", response=UserSchema)
def me(request):
    return request.user