from flask import Flask, jsonify
from src.config import Config
from src.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from src import models  

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok"), 200

    return app
