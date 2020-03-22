from flask import Flask, jsonify
from .models import setup_db, Plant
from  flask_cors import CORS

def create_app(test_config=None):
    app = Flask(__name__)
    #CORS(app, resources={r"*/api/*": {origins: '*'}})
    CORS(app)
    print(__name__)
    
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH , DELETE, OPTIONS')
        return response

    @app.route('/')
    def hello():
        return jsonify({'message': 'HELLO WORLD'})

    @app.route("/plants")
    def get_plants():
        plants = Plant.query.all()
        formatted_plants = [plant.format() for plant in plants]

        return jsonify({
                'success' : True,
                'plants' : formatted_plants
            })
    return app
