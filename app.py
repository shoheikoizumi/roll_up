import os
from flask import Flask, render_template, url_for
import folium

app = Flask(__name__)

def create_map():
    m = folium.Map(location=[35.6895, 139.6917], zoom_start=12)
    return m

API_KEY = "AIzaSyDkfaQedVKWE0Qbl3VYoX_WH9hEEBL8NMQ"

@app.route("/")
def index():
    css_url = url_for('static', filename='css/styles.css')
    return render_template("index.html", api_key=API_KEY, css_url=css_url)



if __name__ == '__main__':
    app.run(debug=True)
