from typing import Type
from sqlalchemy.sql.expression import insert
from sqlalchemy.sql.sqltypes import Float, String
from models.base_model import BaseModel
from sqlalchemy import Column, Float
from sqlalchemy.orm import validates


class ProductPet(BaseModel):
    __tablename__ = 'product_pet'

    name = Column('name', String(length=100), nullable=False)
    description = Column('description', String(length=255), nullable=False)
    price = Column('price', Float(precision=2), nullable=False)
    weight = Column('weight', Float(precision=2), nullable=False)

    def __init__(self, name: str, description: str, price: float, weight: float) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.weight = weight

    @validates('name')
    def vali_name(self, key, name):
        if not isinstance(name, str):
            raise TypeError('Name must be of the type Str.')
        elif len(name) > 100:
            raise ValueError('Max name lenght is 100 chacteres.')
        elif not name.strip():
            raise ValueError("Name can't be empty.")
        return name

    @validates('description')
    def vali_description(self, key, description):
        if not isinstance(description, str):
            raise TypeError(description, str)
        elif len(description) > 100:
            raise ValueError('Max name lenght is 255 chacteres.')
        elif not description.strip():
            raise ValueError("Description cant't empty.")
        return description

    @validates('price')
    def vali_price(self, key, price):
        if not isinstance(price, float):
            raise TypeError('Price must be of the type Float.')
        return price

    @validates('weight')
    def vali_weight(self, key, weight):
        if not isinstance(weight, float):
            raise TypeError('Weight must be of the type Float.')
        return weight
