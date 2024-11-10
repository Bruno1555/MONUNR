from flask import Flask, redirect, render_template, request, session, g
from flask_session import Session
import sqlite3


from functions import login_required, apology

app = Flask(__name__)

# SQL CONFIG
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect("delegados.db")
        return g.db
    
@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()





    
# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app) 

@app.route("/")
def index():
    name = "Bruno"
    return render_template("index.html", name=name)


# TODO
@app.route("/login")
def login():
    session.clear
    
    return apology("TODO")

@app.route("/logout")
def logout():
    session.clear
    redirect("/")

@app.route("/register", methods=["GET", "POST"])
def register():
    db = get_db()


    nombre = request.form.get("nombre")
    apellido = request.form.get("apellido")
    curso = request.form.get("curso")
    seccion = request.form.get("seccion")
    comision = request.form.get("comision")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")

    if request.method == "POST":
        if not nombre:
            return apology("Nombre no-existente")
        elif not apellido:
            return apology("apellido inexistente")
        elif not password:
            return apology("contraseña no añadida")
        elif not password == confirmation:
            return apology("Contraseñas no coinciden") 
        else:
            db.execute(f"INSERT INTO {comision} (nombre, apellido, contraseña, curso, seccion) VALUES(?,?,?,?,?)", (nombre, apellido, password, curso, seccion))
            db.commit()
            return redirect("/")
        

    n_CIDH = db.execute("SELECT COUNT(*) FROM CIDH").fetchone()[0]
    n_OIM = db.execute("SELECT COUNT(*) FROM OIM").fetchone()[0]
    n_OMS = db.execute("SELECT COUNT(*) FROM OMS").fetchone()[0]
    n_OMT = db.execute("SELECT COUNT(*) FROM OMT").fetchone()[0]
    n_CEPAL = db.execute("SELECT COUNT(*) FROM CEPAL").fetchone()[0]

    return render_template("register.html", n_CIDH=n_CIDH, n_OIM=n_OIM, n_OMS=n_OMS, n_OMT=n_OMT, n_CEPAL=n_CEPAL )






