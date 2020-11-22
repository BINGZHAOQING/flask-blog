# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-16


from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api import ping, users,tokens
