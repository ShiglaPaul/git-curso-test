import os

#from app.settings import BASE_DIR
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))#la ruta del directorio de miproyecto
SQLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db/sqlite/db.sqlite3'),
    }
}

POSTGRESQL={
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER':'postgres',
        'PASSWORD':'leticia',
        'HOST':'localhost',
        'PORT':'5432'
    }
}