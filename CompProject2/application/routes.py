from application import app
from flask import render_template,url_for
import pandas as pd
import json
import plotly
import plotly.express as px


@app.route("/")

def index():
    df = pd.read_csv("/Users/Apple/Downloads/diabetes 2.csv")
    fig1 = px.bar(df,x = "Age",y = "Pregnancies")
    
    graphIJSON = json.dumps(fig1 , cls=plotly.utils.PlotlyJSONEncoder)
    
    return render_template("index.html", graph1JSON = graphIJSON)

