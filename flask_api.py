#-----------------------------------------------------
# Flash API, example usage of Flash_restful, random number generator
# Coded by AGM-GR
#-----------------------------------------------------

import random

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

class Home(Resource):
    def get(self):
        return jsonify({'service_name': 'FlashAPI Example', 'service_version': '1.0'})

class Status(Resource):
    def get(self):
        return jsonify({'status': 'ok'})

class Random(Resource):
    def get(self):
        randomNumber = random.uniform(0, 1)
        return jsonify({'number': randomNumber})

class RandomRange(Resource):
    def get(self, min, max):
        randomNumber = random.randint(min, max + 1)
        return jsonify({'number': randomNumber})

#API REST addresses
api.add_resource(Home, '/')
api.add_resource(Status, '/status')
api.add_resource(Random, '/random')
api.add_resource(RandomRange, '/random/<min>/<max>')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
