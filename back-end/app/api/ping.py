# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-16

from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET', 'POST'])
def ping():
    return jsonify('Pong')
