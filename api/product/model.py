from bson.objectid import ObjectId
from flask import current_app

class Product():

    def get_all_products():
        try:
            data = current_app.cars_collection.find({})
        except Exception as e:
            print(e)
            data = None
        return list(data)


    def get_product_by_id(_id: str):
        try:
            data = current_app.product_collection.find_one({'_id': ObjectId(_id)})
        except Exception as e:
            print(e)
            data = None
        return data


    def save_product(product):
        try:
            product.pop('_id')
            product['sold'] = False
            current_app.product_collection.insert(product)
        except Exception as e:
            print(e)


    def update_product(product):
        try:
            query = {'_id': ObjectId(product.pop('_id'))}
            current_app.product_collection.update(query, {'$set': product}, upsert=False)
        except Exception as e:
            print(e)


    def delete_product(_id):
        try:
            current_app.product_collection.remove({'_id': ObjectId(_id)})
        except Exception as e:
            print(e)
