import numpy as np
import pandas as pd
from flask import Flask, jsonify
from sqlalchemy import create_engine


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# database setup
path = "sqlite:///Resources/hawaii.sqlite"
engine = create_engine(path)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"""
        <ul>
            <h1>Surfs Up in Honolulu</h1>
            <br>
            <li><a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a></li>
            <li><a href='/api/v1.0/stations'>/api/v1.0/stations</a></li>
            <li><a href='/api/v1.0/tobs'>/api/v1.0/tobs</a></li>
            <li><a href='/api/v1.0/2012-01-12/2012-04-11'>/api/v1.0/2012-01-12/2012-04-11</a></li>
        </ul
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


@app.route("/api/v1.0/<start>/<end>")
def range(start, end):
    conn = engine.connect()
    query = f"""
        SELECT
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM
            measurement
        WHERE
            date >= '{start}'
            and date <= '{end}'
        """

    df = pd.read_sql(query, conn)
    conn.close
    data = df.to_dict(orient="records")
    return(jsonify(data))



if __name__ == '__main__':
    app.run(debug=True)