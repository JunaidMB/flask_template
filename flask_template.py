import os
import sys

def flask_template():

    # Make app directory
    os.makedirs("./app")

    # __init__.py
    init = open("./app/__init__.py", "w")

    text_list = ["from flask import Flask\n", "\n",  "app = Flask(__name__)\n", "\n", 'if app.config["ENV"] == "production":\n', '  app.config.from_object("config.ProductionConfig")\n', 'elif app.config["ENV"] == "testing":\n', '  app.config.from_object("config.TestingConfig")\n', 'else:\n', '  app.config.from_object("config.DevelopmentConfig")\n', '\n', 'from app import views']

    init.writelines(text_list)
    init.close()

    # views.py
    view_py = open("./app/views.py", "w")

    text_list = ['from app import app\n', 'from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort, flash, url_for, session\n', '\n', '@app.route("/")\n', 'def index():\n', '  return "hello world"']

    view_py.writelines(text_list)
    view_py.close()

    # config.py
    config = open("./config.py", "w")

    text_list = ['from app import app\n', '\n',  'class Config(object):\n', '  DEBUG = False\n', '  TESTING = False\n', '\n', 'class ProductionConfig(Config):\n', '  pass\n', '\n', 'class DevelopmentConfig(Config):\n', '  DEBUG = True\n', '\n', 'class TestingConfig(Config):\n', '  TESTING = True']

    config.writelines(text_list)
    config.close()

    # run.py
    run_py = open("./run.py", "w")

    text_list = ['from app import app\n', '\n', 'if __name__ == "main":\n', '  app.run(host="0.0.0.0")']

    run_py.writelines(text_list)
    run_py.close()

    # Requirements.txt
    os.system('pip freeze > requirements.txt')

    # Dockerfile
    dockerfile = open("Dockerfile", "w")

    text_list = ['FROM python:3.7.2-stretch\n', '\n', 'WORKDIR /app\n', '\n', 'ADD . /app\n', '\n', 'RUN pip install -r requirements.txt\n', '\n', 'EXPOSE 5000\n', '\n', 'CMD ["python", "run.py"]']

    dockerfile.writelines(text_list)
    dockerfile.close()

    return print("flask template built")


flask_template()







