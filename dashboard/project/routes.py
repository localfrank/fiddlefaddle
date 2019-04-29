from flask import Blueprint, jsonify
from dashboard.auth.utils import token_required

project = Blueprint('project', __name__)


@project.route('/projects', methods=['GET'])
@token_required
def get_all_projects(current_user):
    """
    Get all projects
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403
    pass


@project.route('/projects/<project_id>', methods=['GET'])
@token_required
def get_one_project(current_user, project_id):
    """
    Get project details against project id
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403
    pass


@project.route('/project', methods=['POST'])
@token_required
def new_project(current_user):
    """
    Create new project
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403
    pass


@project.route('/project/<project_id>', methods=['PUT'])
@token_required
def update_project(current_user, project_id):
    """
    Update project details
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403
    pass


@project.route('/project/<project_id>', methods=['DELETE'])
@token_required
def delete_project(current_user, project_id):
    """
    Delete project
    """
    if not current_user.admin:
        return jsonify({'message': 'Only admin user can perform this function!'}), 403
    pass
