import os
import sys
from sqlalchemy import * #Column, ForeignKey, Integer, String, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import backref
 
ma = Marshmallow()
Base = declarative_base()

# Bridge table between Games and Bowlers
gameBowlers = Table('game_bowlers',
    Base.metadata,
    Column('game_id', Integer, ForeignKey('game.id')),
    Column('bowler_id', Integer, ForeignKey('bowler.id'))
)

class Game(Base):
    __tablename__ = 'game'
    
    id = Column(Integer, primary_key=True)
    players = relationship('Bowler', secondary=gameBowlers, backref=backref('games', lazy = 'dynamic'))

    class Meta:
        fields = ('id')

    def serialize(self):
        #TODO Make this an inline with lambda
        p=[]
        for bowler in self.players:
            p.append(bowler.serialize())
        return {"id": self.id, "players": p}

class Frame(Base):
    __tablename__ = 'frame'
    
    id = Column(Integer, primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'))
    bowler_id = Column(Integer, ForeignKey('bowler.id'))
    number = Column(Integer)
    rollA = Column(Integer)
    rollB = Column(Integer)
    score = Column(Integer)

    class Meta:
        fields = ('id')

    def serialize(self):
        return {"id": self.id,
                "gameid": self.game_id,
                "bowlerid": self.bowler_id,
                "number": self.number,
                "rollA": self.rollA,
                "rollB": self.rollB,
                "score": self.score}

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