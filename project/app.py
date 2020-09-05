from flask import Flask
from flask import make_response, jsonify, request
from daos import *
from models import *
#from schemas import bowler_schema

app = Flask(__name__)

#bowler_schema = BowlerSchema()

#CRUD operations for GAMES
@app.route('/game/<gameid>', methods=['GET'])
def getGame(gameid):
    game = game_dao.get_by_id(gameid)
    if game is None:
        return make_error(400, 1, 'Does not exist', None)
    else:
        return jsonify(game.serialize())

@app.route('/game', methods=['POST'])
def createGame():
    game_dao.create()
    return jsonify({'result': True})

@app.route('/game/<gameid>', methods=['DELETE'])
def deleteGame(gameid):
    game_dao.delete_by_id(gameid)
    return jsonify({'result': True})

#CRUD operations for BOWLERS
@app.route('/bowlers', methods=["GET"])
def getBowlers():
    bowlers = bowler_dao.get_all()
    out=[]
    for bowler in bowlers:
        out.append(bowler.serialize())
    return jsonify(out)

@app.route('/bowler/<bowlerid>', methods=["GET"])
def getBowler(bowlerid):
    bowler = bowler_dao.get_by_id(bowlerid)
    if bowler is None:
        return make_error(400, 1, 'Does not exist', None)
    else:
        return jsonify(bowler.serialize())

@app.route('/bowler/<bowlername>', methods=['POST'])
def createBowler(bowlername):
    bowler_dao.create(bowlername)
    return jsonify({'result': True})

@app.route('/bowler/<bowlerid>', methods=['DELETE'])
def deleteBowler(bowlerid):
    bowler_dao.delete_by_id(bowlerid)
    return jsonify({'result': True})

@app.route('/roll', methods=["POST"])
def roll():
    
    req = request.get_json()

    ## store?
    print(req);

    res = make_response(jsonify({"message": "Collection created"}), 201)
    return res

# Generic method for error handling
def make_error(status_code, sub_code, message, action):
    response = jsonify({
        'status': status_code,
        'sub_code': sub_code,
        'message': message,
        'action': action
    })
    response.status_code = status_code
    return response

# Run the application
app.run()
