from flask import Flask
from flask import make_response, jsonify, request
from daos import *
from models import *

app = Flask(__name__)

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

#Join/Leave games
@app.route('/game/join/<gameid>/<bowlerid>', methods=['POST'])
def joinGame(gameid, bowlerid):
    game_dao.join_game_by_id(gameid, bowlerid)
    return jsonify({'result': True})

@app.route('/game/leave/<gameid>/<bowlerid>', methods=['DELETE'])
def leaveGame(gameid, bowlerid):
    game_dao.leave_game_by_id(gameid, bowlerid)
    return jsonify({'result': True})

#CRUD operations for FRAMES
@app.route('/frames', methods=["GET"])
def getAllFrames():
    frames = frame_dao.get_all()
    frames = calculateScores(frames)
    out=[]
    for frame in frames:
        out.append(frame.serialize())
    else:
        return jsonify(out)

#CRUD operations for BOWLERS
@app.route('/bowlers', methods=["GET"])
def getBowlers():
    bowlers = bowler_dao.get_all()
    #TODO Make this an inline with lambda
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

#CRUD operations for ROLLS
@app.route('/roll/<gameid>/<bowlerid>/<pins>', methods=["POST"])
def roll(gameid, bowlerid, pins):
    
    bowlersFrames = frame_dao.get_all_by_game_and_bowler(gameid, bowlerid)

    #What is the last frame?
    lastFrame = bowlersFrames[-1]

    #If we don't have a rollB, put the pins here.
    if lastFrame is not None and lastFrame.rollB is None:
        frame_dao.updateRolls(lastFrame.id, lastFrame.rollA, pins)
        return jsonify(lastFrame.serialize())
    
    #Otherwise we're a new frame
    nextNum = 1
    if lastFrame is not None:
        nextNum = lastFrame.number + 1
    lastFrame = frame_dao.create(gameid, bowlerid, nextNum, pins)

    return jsonify(lastFrame.serialize())

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

def calculateScores(frames):
    for i, frame in enumerate(frames):

        score = safeInt(frame.rollA)

        #strike
        if safeInt(frame.rollA) == 10:
            # look ahead 2 if we have it
            if len(frames) > i+2:
                next = frames[i+2]            
                score += next.rollA

            # look ahead 1 if we have it
            if len(frames) > i+1:
                next = frames[i+1]            
                score += next.rollA

        #spare
        elif safeInt(frame.rollA) + safeInt(frame.rollB) == 10:

            # look ahead 1 if we have it
            if len(frames) > i+1:
                next = frames[i+1]            
                score += next.rollA

        frame.score = score

    return frames

# to avoid None type exceptions
def safeInt(int):
    if int is None:
        return 0
    return int
    

# Run the application
app.run()
