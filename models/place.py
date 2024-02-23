#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Table, Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', ForeignKey(
        'places.id'), nullable=False, primary_key=True),
    Column('amenity_id', ForeignKey(
        'amenities.id'), nullable=False, primary_key=True)
)


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship('Review', backref='place', cascade='all, delete')
    amenities = relationship(
        'Amenity', secondary=place_amenity, back_populates='places', viewonly=False)

    @property
    def reviews(self):
        """Returns a list of review instances"""
        storage = FileStorage
        reviews_list = [(review) for review in storage.all()
                        if review.place_id == review.id]
        return reviews_list

    @property
    def amenities(self):
        """Returns a list of amenity instances based on amenity_ids
            that contains all amenity.id linked to the Place
        """
        amenities_list = [(amenity_id)
                          for amenity_id in self.amenity_ids]
        return amenities_list

    @amenities.setter
    def amenities(self, amenity):
        """Handles append method for adding an Amenity.id
        to the attribute amenity_ids
        """
        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            self.amenity_ids.append(amenity.id)
