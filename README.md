# django-task-app
to using local coment in setting.py

    'default': dj_database_url.config(
        default='postgres://postgres:postgres@localhost:5432/db_crud',
        conn_max_age=600,
    )
    
  create a database "db_crud" in postgres and remove the coments in
  
  # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': 'db_crud',
    #     'USER': 'postgres',
    #     'PASSWORD': 'root',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
# }
