#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


class State(BaseModel, Base):
    """Creates a State object"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')

    @property
    def cities(self):
        """Getter attribute that returns a list of city instances
            For use with Filestorage
        """
        res = []
        storage = FileStorage()
        all_cities = [(city) for city in storage.all(City).items()]

        for k, v in all_cities:
            res.append(str(v))

        return res
