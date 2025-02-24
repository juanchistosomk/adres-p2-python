from flask import render_template, Blueprint, current_app

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    current_app.logger.info("Main route")
    return render_template('index.html')