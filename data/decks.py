import datetime
import sqlalchemy
from data.binds import Base
from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash


#class Deck(SqlAlchemyBase):
class Deck(Base):
    __tablename__ = 'decks'
    bind_key = 'decks_db'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ch1 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch2 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch3 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch4 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch5 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch6 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch7 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    ch8 = sqlalchemy.Column(sqlalchemy.String, nullable=False)
