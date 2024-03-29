#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


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
        from models import storage
        res = []
        all_cities = storage.all(City)

        for city in all_cities.values():
            if city.state_id == self.id:
                res.append(city)

        return res
