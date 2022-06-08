# python modules
import jwt
import time
import datetime
import os

# local apps
from apps.Carmeil import Carmeil

def validate_token(token):
    secret = os.getenv('SECRET_CEFAS')
    try:
        decoded_data = jwt.decode(token_, key=secret, algorithms=['HS256',])
        if not is_expired(decoded_data['date']):
            raise Exception('Expired link')
        return decoded_data
    except Exception as e:
        return e

def is_expired(exp_date):
    exp_date = decoded_data['date'] + datetime.timedelta(days=3)
    today = datetime.date.today()
    if today < exp_date:
        # if today is earlier than exp_date
        return False
    else:
        return True

def generate_url(data):
    data['date'] = datetime.date.today().strftime('%d/%m/%Y')
    token = jwt.encode(
            payload = data,
            key = os.getenv('SECRET_CEFAS')
            )
    server = 'localhost:8000'
    url = F'{server}/validation/?token={token}'
    return url, token

def new_user_request(data, fields):
    '''
    In data['content'] you can add your message and type [url]
    instead of url with token that will be then added
    '''
    if not(data.get('email') and data.get('header')
            and data.get('subject') and data.get('content')):
        raise Exception('Data must have email, header, subject, and content')
    user_data = format_data(data, fields)
    url, token = generate_url(user_data)
    new_user_email = data['email']
    header = data['header']
    subject = data['subject']
    content = data['content']
    content = content.replace('[url]', url)
    try:
        email = Carmeil(
                'melet.chirino@gmail.com',#from
                new_user_email,#to
                subject,#subject
                '',
                header = header,
                content = content
                )
        email.send()
        return 'OK'
    except Exception as e:
        return e

def format_data(data, fields):
    print(F'original data = {data}')
    print(F'-----------\nOriginal keys= {data.keys()}')

    new_data = dict()
    for field in data:
        for field_ in fields:
            if field == field_:
                new_data[field] = data[field][0]
    print(F'\n-----\nnew_data = {new_data}')
    return new_data
