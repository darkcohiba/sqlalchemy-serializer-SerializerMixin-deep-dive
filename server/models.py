from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import validates, relationship

from config import db

# Models go here!

class Projects(db.Model, SerializerMixin):
    __tablename__ = 'projects_table'
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String, nullable = False)
    scope = db.Column(db.String)
    budget = db.Column(db.Integer)
    # relationships
    task_relationship_field = relationship('Tasks', back_populates='project_relationship_field', cascade = 'all, delete')


class Tasks(db.Model, SerializerMixin):
    __tablename__ = 'tasks_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    cost = db.Column(db.Integer)
    description = db.Column(db.String)

    project_id = db.Column(db.Integer, db.ForeignKey('projects_table.id'))
    # corresseponding relationship
    project_relationship_field = relationship('Projects', back_populates='task_relationship_field')

    engineer_id = db.Column(db.Integer, db.ForeignKey('engineers_table.id'))
    # relationships
    engineer_relationship_field = relationship('Engineers', back_populates='tasks_relationship_field')

    # serialize_rules = ('-arena_field', '-gladiator_field')



class Engineers(db.Model, SerializerMixin):
    __tablename__ = 'engineers_table'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable = False)
    location = db.Column(db.String)
    # relationships
    tasks_relationship_field = relationship('Tasks', back_populates='engineer_relationship_field')