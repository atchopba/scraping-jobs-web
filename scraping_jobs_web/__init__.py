#!/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = "Albin TCHOPBA"
# __copyright__ = "Copyright 2020 Albin TCHOPBA and contributors"
# __credits__ = ["Albin TCHOPBA and contributors"]
# __license__ = "GPL"
# __version__ = "3"
# __maintainer__ = "Albin TCHOPBA"
# __email__ = "Albin TCHOPBA <atchopba @ gmail dot com"
# __status__ = "Production"

from flask import Flask

def create_app():
    #
    app = Flask(__name__, instance_relative_config=False)
    #
    with app.app_context():
        from . import routes
        #
        app.register_blueprint(routes.main_bp)
        #
        #if app.config["FLASK_ENV"] == "development":
        #    pass
        #
        return app
