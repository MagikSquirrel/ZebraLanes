import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
 
ma = Marshmallow()
Base = declarative_base()

class Game(Base):
    __tablename__ = 'game'
    
    id = Column(Integer, primary_key=True)

    class Meta:
        fields = ('id')

    def serialize(self):
        return {"id": self.id}

class Frame(Base):
    __tablename__ = 'frame'
    
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    rollA_id = Column(Integer, ForeignKey('roll.id'))
    rollB_id = Column(Integer, ForeignKey('roll.id'))
 
class Roll(Base):
    __tablename__ = 'roll'
    
    id = Column(Integer, primary_key=True)
    pins = Column(Integer)

class Bowler(Base):
    __tablename__ = 'bowler'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    class Meta:
        fields = ('id','name')

    def serialize(self):
        return {"id": self.id,
                "name": self.name}

class GameSchema(ma.Schema):
    class Meta:
        model = Game

class FrameSchema(ma.Schema):
    class Meta:
        model = Frame

class RollSchema(ma.Schema):
    class Meta:
        model = Roll

class BowlerSchema(ma.Schema):
    class Meta:
        model = Bowler
 
# Create an engine that stores data in the local directory's db file.
engine = create_engine(
'sqlite:///zebraLanes.db',
connect_args={'check_same_thread': False}
)
 
# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
Base.metadata.create_all(engine)