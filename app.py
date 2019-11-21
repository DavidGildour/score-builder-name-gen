from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.names import GenerateName

app = Flask(__name__)
api = Api(app)

cors = CORS(app, supports_credentials=True, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

api.add_resource(GenerateName, '/name')