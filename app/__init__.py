from flask import Flask
from .models import db


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    db.init_app(app)
    from .main.views import main_bp
    app.register_blueprint(main_bp)

    # Just for debugging
    # with app.app_context():
    #     # Query all entries
    #     entries = Entry.query.all()

    #     # Print the entries
    #     for entry in entries:
    #         print(entry.API, entry.Description, entry.Auth,
    #               entry.HTTPS, entry.Cors, entry.Link, entry.Category)

    return app
