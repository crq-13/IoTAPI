from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config.EnvConfig import EnvConfig


user = EnvConfig.DB_USERNAME
pwd = EnvConfig.DB_PASSWORD
host = EnvConfig.DB_HOST
namedb = EnvConfig.DB_DATABASE
port = EnvConfig.DB_PORT


# url to conect to the databse sioma_app
database_url = f"mysql+pymysql://{user}:{pwd}@" \
    f"{host}:{port}/{namedb}"

# create the engine
engine = create_engine(database_url, echo=True)

# create a session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# create the base
Base = declarative_base()
