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