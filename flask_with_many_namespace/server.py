from flask_cors import CORS
from flask import Flask
from flask_restx import Api
from post_image import namespace as identity_namespace
import os
from dotenv import load_dotenv
from pathlib import Path  # Python 3.6+ only


app = Flask(__name__)

CORS(app)
api = Api(app, title="Clover Project", version="1.0.0", description="Swagger API Homepage",)
api.add_namespace(identity_namespace, path="/api/identities")

# load_dotenv(verbose=True)
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

if __name__ == "__main__":
    app.run(host=os.getenv("SERVER_HOST"), port=os.getenv("SERVER_PORT"), threaded=True, debug=False)