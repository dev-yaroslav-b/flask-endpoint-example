from flask import jsonify, request

from app import db
from app.items import bp
from app.errors import bad_request
from app.models import Item, User, items_schema


@bp.route('/', methods=['GET'])
def index():
    items = Item.query.all()
    result = items_schema.dump(items)
    response = {
        'data': result,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['GET'])
def user_items(id):
    items = Item.query.filter_by(user_id=id)
    result = items_schema.dump(items)
    response = {
        'data': result,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json() or {}
    if 'user_id' not in data:
        return bad_request('Must include user id')
    if User.query.filter_by(id=data['user_id']).first() is None:
        return bad_request('User does not exist')
    item = Item(user_id=data['user_id'])
    db.session.add(item)
    db.session.commit()
    response = jsonify({'item': item.id})
    response.status_code = 201
    return response


@bp.route('/<int:id>', methods=['PUT'])
def update_item(id):
    data = request.get_json() or {}
    if 'user_id' not in data:
        return bad_request('Must include user id')
    if User.query.filter_by(id=data['user_id']).first() is None:
        return bad_request('User does not exist')
    item = Item.query.filter_by(id=id).first()
    item.user_id = data['user_id']
    db.session.add(item)
    db.session.commit()
    response = {
        'item': item.id,
        'status_code': 200
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.filter_by(id=id).first()
    if item is None:
        return bad_request('Item does not exist')

    db.session.delete(item)
    db.session.commit()
    response = {
        'item': item.id,
        'status_code': 200
    }
    return jsonify(response)
