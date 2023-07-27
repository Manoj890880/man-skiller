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


@app.route('/projects/<string:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        # Find the project by its ID
        project = db.projects.find_one({"_id": ObjectId(project_id)})
        if not project:
            return jsonify({"message": "Project not found"}), 404

        # Delete the project
        db.projects.delete_one({"_id": ObjectId(project_id)})

        return jsonify({"message": "Project and associated tasks and resources deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Error deleting project", "error": str(e)}), 500


@app.route('/projects/<string:project_id>', methods=['PATCH'])
def update_project(project_id):
    updated_fields = request.json

    # Convert project_id to ObjectId
    project_id_object = ObjectId(project_id)

    # Find the project using the ObjectId
    project_to_update = db.projects.find_one({'_id': project_id_object}, {'_id': False})

    if not project_to_update:
        return jsonify({"message": "Project not found"}), 404

    # Partially update the project with the provided fields
    db.projects.update_one({"_id": project_id_object}, {"$set": updated_fields})

    # Fetch the updated project after the update
    updated_project = db.projects.find_one({'_id': project_id_object}, {'_id': False})

    return jsonify({"message": "Project updated successfully", "project": updated_project})


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    # Assuming you have a collection called "tasks" in your MongoDB
    result = db.tasks.insert_one(data)
    if result.inserted_id:
        # Convert ObjectId to string for JSON serialization
        data["_id"] = str(result.inserted_id)
        return jsonify(data), 201
    else:
        return jsonify({"message": "Failed to create task"}), 500


@app.route('/projects/<string:project_id>/tasks', methods=['GET'])
def get_tasks_by_project_id(project_id):
    # Assuming you have a collection called "tasks" in your MongoDB
    tasks = db.tasks.find({"project_id": project_id})
    task_list = []
    for task in tasks:
        task['_id'] = str(task['_id'])
        task_list.append(task)
    return jsonify(task_list), 200


@app.route('/resources', methods=['POST'])
def create_resource():
    data = request.json
    # Assuming you have a collection called "resources" in your MongoDB
    result = db.resources.insert_one(data)
    if result.inserted_id:
        # Convert ObjectId to string for JSON serialization
        data["_id"] = str(result.inserted_id)
        return jsonify(data), 201
    else:
        return jsonify({"message": "Failed to create resource"}), 500


@app.route('/tasks/<task_id>/resources', methods=['GET'])
def get_resources_by_task_id(task_id):
    try:
        task_resources = db.resources.find({"task_id": task_id})
        resources = [resource for resource in task_resources]

        # Convert ObjectId to string for JSON serialization
        for resource in resources:
            resource["_id"] = str(resource["_id"])

        return jsonify(resources)
    except Exception as e:
        return jsonify({"message": f"Error fetching resources: {str(e)}"}), 500


@app.route('/tasks/<string:task_id>/resources', methods=['DELETE'])
def delete_resources_for_task(task_id):
    try:
        # Find the task by its ID
        task = db.tasks.find_one({"_id": ObjectId(task_id)})
        if not task:
            return jsonify({"message": "Task not found"}), 404

        # Delete resources associated with the task
        db.resources.delete_many({"task_id": task_id})

        return jsonify({"message": "Resources deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Error deleting resources", "error": str(e)}), 500


@app.route('/projects/<string:project_id>/tasks', methods=['DELETE'])
def delete_tasks_for_project(project_id):
    try:
        # Find the project by its ID
        project = db.projects.find_one({"_id": ObjectId(project_id)})
        if not project:
            return jsonify({"message": "Project not found"}), 404

        # Delete tasks associated with the project
        db.tasks.delete_many({"project_id": project_id})

        return jsonify({"message": "Tasks deleted successfully"}), 200

    except Exception as e:
        return jsonify({"message": "Error deleting tasks", "error": str(e)}), 500


if __name__ == '__main__':
    app.run()
