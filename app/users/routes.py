from flask import jsonify, request

from app import db
from app.users import bp
from app.errors import bad_request
from app.models import User, Category, Item, users_schema, categories_schema, \
    items_schema


@bp.route('/', methods=['GET'])
def index():
    users = User.query.all()
    result = users_schema.dump(users)
    response = {
        'data': result,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['GET'])
def user_categories_items(id):
    categories = categories_schema.dump(Category.query.filter_by(user_id=id))
    items = items_schema.dump(Item.query.filter_by(user_id=id))
    response = {
        'categories': categories,
        'items': items,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'user_id' not in data:
        return bad_request('Must include user id')
    if User.query.filter_by(id=data['user_id']).first() is not None:
        return bad_request('User already exists')
    user = User(id=data['user_id'])
    db.session.add(user)
    db.session.commit()
    response = jsonify({'user': user.id})
    response.status_code = 201
    return response


@bp.route('/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.filter_by(id=id).first()
    if user is None:
        return bad_request('User does not exist')

    db.session.delete(user)
    db.session.commit()
    response = {
        'user': user.id,
        'status_code': 200
    }
    return jsonify(response)
