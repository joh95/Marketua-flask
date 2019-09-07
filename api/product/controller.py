from flask import jsonify
from flask_restful import Resource
from api.product.utils import encode_document

from api.product.model import Product 

class Product(Resource):

    def get(self, product_id: str):
        try:
            data = product.get_product_by_id(product_id)
            success = True
        except Exception as e:
            print(e)
            data = None
            success = False

        return jsonify({'success': success, 'data': encode_document(data)})

    def post(self):
        data = product_parse.parse_args()
        try:
            product.save_product(data)
            success = True
        except Exception as e:
            print(e)
            success = False

        return jsonify({'success': success, 'data': None})

    def put(self):
        data = product_parse.parse_args()
        try:
            product.update_product(data)
            success = True
        except Exception as e:
            print(e)
            success = False

        return jsonify({'success': success, 'data': None})

    def delete(self, product_id):
        try:
            product.delete_product(product_id)
            success = True
        except Exception as e:
            print(e)
            success = False

        return jsonify({'success': success, 'data': None})


class ProductList(Resource):

    def get(self):
        try:
            data = product.get_all_products()
            success = True
        except Exception as e:
            print(e)
            data = None
            success = False

        return jsonify({'success': success, 'data': encode_document(data)})