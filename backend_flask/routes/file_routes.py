from flask import Blueprint, jsonify
from methods.file_operations import list_files, move_file

file_blueprint = Blueprint('file_blueprint', __name__)

@file_blueprint.route('/list_files', methods=['GET'])
def route_list_files():
    files = list_files('source_data')
    return jsonify(files)

@file_blueprint.route('/move_file/<filename>', methods=['GET'])
def route_move_file(filename):
    result = move_file('source_data', 'processed_data', filename)
    return jsonify(result)
