from flask import Flask
from flask import make_response, jsonify, request
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
ma = Marshmallow(app)