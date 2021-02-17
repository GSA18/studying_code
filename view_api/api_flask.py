import sys
sys.path.append('.')
from flask import Flask
from flask_restful import Api
from resources.product_pet_resource import Product_petResource

app = Flask(__name__)
api = Api(app)

api.add_resource(Product_petResource, '/product_pet', endpoint='product_pets')
api.add_resource(Product_petResource, '/product_pet/<int:id>', endpoint='product_pet')

@app.route('/')
def main():
    return 'Ta funcionando corretamente'


app.run(debug=True)
