from dao.base_dao import BaseDao
from models.products_pet_model import ProductPet


class Product_pet_Dao(BaseDao):
    def __init__(self) -> None:
        super().__init__(ProductPet)
