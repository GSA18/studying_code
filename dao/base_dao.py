from models.base_model import Base, BaseModel
from dao.session import Session


class BaseDao:
    def __init__(self, type_model) -> None:
        self.__type_model = type_model

    def save(self, model: BaseModel) -> BaseModel:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def read_by_id(self, id_: int) -> BaseModel:
        with Session() as session:
            result = session.query(self.__type_model).filter_by(id=id_).first()
        return result

    def read_all(self) -> list:
        with Session() as session:
            result = session.query(self.__type_model).all()
        return result

    def delete(self, model: BaseModel):
        with Session() as session:
            session.delete(model)
            session.commit()
