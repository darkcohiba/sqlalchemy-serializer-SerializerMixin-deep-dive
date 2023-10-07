from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates, relationship

from config import db

# Models go here!

class Gladiator(db.Model, SerializerMixin):
    __tablename__ = 'gladiator_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    number_of_fights = db.Column(db.Integer)
    weapon = db.Column(db.String)
    # relationships
    fights_field = relationship('Fights', back_populates='gladiator_field', cascade = 'all, delete')


class Fights(db.Model, SerializerMixin):
    __tablename__ = 'fights_table'
    id = db.Column(db.Integer, primary_key=True)

    gladiator_id = db.Column(db.Integer, db.ForeignKey('gladiator_table.id'))
    # relationships

    gladiator_field = relationship('Gladiator', back_populates='fights_field')

    arena_id = db.Column(db.Integer, db.ForeignKey('arena_table.id'))
    # relationships
    arena_field = relationship('Arena', back_populates='fight_field')

    serialize_rules = ('-arena_field', '-gladiator_field')



class Arena(db.Model, SerializerMixin):
    __tablename__ = 'arena_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    location = db.Column(db.String)
    # relationships
    fight_field = relationship('Fights', back_populates='arena_field')