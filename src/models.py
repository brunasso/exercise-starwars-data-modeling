import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum as PyEnum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    
    id = Column(Integer, primary_key=True)
    userName = Column(String(250), nullable=False)
    firstName = Column(String(250), nullable=False)
    lastName = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)

class Follower(Base):
    __tablename__ = 'follower'
    
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), ForeignKey('user.id'))
    author = relationship(User)

class Comment(Base):
    __tablename__ = 'comment'

    id = Column(Integer, primary_key=True)
    comment_text = Column(String(800))
    author_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    author = relationship(User)

class MediaType(PyEnum):
    REEL = "reel"
    PICTURE = "picture"
    STORY = "story"

class Media(Base):
    __tablename__ = 'media'

    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
