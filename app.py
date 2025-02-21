from flask import Flask,render_template,request,redirect,session
from cs50 import SQL
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps
import datetime

db = SQL("sqlite:///finalproject.db")

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

app = Flask(__name__)
app.secret_key = "cu&hds/¨kjdnkj844*54![8%62`4fds#f84$6"

@app.route("/",methods=["GET", "POST"])
@login_required
def index():
    if request.method == "POST":
        tasks = request.form.getlist('tasks') 
        b = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?","tasks" + str(session["id"]))
        if len(b) == 0 :
            db.execute("CREATE TABLE tasks?(task TEXT , type TEXT , checked TEXT , date DATE)",session["id"])
        for task in tasks :
            current_time = str(datetime.date.today())
            db.execute("INSERT INTO tasks?(task, type , checked,date) VALUES(?,'task','false',?)",session["id"],task,current_time)
        return redirect("/tasks")
    else:
        user = session["name"]
        table = {}
        b = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?","tasks" + str(session["id"]))
        if len(b)!=0:
            table = db.execute("SELECT * FROM tasks? WHERE checked='false'",session["id"])
        return render_template("index.html" , name = user,table = table)

@app.route("/tasks",methods=["GET", "POST"])
@login_required
def tasks():
    if request.method == "POST":
        checked_tasks = request.form.getlist('option')
        print("checked tasks : ",checked_tasks)
        current_time = str(datetime.date.today())
        for task in checked_tasks:
            db.execute("UPDATE tasks? SET checked = 'true' , date = ? WHERE task = ? AND type = 'task'", session["id"],current_time,task)
            db.execute("UPDATE tasks? SET checked = 'true' WHERE task = ? AND type = 'daily' and date =?", session["id"],current_time,task)
        return redirect("/checked")
    else:
        b = db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?","tasks" + str(session["id"]))
        if len(b) == 0 :
            db.execute("CREATE TABLE tasks?(task TEXT , type TEXT , checked TEXT , date DATE)",session["id"])
        table = db.execute("SELECT * FROM tasks? WHERE checked='false' AND type='task'",session["id"])
        return render_template("tasks.html",table = table)
        
@app.route("/checked")
@login_required
def checked():
    table = db.execute("SELECT * FROM tasks? Where checked = 'true'",session["id"])
    return render_template("checked.html",table = table)

@app.route("/register",methods=["GET", "POST"])
def register():
    if request.method == "POST":
            if not request.form.get("username"):
                return render_template("register.html" , user = "must provide a username", password = "" , confirmation = "")
            elif not request.form.get("password"):
                return render_template("register.html" , password = "must provide a password" , user="" , confirmation ="")
            elif not request.form.get("confirmation"):
                return render_template("register.html" , confirmation = "must confirm your password" , user ="" , password ="")
            elif request.form.get("password") != request.form.get("confirmation"):
                return render_template("register.html" , confirmation = "passwords do not match" , password = "" , user ="")
            elif len(request.form.get("password")) < 8:
                return render_template("register.html" , password = "password must have at least 8 characters" , user="" , confirmation ="")
            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", request.form.get("username")
            )
            if len(rows) != 0:
                return render_template("register.html" , user = "username is taken" , password = "", confirmatin = "")
            username = request.form.get("username")
            hash = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users(username,hash) VALUES(?,?)", username, hash)
            return redirect("/")
    else:
        return render_template("register.html")

@app.route("/login",methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("login.html" , user = "must provide a username" , password = "")

        elif not request.form.get("password"):
            return render_template("login.html" , user = "",password = "must provide a password")

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("login.html" , user = "",password = "invalid username and/or password")
        session["id"] = rows[0]["id"]
        session["name"] = rows[0]["username"]
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

