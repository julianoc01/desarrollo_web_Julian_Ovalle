from flask import Flask, request, render_template, redirect, url_for, session
#from utils.validations import validate_login_user, validate_register_user, validate_confession
from database import db
from werkzeug.utils import secure_filename
import hashlib
import filetype
import os
from datetime import datetime
from utils import validations
UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__)


app.secret_key = "s3cr3t_k3y"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000

@app.route("/portada", methods=["GET", "POST"])
def portada():
    data = db.get_avistamientos()
    
    for avis in data:
        for archivo in avis["archivos"]:
            archivo["url"] = url_for(
                "static", filename=archivo["ruta"]
            )
    
            extension = os.path.splitext(archivo["ruta"])[1].lower()
            archivo["es_video"] = extension in {
                ".mp4", ".webm", ".mov", ".avi", ".mkv", ".m4v"
            }
    return render_template("auth/portada.html", data = data)


@app.route("/estadisticas", methods=["GET", "POST"])
def estadisticas():
    data = db.get_avistamientos()
    
    for avis in data:
        for archivo in avis["archivos"]:
            archivo["url"] = url_for(
                "static", filename=archivo["ruta"]
            )
    
            extension = os.path.splitext(archivo["ruta"])[1].lower()
            archivo["es_video"] = extension in {
                ".mp4", ".webm", ".mov", ".avi", ".mkv", ".m4v"
            }
    usuario = "activo"
    if not session.get("user"):
        usuario = "inactivo"
        return render_template("avistamientos/estadisticas.html", data = data, usuario = usuario)

    return render_template("avistamientos/estadisticas.html", data = data)




@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("nombre")
        password = request.form.get("clave")
        error = ""
        if validations.validar_nombre(username) and validations.validar_contrasena(password):
            # try to login
            status, msg = db.login_user(username, password)
            if status:
                # set user field in session
                session["user"] = username
                return redirect(url_for("panel"))
                error += msg
            else:
                error += "Uno de los campos no es valido."

        #print(error)

        return render_template("auth/login.html")
    
    elif request.method == "GET":
        if session.get("user", None):
            return redirect(url_for("panel"))
        else:
            return render_template("auth/login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("nombre")
        password = request.form.get("contrasena")
        password2 = request.form.get("contrasena2")
        email = request.form.get("mail")
        telefono = request.form.get("telefono")
        comuna = request.form.get("comuna")
        region = request.form.get("region")


        mail_prueba = ""
        if db.get_user_by_email(email) is not None:
            mail_prueba = db.get_user_by_email(email).email


        error = ""
        if validations.validar_registro(username,telefono,email,region,comuna, password, password2) and (email != mail_prueba):

            # try to register user
            status, msg = db.register_vol(username, password, email, telefono, comuna)
            if status:
                # set user field in session
                session["user"] = username
                return redirect(url_for("index"))
            error += msg
        else:
            error += "Uno de los campos no es valido."

        return render_template("auth/register.html")
    
    elif request.method == "GET":
        if session.get("user", None):
            return redirect(url_for("panel"))
        else:
            return render_template("auth/register.html")
    



@app.route("/panel", methods=["GET"])
def panel():
    if not session.get("user"):
        return redirect(url_for("login"))

    #return render_template("avistamientos/panel.html", data=[])
    return redirect(url_for("index"))

@app.route("/logout", methods=["GET"])
def logout():
    session.pop("user", None)
    return redirect(url_for("portada"))

@app.route("/post-avis", methods=["POST"])
def post_avis():
    username = session.get("user", None)
    if username is None:
        return redirect(url_for("login"))

    ave_avis = request.form.get("ave")
    fecha_avis = request.form.get("fecha")
    lugar_avis = request.form.get("lugar")
    foto = request.files.get("foto")
    comentario_avis = request.form.get("comentario")

    if validations.validar_avis(ave_avis, fecha_avis, lugar_avis, foto, comentario_avis):
        # 1. generate random name for img
        _filename = hashlib.sha256(
            secure_filename(foto.filename) # nombre del archivo
            .encode("utf-8") # encodear a bytes
            ).hexdigest()
        _extension = filetype.guess(foto).extension
        img_filename = f"{_filename}.{_extension}"

        # 2. save img as a file
        foto.save(os.path.join(app.config["UPLOAD_FOLDER"], img_filename))

        # 3. save confession in db
    #print("Usuario en sesión:", repr(username))
        user = db.get_user_by_username(username)
        ave = db.get_ave(ave_avis)
        fecha = datetime.strptime(fecha_avis, "%Y-%m-%d")


        avis_id = db.create_avistamiento(user.id, ave.id, fecha, lugar_avis, comentario_avis)
    
    #db.create_registro(img_filename, img_filename, avis_id)
        db.create_registro(f"uploads/{img_filename}",img_filename,avis_id)


        return redirect(url_for("index"))
    else:
        return render_template("avistamientos/panel.html")
    #return "Avistamiento y registro guardados correctamente."

@app.route("/", methods=["GET"])
def index():
    
    if not session.get("user"):
        return redirect(url_for("portada"))

    data = db.get_avistamientos()

    for avis in data:
        for archivo in avis["archivos"]:
            archivo["url"] = url_for(
                "static", filename=archivo["ruta"]
            )

            extension = os.path.splitext(archivo["ruta"])[1].lower()
            archivo["es_video"] = extension in {
                ".mp4", ".webm", ".mov", ".avi", ".mkv", ".m4v"
            }

    return render_template("avistamientos/panel.html", data=data)