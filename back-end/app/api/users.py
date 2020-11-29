# encoding=utf-8
# __Author__: BingZhaoQing
# __Date__: 2020-11-21
import re

from app.api import bp
from flask import request, jsonify, url_for
from app.api.errors import bad_request
from app.api.auth import token_auth
from app.models import User
from app import db


# 用户的增、删(id)、改(id)、查(多个、单个需要id)

@bp.route('/users', methods=['POST'])
def create_user():
    '''注册一个新用户'''
    data = request.get_json()
    if not data:
        return bad_request('you need add data')
    message = {}
    # 查看传入的数据
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'please provide a valid username'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern, data.get('email', None)):
        message['email'] = 'please provide a valid email address'
    if 'password' not in data or not data.get('password', None):
        message['password'] = 'please provide a valid password'

    # 查看数据库
    if User.query.filter_by(username=data.get('username', None)).first():
        message['username'] = 'please use a different username'
    if User.query.filter_by(email=data.get('email', None)).first():
        message['email'] = 'please use a different email'

    if message:
        return bad_request(message)

    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    '''获取所有的用户,返回用户集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, 'api.get_users')
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    ''''''
    data = User.query.get_or_404(id).to_dict()
    return jsonify(data)


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    '''修改一个用户'''
    user = User.query.get_or_404(id)
    data = request.get_json()
    print('---data:', data)
    if not data:
        return bad_request('你需要添加数据')
    message = {}
    # 查看传入的数据
    if 'username' in data and not data.get('username', None):
        message['username'] = 'please provide a valid username'

    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' in data and not re.match(pattern, data.get('email', None)):
        message['email'] = 'please provide a valid email address'

        # 查看数据库
    if 'username' in data and data['username'] != user.username and User.query.filter_by(
            username=data['username']).first():
        message['username'] = 'please use a different username'
    if 'email' in data and data['email'] != user.email and User.query.filter_by(email=data['email']).first():
        message['email'] = 'please use a different email'

    if message:
        return bad_request(message)

    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())


@bp.route('/users/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_user():
    ''''''
    pass
