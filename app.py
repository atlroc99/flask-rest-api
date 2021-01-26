from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
items = [{'name': 'default', 'price': 999999}]


class Item(Resource):
    # @staticmethod
    def get(self, name):  # apply filter in here
        for item in items:
            if item['name'] == name:
                return item

    def post(self, name):

        pass


api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/student/jon

# if __name__ == '__main__':
# app.run(port=3000)
app.debug = True
app.run(port=3000, debug=True)
