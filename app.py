from flask import Flask, jsonify, request
from book import Book
import os
import json

app = Flask(__name__)

stores = [{'name': 'my wonderful store', 'items': [{'name': 'my item', 'price': 15.99}]}, {'name': 'Bike Store',
                                                                                           'items': [{'name': 'scooter',
                                                                                                      'price': 35.99}, {
                                                                                                         'name': 'skate board',
                                                                                                         'price': 55.99},
                                                                                                     {
                                                                                                         'name': 'roller skater',
                                                                                                         'price': 65.99}]}]


@app.route('/index')
def index():
    return 'hello'


# POST /store data:{name}
@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()  # returns pythond dictionary
    # print(f'**** incoming request: data type: {type(data)}') print(json.dumps(data, indent=2))
    new_store = {
        "name": data.get('name'),
        "items": data.get('items')
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store_by_name(name):
    for store in stores:
        if store['name'].strip() == name.strip():
            return jsonify(store)

    return {'error': f'{name} does not exists'}, 403


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item data:{name, price}
@app.route('/store/<string:name>/item', methods=['POST'])
def add_item_to_store(name):
    # add item to the given store
    found_store = {}
    if name is None:
        return {"error": "store cannot be null or empty"}

    for store in stores:
        if store['name'].strip() == name:
            found_store = store
            break
    if found_store is None:
        return {"error": f"Store with {name} not found!"}

    store['items'].append(request.get_json())
    return jsonify({"stores": stores})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_by_store(name):
    if name is None:
        return {"error": f"store name cannot be empty or null - named received: {name}"}, 404
    for store in stores:
        if store['name'].strip() == name.strip():
            return jsonify({"items": store['items']}), 200
    return jsonify({"error": f"Store name: {name} NOT FOUND"}), 404


@app.route('/store/add-book', methods=['POST'])
def add_book():
    data = request.get_json()
    store = data.get('name')
    books = data.get('items')
    book = Book(store, books)

    book.get_book_info()
    return {"response": "success"}, 21200


@app.route('/store/<string:name>/items', methods=['PUT'])
def add_items_to_store(name):
    if name is None:
        return jsonify({"error": "Store name cannot be null or empty"})

    req_items = request.get_json()
    items = None
    for store in stores:
        if store.get('name').strip() == name.strip():
            items = store.get('items')
    for item in req_items:
        items.append(item)

    return jsonify({"store": store})


if __name__ == '__main__':
    app.run(port=4500, debug=True)
