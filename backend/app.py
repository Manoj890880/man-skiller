from bson import ObjectId
from flask_cors import CORS
from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
client = MongoClient("mongodb://localhost:27017")
db = client["project_portfolio"]


# Add this before connecting to MongoDB


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/portfolio-managers', methods=['POST'])
def create_portfolio_manager():
    data = request.json
    result = db.portfolio_managers.insert_one(data)
    return jsonify(str(result.inserted_id)), 201


@app.route('/portfolio-managers/<string:manager_id>', methods=['GET'])
def get_portfolio_manager_by_id(manager_id):
    manager = db.portfolio_managers.find_one({'_id': ObjectId(manager_id)}, {'_id': False})
    if manager:
        return jsonify(manager), 200
    else:
        return jsonify({"message": "Portfolio Manager not found"}), 404


@app.route('/portfolio-managers/<string:manager_id>', methods=['DELETE'])
def delete_portfolio_manager(manager_id):
    result = db.portfolio_managers.delete_one({"_id": ObjectId(manager_id)})
    if result.deleted_count > 0:
        return jsonify({"message": "Portfolio Manager deleted successfully"}), 200
    else:
        return jsonify({"message": "Portfolio Manager not found"}), 404


@app.route('/portfolio-managers/<string:manager_id>', methods=['PUT'])
def update_portfolio_manager(manager_id):
    data = request.json
    updated_fields = {}
    if "name" in data:
        updated_fields["name"] = data["name"]
    if "status" in data:
        updated_fields["status"] = data["status"]
    if "role" in data:
        updated_fields["role"] = data["role"]
    if "bio" in data:
        updated_fields["bio"] = data["bio"]
    if "date" in data:
        updated_fields["date"] = data["date"]
    if "email" in data:
        updated_fields["email"] = data["email"]
    if "password" in data:
        updated_fields["password"] = data["password"]

    result = db.portfolio_managers.update_one({"_id": ObjectId(manager_id)}, {"$set": updated_fields})
    if result.modified_count > 0:
        updated_manager = db.portfolio_managers.find_one({"_id": ObjectId(manager_id)}, {'_id': False})
        return jsonify(updated_manager), 200
    else:
        return jsonify({"message": "Portfolio Manager not found"}), 404


@app.route('/portfolio-managers', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')

    # Find the portfolio manager by email and password
    portfolio_manager = db.portfolio_managers.find_one({"email": email, "password": password}, {"_id": 1})

    if portfolio_manager:
        return jsonify({"_id": str(portfolio_manager["_id"])})
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    # Assuming you have a collection called "projects" in your MongoDB
    result = db.projects.insert_one(data)
    if result.inserted_id:
        # Convert ObjectId to string for JSON serialization
        data["_id"] = str(result.inserted_id)
        return jsonify(data), 201
    else:
        return jsonify({"message": "Failed to create project"}), 500


@app.route('/projects/manager/<string:manager_id>', methods=['GET'])
def get_projects_by_manager(manager_id):
    try:
        # Find all projects with the specified manager_id in the "projects" collection
        projects = list(db.projects.find({'manager_id': manager_id},
                                         {'_id': True, 'name': True, 'status': True, 'manager_id': True, 's_date': True,
                                          'e_date': True}))

        # Convert ObjectId to string for JSON serialization
        for project in projects:
            project['_id'] = str(project['_id'])

        return jsonify(projects), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/projects/<string:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        project = db.projects.find_one({'_id': ObjectId(project_id)}, {'_id': False})

        if not project:
            return jsonify({"message": "Project not found"}), 404
        return jsonify(project), 200
    except Exception as e:
        print(str(e))
        return jsonify({"message": "Internal server error"}), 500


if __name__ == '__main__':
    app.run()
