from flask import Blueprint
from pathlib import PurePath

static_folder = PurePath(PurePath(__file__).parent.parent.parent.parent, "overlay", "out")

main_bp = Blueprint(
    "main",
    __name__,
    static_url_path="/build",
    static_folder=static_folder,
    template_folder=static_folder
)

from . import routes
