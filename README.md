
# ZebraLanes
This is a software coding challenge to implement a bowling scoring system that operates as a REST API. The decided to make this using Python and Flask as those have been a pair I've wanting to try and figured it would fit the requirements. As I stated before I had not actually made a REST API from scratch before, but have made extensive use of them. While my most proficient language would be Java I opted for Python since that is what you use in the back-end and would appreciate it. This was built using the following stack

 - Python 3.8
 - [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 - [SQLAlchemy](https://www.sqlalchemy.org/)
 - [Marshmallow](https://marshmallow.readthedocs.io/en/stable/)
 - [Postman](https://www.postman.com/)

The API has 3 major models that it works with

 - **Game** - Which is a list of frames and list of players.
 - **Frame** - Contains up to 2 rolls, there can be 10-12 of these in a game.
 - **Bowler** - Someone with a name who bowls by making calls to ```/roll```

The API supports the following calls
- GET '/game/&lt;gameid&gt;'
- POST '/game'
- DELETE '/game/&lt;gameid&gt;'
- POST '/game/join/&lt;gameid&gt;/&lt;bowlerid&gt;'
- DELETE '/game/leave/&lt;gameid&gt;/&lt;bowlerid&gt;'
- GET '/frames'
- GET '/bowlers'
- GET '/bowler/&lt;bowlerid&gt;'
- POST '/bowler/&lt;bowlername&gt;'
- DELETE '/bowler/&lt;bowlerid&gt;'
- POST '/roll/&lt;gameid&gt;/&lt;bowlerid&gt;/&lt;pins&gt;' 

Example Request
```http
http://localhost:5000/frames
```
Example Response
```json
[
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 1,
        "number": 1,
        "rollA": 10,
        "rollB": null,
        "score": 25
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 2,
        "number": 2,
        "rollA": 10,
        "rollB": null,
        "score": 19
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 3,
        "number": 3,
        "rollA": 5,
        "rollB": 3,
        "score": 8
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 4,
        "number": 4,
        "rollA": 4,
        "rollB": 3,
        "score": 7
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 5,
        "number": 5,
        "rollA": 10,
        "rollB": null,
        "score": 25
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 6,
        "number": 6,
        "rollA": 10,
        "rollB": null,
        "score": 19
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 7,
        "number": 7,
        "rollA": 5,
        "rollB": 5,
        "score": 10
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 8,
        "number": 8,
        "rollA": 4,
        "rollB": 2,
        "score": 6
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 9,
        "number": 9,
        "rollA": 10,
        "rollB": null,
        "score": 30
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 10,
        "number": 10,
        "rollA": 10,
        "rollB": null,
        "score": 30
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 11,
        "number": 11,
        "rollA": 10,
        "rollB": null,
        "score": 20
    },
    {
        "bowlerid": 1,
        "gameid": 1,
        "id": 12,
        "number": 12,
        "rollA": 10,
        "rollB": null,
        "score": 10
    }
]
```

Somethings that would have been nice to explore
 - Using Swagger for automatic API documentation
 - Making use of a service layer for business logic to separate it from the API logic.
 - Making a React UI to make use of the API.
 - Add the ability to 'correct' a frame score.
 - Make use of more python libraries to clean up things like serialization.
 - Adding unit tests
 - Enforcing multiple players to bowl in order
 - Instead of returning 200 OK for most calls, return data that would be useful for the next phase of the game.
 - 
