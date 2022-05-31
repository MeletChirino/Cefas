#django modules
from django.http import JsonResponse
#python modules
import os
import jwt

def validation(request):
    '''
    http://localhost:8000/validation/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ZHNkODkwIiwibmFtZSI6IkogQmFsdmluIiwiaWF0IjoxNTEzOTAyMiwid2lzaW4iOiJZYW5kZWwifQ.rr_uc-ebLpabO353a44PiPETwCFzb3X4O-3y9wGi57wj
    '''
    print(F'data = {request.GET}')
    token_ = request.GET['token']
    print(F'token = {token_}')
    secret = os.getenv('SECRET_CEFAS')
    decoded_data = jwt.decode(token_, key=secret, algorithms=['HS256',])
    '''
    Ahora debes validar la fecha de expiracion, si el link es valido redirige
    al usuario a un form donde de verdad se van a guardar los datos del usuario.
    '''
    return JsonResponse(decoded_data)

def generate_url(data):
    token = jwt.encode(
            payload = data,
            key = os.getenv('SECRET_CEFAS')
            )
    server = 'localhost:8000'
    url = F'{server}/validation/?token={token}'
    return url

def new_user_request(request):
    # esto deberia ser un formView en el que le pases datos de payload y luego
    # los mandas por email con carmeil.
    pass

