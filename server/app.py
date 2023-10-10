#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import make_response, jsonify, request
from flask_restful import Resource

# Local imports
from config import app, db, api
# Add your model imports
from models import Projects, Tasks, Engineers

# Views go here!

@app.route('/')
def index():
    return '<h1>Phase 4 Project Server</h1>'

@app.route("/projects")
def projectsAll():
    if request.method == "GET":
        projs = [p.to_dict() for p in Projects.query.all()]
        return make_response(projs, 200)
    
        # projs = [p.to_dict(rules=('check_costs','display_budget', '-budget')) for p in Projects.query.all()]

    
        # projs = [p.to_dict(rules=('-budget',)) for p in Projects.query.all()]
        # projs = [p.to_dict(only=('scope', 'budget')) for p in Projects.query.all()]


        # all_planet = Planet.query.all()
        # all_planet_dict = []
        # for planet in all_planet:
        #     planet.serialize_rules = ('-scope',)
        #     all_planet_dict.append(planet.to_dict())
        # return make_response(all_planet_dict,200)


@app.route("/tasks")
def tasksAll():
    if request.method == "GET":
        tas = [t.to_dict() for t in Tasks.query.all()]
        return make_response(tas, 200)

@app.route('/tasks/<id>')
def get_tasks_by_id(id):
    task = Tasks.query.filter(
        Tasks.id == id
    ).first()

    if not task:
        return make_response(
            jsonify({'error': 'Task not found'}),
            404
        )

    return make_response(
        jsonify(task.to_dict()),
        200
    )

@app.route("/engineers")
def enginAll():
    if request.method == "GET":
        engL = [e.to_dict() for e in Engineers.query.all()]
        return make_response(engL, 200)
    
        # engL = [e.to_dict(rules=('check_spending','total_tasks', 'avg_spend_per_task','-tasks_relationship_field')) for e in Engineers.query.all()]




if __name__ == '__main__':
    app.run(port=5555, debug=True)

