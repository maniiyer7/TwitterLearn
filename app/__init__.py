from flask import Flask, redirect, request, render_template, url_for
#from flaskext.uploads import delete, init, save, Upload
from flask_bootstrap import Bootstrap

def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()
from app import views
