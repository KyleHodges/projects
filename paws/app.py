from datetime import date, time
import sqlite3
from flask import Flask, flash, render_template, request, session
from flask_cors import CORS
from flask_session import Session
import math




app = Flask(__name__)
CORS(app)

con = sqlite3.connect('puppy.db')
db = con.cursor()

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

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        names = db.execute('SELECT name FROM pups')
        return render_template('index.html', names = names)
    else:
        #get dog name and corresponding information to pass to print

        name = request.form.get('puppy')
        name = name.lstrip("{''name'': ''").rstrip("'}")
        registration = db.execute('SELECT registration FROM profile WHERE name = ?', name)
        location = db.execute('SELECT location FROM profile WHERE name = ?', name)
        day = db.execute('SELECT birthday FROM profile WHERE name = ?', name)
        for d in day:
            birthday = d['birthday']
            birthday = date.fromisoformat(birthday)
        today = date.today()
        delta = (today - birthday)
        years = math.floor(delta.days / 365)
        months = round((delta.days / 365) % 1 * 12)
        age = f'{years}yrs {months}mths'
        gender = db.execute('SELECT gender FROM profile WHERE name = ?', name)
        vet = db.execute('SELECT vet FROM profile WHERE name = ?', name)
        primary = db.execute('SELECT hand_p FROM profile WHERE name = ?', name)
        secondary = db.execute('SELECT hand_s FROM profile WHERE name = ?', name)
        skills = db.execute('SELECT * FROM skills WHERE name = ?', name)
        return render_template('print.html', name = name, registration = registration, age = age, gender = gender, location = location, vet = vet, primary = primary, secondary = secondary, skills = skills)

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'GET':
        names = db.execute('SELECT name FROM pups')
        return render_template('update.html', names = names)
    else:
        #take all input from update form and update sql databases
        name = request.form.get('puppy')
        name = name.lstrip("{''name'': ''").rstrip("'}")

        registration = request.form.get('registration')
        if registration:
            db.execute('UPDATE profile SET registration = ? WHERE name = ?', registration, name)
        location = request.form.get('location')
        if location:
            db.execute('UPDATE profile SET location = ? WHERE name = ?', location, name)
        birthday = request.form.get('birthday')
        if birthday:
            db.execute('UPDATE profile SET birthday = ? WHERE name = ?', birthday, name)
        primary = request.form.get('primary')
        if primary:
            db.execute('UPDATE profile SET hand_p = ? WHERE name = ?', primary, name)
        secondary = request.form.get('secondary')
        if secondary:
            db.execute('UPDATE profile SET hand_s = ? WHERE name = ?', secondary, name)
        gender = request.form.get('gender')
        if gender:
            db.execute('UPDATE profile SET gender = ? WHERE name = ?', gender, name)
        vet = request.form.get('vet')
        if vet:
            db.execute('UPDATE profile SET vet = ? WHERE name = ?', vet, name)

        #update profile table


        #get all skill inputs and update skills table
        aggression = request.form.get('aggression')
        if aggression:
            db.execute('UPDATE skills SET aggression = ? WHERE name = ?', aggression, name)
        hug = request.form.get('hug')
        if hug:
            db.execute('UPDATE skills SET hug = ? WHERE name = ?', hug, name)
        takeaway = request.form.get('takeaway')
        if takeaway:
            db.execute('UPDATE skills SET takeaway = ? WHERE name = ?', takeaway, name)
        petting = request.form.get('petting')
        if petting:
            db.execute('UPDATE skills SET petting = ? WHERE name = ?', petting, name)
        exam = request.form.get('exam')
        if exam:
            db.execute('UPDATE skills SET exam = ? WHERE name = ?', exam, name)
        straight = request.form.get('straight')
        if straight:
            db.execute('UPDATE skills SET straight = ? WHERE name = ?', straight, name)
        leash5 = request.form.get('leash5')
        if leash5:
            db.execute('UPDATE skills SET leash5 = ? WHERE name = ?', leash5, name)
        sit = request.form.get('sit')
        if sit:
            db.execute('UPDATE skills SET sit = ? WHERE name = ?', sit, name)
        down = request.form.get('down')
        if down:
            db.execute('UPDATE skills SET down = ? WHERE name = ?', down, name)
        stay10 = request.form.get('stay10')
        if stay10:
            db.execute('UPDATE skills SET stay10 = ? WHERE name = ?', stay10, name)
        accepting = request.form.get('accepting')
        if accepting:
            db.execute('UPDATE skills SET accepting = ? WHERE name = ?', accepting, name)
        sitpet = request.form.get('sitpet')
        if sitpet:
            db.execute('UPDATE skills SET sitpet = ? WHERE name = ?', sitpet, name)
        groom = request.form.get('groom')
        if groom:
            db.execute('UPDATE skills SET groom = ? WHERE name = ?', groom, name)
        walkloose = request.form.get('walkloose')
        if walkloose:
            db.execute('UPDATE skills SET walkloose = ? WHERE name = ?', walkloose, name)
        walkcrowd = request.form.get('walkcrowd')
        if walkcrowd:
            db.execute('UPDATE skills SET walkcrowd = ? WHERE name = ?', walkcrowd, name)
        sitandstay = request.form.get('sitandstay')
        if sitandstay:
            db.execute('UPDATE skills SET sitandstay = ? WHERE name = ?', sitandstay, name)
        downandstay = request.form.get('downandstay')
        if downandstay:
            db.execute('UPDATE skills SET downandstay = ? WHERE name = ?', downandstay, name)
        comefromss = request.form.get('comefromss')
        if comefromss:
            db.execute('UPDATE skills SET comefromss = ? WHERE name = ?', comefromss, name)
        leaveit = request.form.get('leaveit')
        if leaveit:
            db.execute('UPDATE skills SET leaveit = ? WHERE name = ?', leaveit, name)
        dogreact = request.form.get('dogreact')
        if dogreact:
            db.execute('UPDATE skills SET dogreact = ? WHERE name = ?', dogreact, name)
        distraction = request.form.get('distraction')
        if distraction:
            db.execute('UPDATE skills SET distraction = ? WHERE name = ?', distraction, name)
        supstranger = request.form.get('supstranger')
        if supstranger:
            db.execute('UPDATE skills SET supstranger = ? WHERE name = ?', supstranger, name)
        downandstay20 = request.form.get('downandstay20')
        if downandstay20:
            db.execute('UPDATE skills SET downandstay20 = ? WHERE name = ?', downandstay20, name)
        waits = request.form.get('waits')
        if waits:
            db.execute('UPDATE skills SET waits = ? WHERE name = ?', waits, name)
        walkdirection = request.form.get('walkdirection')
        if walkdirection:
            db.execute('UPDATE skills SET walkdirection = ? WHERE name = ?', walkdirection, name)
        walkloosecrowd = request.form.get('walkloosecrowd')
        if walkloosecrowd:
            db.execute('UPDATE skills SET walkloosecrowd = ? WHERE name = ?', walkloosecrowd, name)
        walkdistraction = request.form.get('walkdistraction')
        if walkdistraction:
            db.execute('UPDATE skills SET walkdistraction = ? WHERE name = ?', walkdistraction, name)
        sitstaygroup = request.form.get('sitstaygroup')
        if sitstaygroup:
            db.execute('UPDATE skills SET sitstaygroup = ? WHERE name = ?', sitstaygroup, name)
        carrypet = request.form.get('carrypet')
        if carrypet:
            db.execute('UPDATE skills SET carrypet = ? WHERE name = ?', carrypet, name)
        comedistraction = request.form.get('comedistraction')
        if comedistraction:
            db.execute('UPDATE skills SET hug = ? WHERE name = ?', comedistraction, name)
        doorway = request.form.get('doorway')
        if doorway:
            db.execute('UPDATE skills SET doorway = ? WHERE name = ?', doorway, name)

        #give success message and send to index
        flash('Success')
        names = db.execute('SELECT name FROM pups')
        return render_template('index.html', names = names)


@app.route('/print', methods=['GET', 'POST'])
def print():
    if request.method == 'GET':
        return render_template('print.html')