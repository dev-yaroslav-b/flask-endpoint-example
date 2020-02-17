from flask import jsonify, request
from app import db
from app.categories import bp
from app.errors import bad_request
from app.models import Category, User, categories_schema


@bp.route('/', methods=['GET'])
def index():
    categories = Category.query.all()
    result = categories_schema.dump(categories)
    response = {
        'data': result,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['GET'])
def user_categories(id):
    categories = Category.query.filter_by(user_id=id).first()
    result = categories_schema.dump(categories)
    response = {
        'data': result,
        'status_code': 200,
    }
    return jsonify(response)


@bp.route('/', methods=['POST'])
def create_category():
    data = request.get_json() or {}
    if 'user_id' not in data:
        return bad_request('Must include user id')
    if User.query.filter_by(id=data['user_id']).first() is None:
        return bad_request('User does not exist')
    category = Category(user_id=data['user_id'])
    db.session.add(category)
    db.session.commit()
    response = {
        'category': category.id,
        'status_code': 201
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['PUT'])
def update_category(id):
    data = request.get_json() or {}
    if 'user_id' not in data:
        return bad_request('Must include user id')
    if User.query.filter_by(id=data['user_id']).first() is None:
        return bad_request('User does not exist')
    category = Category.query.filter_by(id=id).first()
    category.user_id = data['user_id']
    db.session.add(category)
    db.session.commit()
    response = {
        'category': category.id,
        'status_code': 200
    }
    return jsonify(response)


@bp.route('/<int:id>', methods=['DELETE'])
def delete_category(id):
    category = Category.query.filter_by(id=id).first()
    if category is None:
        return bad_request('Category does not exist')

    db.session.delete(category)
    db.session.commit()
    response = {
        'category': category.id,
        'status_code': 200
    }
    return jsonify(response)
