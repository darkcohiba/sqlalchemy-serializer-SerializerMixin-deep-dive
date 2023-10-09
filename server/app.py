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
        # all_planet = Planet.query.all()
        # all_planet_dict = []
        # for planet in all_planet:
        #     planet.serialize_rules = ('-missions',)
        #     all_planet_dict.append(planet.to_dict())
        # return make_response(all_planet_dict,200)




if __name__ == '__main__':
    app.run(port=5555, debug=True)

