from requests import get
from requests import exceptions
def internetConnection():
    try:
        get('http://Google.com', timeout = 3)
        print('Connected')
    except exceptions.ConnectionError:
        print('not connected') 

internetConnection()