import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model#
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
measure = Base.classes.measurement
stations = Base.classes.station

# Flask Setup
#################################################
app = Flask(__name__)

path = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(path)


app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"""
        <ul>
            <li><a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a></li>
            <li><a href='/api/v1.0/stations'>/api/v1.0/stations</a></li>
            <li><a href='/api/v1.0/tobs'>/api/v1.0/tobs</a></li>
            <li><a href='/api/v1.0/2010-01-01'>/api/v1.0/2010-01-01</a></li>
            <li><a href='/api/v1.0/2016-08-23/2017-08-23'>/api/v1.0/2016-08-23/2017-08-23</a></li>
            """
    )

@app.route("/api/v1.0/precipitation")
def prcp():
    conn = engine.connect()
    query = """
            Select
                date, station, prcp
            From
                measurement
            Order By 
                date asc;
            """
    df = pd.read_sql(query, conn)
    conn.close
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def stations():
   conn = engine.connect()
   query = """
            Select Distinct
                station
            From
                station
            """
   df = pd.read_sql(query, conn)
   conn.close
   data = df.to_dict(orient="records")
   return(jsonify(data))

@app.route("/api/v1.0/tobs")
def tobs():
    conn = engine.connect()
    query = """
            Select
                date, station, tobs
            From
                measurement
            where
                date >= '2016-08-23'
                And station = 'USC00519281';
             """
    df = pd.read_sql(query, conn)
    conn.close
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/2010-01-01")
def start():
    conn = engine.connect()
    query= """
            Select 
                max(tobs) as tmax, min(tobs) as tmin, avg(tobs) as tavg
            From 
                measurement
            Where
                date >= '2010-01-01';
            """
    df = pd.read_sql(query, conn)
    conn.close
    data = df.to_dict(orient="records")
    return(jsonify(data))

       
@app.route("/api/v1.0/2016-08-23/2017-08-23")
def startend():
    conn = engine.connect()
    query= """
            Select 
                max(tobs) as tmax, min(tobs) as tmin, avg(tobs) as tavg
            From 
                measurement
            Where
                date >= '2016-08-23'
                And date <= '2017-08-23';
            """
    df = pd.read_sql(query, conn)
    conn.close
    data = df.to_dict(orient="records")
    return(jsonify(data))



if __name__ == '__main__':
    app.run(debug=True)