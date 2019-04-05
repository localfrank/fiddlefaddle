from flask import Blueprint

project = Blueprint('project', __name__)


@project.route('/projects', methods=['GET'])
def get_all_projects():
    """
    Get all projects
    """
    pass


@project.route('/projects/<project_id>', methods=['GET'])
def get_one_project(project_id):
    """
    Get project against project id
    """
    pass
