# Import needed dependecies to create app
#https://www.digitalocean.com/community/tutorials/how-to-structure-large-flask-applications
# ^ refrence used to create app
import numpy as np
import pandas as pd

# sqlAlchemy http://docs.sqlalchemy.org/en/latest/orm/extensions/automap.html#basic-use
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

# Stu_Pet Pals Shows alchemy before flask research indicates 
# it avoids circular imports and is more reusable
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

#Set up Flask
app = Flask(__name__)

#Set up Database. Placed SQLite in the same folder. Will return to meet MVC standard
Base = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("belly_button_biodiversity.sqlite")

# reflect the tables
Base.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
samples = Base.class.samples
otu = Base.class.otu
meta = Base.class.samples_metadata

session = Session(engine)

#create the backend routes to push data from db to DOM

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/names')

@app.route('/otu')

@app.route('/metadata/<sample>')

@app.route('/samples/<sample>')