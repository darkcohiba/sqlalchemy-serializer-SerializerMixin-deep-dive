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

def create_tasks(projects, engineers):
    task_list = []
    for pro in projects:
        for _ in range(5):
            engineer = rc(engineers)
            t = Tasks(
                title=fake.name(),
                cost= randint(50, 10000),
                description=fake.paragraph(),
                project_id=pro.id,
                engineer_id=engineer.id
            )
            task_list.append(t)
    return task_list

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

 

        # Seed code goes here!
        # print("removing current data")
        # db.session.query(Engineers).delete()
        # db.session.query(Tasks).delete()
        # db.session.query(Projects).delete()


        # # create_db()
        # print("seeding engineers")

        # eng = create_engineers()
        # db.session.add_all(eng)
        # db.session.commit()

        # print("seeding projects")
        # proj = create_projects()
        # db.session.add_all(proj)
        # db.session.commit()


        # print("seeding tasks")
        # task = create_tasks(proj, eng)
        # db.session.add_all(task)
        # db.session.commit()

        # print("great sucess! Everything is seeded!✅")







