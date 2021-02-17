from typing import Type

from flask.globals import request
from dao.base_dao import BaseDao
from flask_restful import Resource

class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def post (self):
        data= request.json
        item= self.__model_type(**data)
        self.__dao.save(item)
        return item

