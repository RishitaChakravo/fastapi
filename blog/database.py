# Database connection file engine, session, base

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args=
                       {"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# this works as basic model or parent for other classes which inherit this base.
Base = declarative_base()