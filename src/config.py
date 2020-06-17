import os

ENV = os.environ.get("ENV", "local")
DEBUG = ENV == "local"
HOST = os.environ.get("HOST", "0.0.0.0")
