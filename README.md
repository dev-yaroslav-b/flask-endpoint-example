# Simple flask endpoint example

### Routes:

#### Categories
`GET` all categories
```
/api/categories
```
`GET` items categories by user id
```
/api/categories/<id>
```
`POST` create category
```
/api/categories
```
`PUT` change category user_id
```
/api/categories/<id>
```
`DELETE` delete category
```
/api/categories/<id>
```

#### Items
`GET` all items
```
/api/items
```
`GET` all items by user id
```
/api/items/<id>
```
`POST` create item
```
/api/items
```
`PUT` change item user_id
```
/api/items/<id>
```
`DELETE` delete item
```
/api/items/<id>
```

#### Users
`GET` all users
```
/api/users
```
`GET` all items and categories by user id
```
/api/users/<id>
```
`POST` create user
```
/api/users
```
`DELETE` delete user
```
/api/users/<id>
```

### Installation:

Clone project:
```
git clone https://github.com/dev-yaroslav-b/flask_test_task.git
```
Create virtual environment:
```
virtualenv --python=python3.7 venv
```
Activate venv `source venv/bin/activate` and install requirements:
```
pip install -r requirements.txt
```
Export app `export FLASK_APP=shop.py` 

Initialize and migrate database `flask init db && flask db migrate && flask db upgrade`
and run `flask run` flask server 
