from decouple import config

class EnvConfig:
    """Configuración general de la aplicación."""
    DB_HOST = config('DB_HOST')
    DB_PORT = config('DB_PORT')
    DB_DATABASE = config('DB_DATABASE')
    DB_USERNAME = config('DB_USERNAME')
    DB_PASSWORD = config('DB_PASSWORD')