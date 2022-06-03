#django modules
from django.http import JsonResponse
#python modules
import os
import jwt
from apps.Cefas import validate_token

def validation(request):
    '''
    http://localhost:8000/validation/?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ZHNkODkwIiwibmFtZSI6IkogQmFsdmluIiwiaWF0IjoxNTEzOTAyMiwid2lzaW4iOiJZYW5kZWwifQ.rr_uc-ebLpabO353a44PiPETwCFzb3X4O-3y9wGi57wj
    '''

    print(F'data = {request.GET}')
    token_ = request.GET['token']
    print(F'token = {token_}')
    try:
        decoded_data = validate_token(token)

        #this is an interface of admin2
        new_user_form(data)
    except Exception as e:
        return e
