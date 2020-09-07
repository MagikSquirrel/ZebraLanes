from models import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind = engine)
session = Session()

class GameDAO:

    def __init__(self, model):
        self.model = model    
    
    def get_all(self):
        return session.query(self.model).all()

    def get_by_id(self, id):
        return session.query(self.model).get(id)

    def create(self):
        game = Game()
        session.add(game)
        session.commit()

    def delete_by_id(self, id):
        session.query(Game).filter(Game.id==id).delete()
        session.commit()

    def join_game_by_id(self, gameid, bowlerid):
        game = self.get_by_id(gameid)
        bowler = bowler_dao.get_by_id(bowlerid)
        game.players.append(bowler)
        session.commit()

    def leave_game_by_id(self, gameid, bowlerid):
        game = get_by_id(gameid)
        bowler = bowler_dao.get_by_id(bowlerid)
        game.players.delete(bowler)
        session.commit()
        session.commit()
    
game_dao = GameDAO(Game)

class FrameDAO:

    def __init__(self, model):
        self.model = model    
    
    def get_all(self):
        return session.query(self.model).all()

    def get_all__id(self, id):
        return session.query(self.model).get(id)

    def get_all_by_game_and_bowler(self, gameid, bowlerid):
        return session.query(Frame).filter(Frame.game_id==gameid).filter(Frame.bowler_id==bowlerid).all()

    def updateRolls(self, frameid, rollA, rollB):
        session.query(Frame).filter(Frame.id==frameid).update({"rollA": rollA, "rollB": rollB})
        session.commit()

    def create(self, gameid, bowlerid, number, pinsA):
        frame = Frame(game_id=gameid, bowler_id=bowlerid, number=number, rollA=pinsA)
        session.add(frame)
        session.commit()
        return frame

frame_dao = FrameDAO(Frame)

class BowlerDAO:

    def __init__(self, model):
        self.model = model    
    
    def get_all(self):
        return session.query(self.model).all()

    def get_by_id(self, id):
        return session.query(self.model).get(id)

    def create(self, name):
        bowler = Bowler(name=name)
        session.add(bowler)
        session.commit()

    def delete_by_id(self, id):
        session.query(Bowler).filter(Bowler.id==id).delete()
        session.commit()
    
bowler_dao = BowlerDAO(Bowler)