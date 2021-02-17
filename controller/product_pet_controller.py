from controller.base_controller import BaseController
from dao.product_pet_dao import Product_pet_Dao


class Product_pet_ctrl(BaseController):
    def __init__(self) -> None:
        self.__dao = Product_pet_Dao()
        super().__init__(self.__dao)
