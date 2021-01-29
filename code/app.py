from flask import Flask, request
from flask_restful import Resource, Api, reqparse

import json

app = Flask(__name__)
api = Api(app)

items = []


# no need to do jsonify if we are using flask-restful
class Item(Resource):
    @classmethod
    def get(cls, name):
        print(f"items: {items}")
        # for item in items:
        #     if item['name'] == name:
        #         return item, 200
        # using filter - return a filter object
        # we can call list, next or other function on the filter object -> list((filter(lambda x: x['name'] == name,items)))

        # calling next on the filter object will return the next item, however if there is no more item in the list it will raise an erro
        # to void / prevent we return None, if no match found

        item = next(filter(lambda x: x['name'] == name, items), None)
        print(f"Item matched: {item}")
        if item:
            return item, 200

        return {"item": 'not found'}, 404

    @classmethod
    def post(cls, name):  # receives json payload and pass name
        exits = next(filter(lambda x: x['name'] == name, items), None) is not None
        if exits:
            return {"items": "item with the name {} already exists".format(name)}

        _new_item = request.get_json()
        items.append(_new_item)
        return _new_item, 201

    # @classmethod
    # def update(cls, name):
    #     data = request.get_json()
    #     if items:
    #         for item in items:
    #             if item.get('name') == name:
    #                 item = data
    #                 return items

    @classmethod
    def put(cls, name):
        json_data = request.get_json()
        print(f"json_data: {json_data}")
        req_parser = reqparse.RequestParser()
        print(req_parser)

        # here we are defining the fields we want to update
        req_parser.add_argument('price',
                                type=float,
                                required=True,
                                help="Required field it is")
        req_parser.add_argument("author",
                                type=str,
                                required=True,
                                help="Cannot process request, Author is a required field")

        parsed_args = req_parser.parse_args()
        existing_item = next(filter(lambda x: x['name'] == name, items), None)
        if existing_item is None:
            items.append(parsed_args)
        else:
            existing_item.update(parsed_args)

        return {
            "json_data": json_data,
            "msg": "parsing or extracting only the price and author key from the json payload",
            "args": parsed_args,
            "updated_item": existing_item
        }


class Items(Resource):
    @classmethod
    def get(cls):
        print(f"items: {items}")
        return {"items": items}, 200

    @classmethod
    def post(cls):
        print(f"invoked post request on items resource")
        data = request.get_json()
        print(f"data: {data}")
        print(f"data.items: {data['items']}")
        items.extend(data['items'])
        print(items)
        return {"items": items}, 200


api.add_resource(Item, '/api/item/<string:name>')  # localhost:5000/api/item/{itemName}
api.add_resource(Items, '/api/items')  # localhost:5000/api.items

if __name__ == '__main__':
    app.debug = True
    app.run()
