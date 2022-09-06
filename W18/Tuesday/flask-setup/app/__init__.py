from flask import Flask
from .config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def index():
  # this is where you would do DB stuff
  return '<h1>Sample app</h1>'
