# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-22


from flask import jsonify, g
from app import db
from app.api import bp
from app.api.auth import basic_auth


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_jwt()
    db.session.commit()
    return jsonify({'token': token})

# @bp.route('/tokens', methods=['DELETE'])
# def revoke_token():
#     g.current_user.revoke_token()
#     db.session.commit()
#     return '', 204
