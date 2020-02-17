from app import db, ma


# Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    items = db.relationship('Item', backref='user', lazy='dynamic')
    categories = db.relationship('Category', backref='user', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.id}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Item {self.id}>'


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Category {self.id}>'


# Schemas
class UserSchema(ma.Schema):
    class Meta:
        model = User
        fields = ('id',)


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class ItemSchema(ma.Schema):
    class Meta:
        model = Item
        fields = ('id', 'user_id')


item_schema = ItemSchema()
items_schema = ItemSchema(many=True)


class CategorySchema(ma.Schema):
    class Meta:
        model = Category
        fields = ('id', 'user_id')


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)
