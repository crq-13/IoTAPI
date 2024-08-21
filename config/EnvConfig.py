from decouple import config

class EnvConfig:
    """Configuración general de la aplicación."""
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')
    DB_DATABASE = config('DB_DATABASE')
    DB_USERNAME = config('DB_USERNAME')
    DB_PASSWORD = config('DB_PASSWORD')
    KEYS_SEARCH = config('KEYS_SEARCH')
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_BUCKET_NAME = config('AWS_BUCKET_NAME')
    AWS_BUCKET_REGION = config('AWS_BUCKET_REGION')