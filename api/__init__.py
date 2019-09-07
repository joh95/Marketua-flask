from flask import Flask
from flask_cors import CORS
from flask_pymongo import PyMongo
from flask_restful import Api

from api.product.controller import Product
from api.product.controller import ProductList

app = Flask(__name__)

# Configure CORS
#cors = CORS(app,  origins=['http://localhost:8080'])

# Configure database
app.config["MONGO_URI"] = "mongodb://18.222.226.58:27017/marketua"
app.database = PyMongo(app)
app.product_collection = app.database.db.marketua

# Create api
api = Api(app)

api.add_resource(Product, '/product', '/<product_id>',methods=['GET', 'POST', 'PUT', 'DELETE'])
api.add_resource(ProductList, '/productlist', methods=['GET'])
