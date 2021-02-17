

class BaseController:
    def __init__(self, dao: object) -> None:
        self.__dao = dao

    def create(self, model: object) -> object:
        self.__dao.save(model)
