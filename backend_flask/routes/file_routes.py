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

@file_blueprint.route('/', methods=['GET'])
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Day and Night Cycle</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(to bottom, #2b1055, #7597de);
                transition: background-color 2s;
            }
            .celestial-body {
                width: 150px;
                height: 150px;
                border-radius: 50%;
                position: relative;
                box-shadow: 0 0 50px rgba(255, 255, 0, 0.5);
                transition: all 2s;
            }
            .moon {
                background: #f6f8ff;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.2);
                transition: all 2s;
            }
            .crater {
                position: absolute;
                background: #ccc;
                width: 20px;
                height: 20px;
                border-radius: 50%;
                opacity: 0;
                transition: opacity 2s;
            }
            .crater:nth-child(2) { top: 30px; left: 50px; }
            .crater:nth-child(3) { top: 80px; left: 110px; }
            .crater:nth-child(4) { top: 40px; left: 100px; }
        </style>
    </head>
    <body>
        <div class="celestial-body moon">
            <div class="crater"></div>
            <div class="crater"></div>
            <div class="crater"></div>
        </div>
        <script>
            const body = document.querySelector('.celestial-body');
            const craters = document.querySelectorAll('.crater');
            const toggleDayNight = () => {
                body.classList.toggle('moon');
                craters.forEach(crater => crater.style.opacity = body.classList.contains('moon') ? 0 : 1);
                document.body.style.background = body.classList.contains('moon') ? 
                    'linear-gradient(to bottom, #2b1055, #7597de)' : 
                    'linear-gradient(to bottom, #ff9900, #ffe4b3)';
            };
            
            // Run every two minutes
            setInterval(toggleDayNight, 120000);
        </script>
    </body>
    </html>
    """
    return html_content
