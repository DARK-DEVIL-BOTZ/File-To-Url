# Modified By @DARK-Devil
import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
   MULTI_CLIENT = False
    API_ID = (19562731)
    API_HASH = (1667473e722f17eaa8ccbb98dc5f727d)
    BOT_TOKEN = (5505255276:AAFi2EviEpXs3cppv1EQscKQvGVl-hcShLg)
    SESSION_NAME = (file-to-url)
    SLEEP_THRESHOLD = (60)
    WORKERS = (4)
    BIN_CHANNEL = (-1001756916904)
    PORT = (8080)
    BIND_ADRESS = (0.0.0.0)
    PING_INTERVAL = (1200)
    OWNER_ID = (2071644540)
    NO_PORT = False
    APP_NAME = None
    OWNER_USERNAME = (DARKDevilV2)
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = FQDN', BIND_ADRESS)) if not ON_HEROKU
    else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = (mongodb+srv://malindunimsara2:darkdevil7@cluster0.q6m3t.mongodb.net/?retryWrites=true&w=majority)
    UPDATES_CHANNEL = (DarkDevilBotz)