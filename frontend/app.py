
from flask import Flask,request,render_template,redirect
import requests
import os

class Review(object):
    def __init__(self,name,review):
        self.name = name
        self.review = review
        
app = Flask(__name__)

# Get the backend URL from the environment variable
BACKEND_URL = os.getenv("BACKEND_URL", "http://backend:5000")  # Default to "http://backend:5000" if not set

@app.route("/",methods=["POST","GET"])
def index():

    if request.method == "POST":
        name = request.form["name"]
        review = request.form["review"]

        res = requests.post(f"{BACKEND_URL}/reviews/add",data={"name":name,"review":review})

        if res.status_code == 200:
            return redirect("/reviews")

    return render_template("index.html")

@app.route("/reviews",methods=["GET"])
def reviews():

    res = requests.post(f"{BACKEND_URL}/reviews/list").json()
    reviews = []

    for review in res["list"]:
        reviews.append(Review(review[0],review[1]))

    return render_template("reviews.html",reviews=reviews)

app.run(host="0.0.0.0",port=5000)