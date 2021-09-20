from mock_data import mock_data
import json
from flask import Flask
app = Flask(__name__)


me = {
        "name": "Angel",
        "last": "Angel",
        "email": "Angel",
        "age": "Angel",
        "hobbies": "Angel",
        "address": "Angel"
}
@app.route("/")
def index():
        return "Hello from api"


@app.route("/about")
def about():
        return "Angel A"
      

@app.route("/about/email")
def get_email():
        return me["email"]
      

@app.route("/about/address")
def get_address():
        address = me["address"]
        return address["number"] + " " + address["street"]
      
# api methods

@app.route("/api/catalog")
def get_catalog():
        return json.dumps(mock_data)


@app.route("/api/categories")
def get_categories():


        categories =[]
        for product in mock_data:
                cat = product["category"]

                if cat not in categories:
                 categories.append(cat)

        return json.dumps(categories)



app.run(debug=True)

\\wsl$\kali-linux\home\networkangel\flask_api