from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mysql+pymysql://root@localhost:3306/API"

engine = create_engine(URL_DATABASE, pool_size= 10, max_overflow= 30)

Sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind= engine)

Base = declarative_base()