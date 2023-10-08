#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Engineers, Tasks, Projects

fake = Faker()

def create_db():
    db.create_all()

def create_engineers():
    engineer_list = []

    for _ in range(50):
        e = Engineers(
            title=fake.name(),
            location= fake.city()
        )
        engineer_list.append(e)
    return engineer_list


def create_projects():
    project_list= []

    for _ in range(50):
        p = Projects(
            company=fake.company(),
            scope= fake.paragraph(),
            budget=randint(100000,10000000)
        )
        project_list.append(p)
    return project_list

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        # create_db()

        eng = create_engineers()
        db.session.add_all(eng)
        db.session.commit()


        proj = create_projects()
        db.session.commit(proj)
        db.session.commit()




