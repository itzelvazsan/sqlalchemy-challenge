# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#################################################
# Database Setup
#################################################
# create engine to hawaii.sqlite
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return (
        f"Welcome to my 'Home' page!<br/>"
        f"Here are the available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
    )

#Define what to do when a user hits the /api/v1.0/precipitation route
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all())
    session.close()
    results_dict = {result.date: result.prcp for result in results}
    return jsonify(results_dict)

#Define what to do when a user hits the /api/v1.0/stations route
@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    active_stations = session.query(Measurement.station).group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).all()
    session.close()    
    active_stations_list = [station[0] for station in active_stations]
    return jsonify(active_stations_list)

#Define what to do when a user hits the /api/v1.0/tobs route
@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    act_station_year = session.query(Measurement.date, Measurement.tobs).filter(Measurement.station == 'USC00519281').filter(Measurement.date >= '2016-08-23').all()
    session.close()
    act_station_year_dict = {act_station_year.date: act_station_year.tobs for station in act_station_year}
    return jsonify(act_station_year_dict)

#Define what to do when a user hits the /api/v1.0/<start> route
@app.route("/api/v1.0/<start>")
def start(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results_start = session.query(func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)).filter(Measurement.date >= start_date).all()
    session.close()
    start_ls = []
    for min, max, avg in results_start:
        start_dict = {}
        start_dict[min] = min
        start_dict[max] = max
        start_dict[avg] = avg
        start_ls.append(start_dict) 
    return jsonify(start_ls)

#Define what to do when a user hits the /api/v1.0/<start>/<end> route
@app.route("/api/v1.0/<start>/<end>")
def end(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results_start_end = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    start_end_ls = []
    for min, max, avg in results_start_end:
        start_end_dict = {}
        start_end_dict[min] = min
        start_end_dict[max] = max
        start_end_dict[avg] = avg
        start_end_ls.append(start_end_dict) 
    return jsonify(start_end_ls)


if __name__ == "__main__":
    app.run(debug=True)
