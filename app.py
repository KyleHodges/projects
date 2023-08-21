import os
import csv
import datetime
from cs50 import get_int
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_cors import CORS
from flask_session import Session
from tempfile import mkdtemp



app = Flask(__name__)
CORS(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///church.db")

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        hymns_db = db.execute("SELECT s_title FROM hymns")
        songs_db = db.execute("SELECT s_title FROM modern_songs")
        dates_db = db.execute("SELECT date FROM c_church")
        return render_template("index.html", hymns = hymns_db, songs = songs_db, dates = dates_db)
    else:
        date = request.form.get("service-date")
        call = request.form.get("call_h")

        if not call:
            call = request.form.get("call_s")

        a1 = request.form.get("s1_h")
        if not a1:
            a1 = request.form.get("s1_s")

        a2 = request.form.get("s2_h")
        if not a2:
            a2 = request.form.get("s2_s")

        a3 = request.form.get("s3_h")
        if not a3:
            a3 = request.form.get("s3_s")

        a4 = request.form.get("s4_h")
        if not a4:
            a4 = request.form.get("s4_s")
        a = {a1, a2, a3, a4}
        offer = request.form.get("offer_h")
        if not offer:
            offer = request.form.get("offer_s")

        sp1 = request.form.get("sp1")
        sp2 = request.form.get("sp2")
        sp3 = request.form.get("sp3")
        special = {sp1, sp2, sp3}
        invite = request.form.get("inv_h")
        if not invite:
            invite = request.form.get("inv_s")

        teacher = db.execute("SELECT name FROM c_church WHERE date = ?", date)

        return render_template("plan.html", date = date, call = call, offer = offer, special = special, invite = invite, name = teacher, a = a)

@app.route("/addsongs", methods=["GET", "POST"])
def addsongs():
    if request.method == "GET":
        return render_template("addsongs.html")

    else:
        s_title = request.form.get("title")
        artist = request.form.get("artist")
        number = request.form.get("number")
        h_title = request.form.get("htitle")

        if not h_title:
            db.execute("INSERT INTO modern_songs (s_title, artist) VALUES (?, ?)", s_title, artist)

        if not s_title:
            db.execute("INSERT INTO hymns (s_title, number) VALUES (?, ?)", h_title, number)

        flash("Song Added!")
        return render_template("added.html")

@app.route("/added", methods=["GET", "POST"])
def added():
    if request.method == "GET":
        return render_template("added.html")

    else:
        s_title = request.form.get("title")
        artist = request.form.get("artist")
        number = request.form.get("number")
        h_title = request.form.get("htitle")


        if not h_title:
            db.execute("INSERT INTO modern_songs (s_title, artist) VALUES (?, ?)", s_title, artist)

        if not s_title:
            db.execute("INSERT INTO hymns (s_title, number) VALUES (?, ?)", h_title, number)

        return render_template("added.html")



@app.route("/kids", methods=["GET", "POST"])
def kids():
    if request.method == "GET":
        return render_template("kids.html")



@app.route('/upload_static_file', methods=['POST'])
def upload_static_file():
    print("Got request in static files")
    print(request.files)
    f = request.files['static_file']
    f.save(f.filename)
    os.rename(f.filename, 'file.csv')
    with open("file.csv", "r") as file:
        reader = csv.DictReader(file)

        names = ()
        dates = ()

        db.execute("DELETE FROM c_church")
        for line in reader:
            dates = line["Date"]
            names = line["Name"]
            db.execute("INSERT INTO c_church (date, name) VALUES (?, ?)", dates, names)



    return redirect("/")

@app.route("/plan", methods=["GET", "POST"])
def plan():
    if request.method == "GET":
        return render_template("plan.html")
