import os
import requests
from dotenv import load_dotenv
from flask import Flask

app = Flask(__name__)

load_dotenv()


@app.route("/")
def getLocation():
    apiKey = os.getenv("API_KEY")
    url = "https://geo.ipify.org/api/v1?apiKey={}".format(apiKey)
    res = requests.get(url).json()
    return res


app.run(host="0.0.0.0", port=8080)
