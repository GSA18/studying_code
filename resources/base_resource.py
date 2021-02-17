from typing import Type
from flask.globals import request
from sqlalchemy.sql.sqltypes import JSON
from dao.base_dao import BaseDao
from flask_restful import Resource


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, model_type: Type) -> None:
        self.__dao = dao
        self.__model_type = model_type

    def post(self):
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)
        return item, 201

    def get(self, id=None):
        if id:
            return self.__dao.read_by_id(id)
        return self.__dao.read_all()

    def put(self, id: int):
        data = request.json
        if data['id'] == id:
            item = self.__dao.read_by_id(id)
            for key, value in data.items():
                setattr(item, key, value)
            return self.__dao.save(item)
        return None, 404

    def delete(self, id):
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None, 204
