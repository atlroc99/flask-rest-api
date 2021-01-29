from flask import Flask, request, jsonify
from user import User
from db import create_table
app = Flask(__name__)

items = [
    {"name": "default_item", "price": 1234567}
]


@app.route('/items')
def get_items():
    return {"items": items}


@app.route('/item', methods=["POST"])
def method_name():
    new_item = request.get_json()
    print(request._get_current_object())
    app.logger.debug(f"data received: {new_item}")
    _exisitng_items = []
    for item in items:
        _exisitng_items.append(item["name"])

    app.logger.debug(f"existing items: {_exisitng_items}")
    if new_item["name"] not in _exisitng_items:
        app.logger.debug(f"adding new item {new_item} to the items list")
        items.append(new_item)
        return {"result": f"added new item {new_item}"}, 201

    return {"result": f"Item already exists: {new_item}"}, 200


@app.route('/register', methods=["POST"])
def register_user():
    data = request.get_json()
    _user = User.add_user(data)
    if _user:
        return jsonify({"user": f"User has been registerd {_user}"})


if __name__ == "__main__":
    app.debug = True
    app.port = 5000
    app.run()
