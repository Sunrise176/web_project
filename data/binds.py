from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine1 = create_engine('sqlite:///db/blogs.db')  # Первая база
engine2 = create_engine('sqlite:///db/decks.db')  # Вторая база
Session1 = sessionmaker(bind=engine1)
Session2 = sessionmaker(bind=engine2)
session1 = Session1()
session2 = Session2()
Base = declarative_base()