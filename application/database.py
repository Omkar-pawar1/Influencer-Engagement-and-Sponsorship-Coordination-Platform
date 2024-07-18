from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

engine=None
base=DeclarativeBase()
db=SQLAlchemy()