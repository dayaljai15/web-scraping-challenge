from flask import Flask, render_template, request
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)

app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_data"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def index():

    # Find a record
    mars_data = mongo.db.mars_data.find_one()

    # Return template and data
    return render_template("index.html", mars_data=mars_data)


#  trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run scrape 
    mars_data = scrape_mars.scrape()

    # Update Mongo database using update 
    mongo.db.mars_data.update({}, mars_data, upsert=True)
    return 'All done!'

if __name__ == "__main__":
    app.run(debug=True)
