from flask_restful import fields, marshal_with
from dao.product_pet_dao import Product_pet_Dao
from models.products_pet_model import ProductPet
from resources.base_resource import BaseResource


class Product_petResource(BaseResource):
    fields = {
        "id": fields.Integer,
        "name": fields.String,
        "description": fields.String,
        "price": fields.Float,
        "weight": fields.Float
    }

    def __init__(self):
        self.__dao = Product_pet_Dao()
        self.__model_type = ProductPet
        super().__init__(self.__dao, self.__model_type)

    @marshal_with(fields)
    def post(self):
        return super().post()

    @marshal_with(fields)
    def get(self,id=None):
        return super().get(id)

    @marshal_with(fields)
    def put (self,id:int):
        return super().put(id)
    
    @marshal_with(fields)
    def delete(self, id:int):
        return super().delete(id)