from dao.base_dao import BaseDao
from models.base_model import BaseModel


class BaseController:
    def __init__(self, dao: BaseDao) -> None:
        self.__dao = dao

    def create(self, model: object) -> object:
        return self.__dao.save(model)

    def delete(self, model: object):
        return self.__dao.delete(model)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def read_by_id(self, model: object) -> object:
        self.__dao.read_by_id(model.id)
        return self.__dao.save(model)
