from flask import Blueprint

from next.auth.trello import trello_bp

auth_bp = Blueprint("auth", __name__, template_folder="templates")
auth_bp.register_blueprint(trello_bp)
