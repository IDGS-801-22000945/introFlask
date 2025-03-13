from flask import Flask, render_template,request #IMPORTANTE IMPORTAR FLASK
import forms 
from flask_wtf.csrf import CSRFProtect
from flask import g
from flask import flash
from forms import hChino


csrf=CSRFProtect()

app=Flask(__name__)
#Crear clave
csrf=CSRFProtect(app)
app.secret_key="12345"


@app.route("/hola")
def hola():
    return "<h1>Hola mundo!</h1>"

#Pasar parametros de tipo float, entero, String
@app.route("/user/<string:user>")
def user(user):
    return f"<h1> ¡Hola, {user}</h1>"

@app.route("/numero/<int:n>")
def num(n):
    return f"<h1> El numero es: {n}</h1>"


@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1> Hola, {username}. Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"La suma es: {n1+n2}"

@app.route("/default/")
@app.route("/default/<string:parm>")
def func(param="Jaqui"):
    return  f"<h1>Hola, {param}! </h1>"



@app.route("/")
def index():
    nom="None"
    titulo="IDGS801"
    lista=["Jaqueline","Rafael","Viviana"]
    nom=g.user
    print("Index 2 {}".format(nom))
    return render_template("index.html",titulo=titulo,lista=lista)

@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")


@app.route("/operas")
def operas():
    return '''
         <form>
    <label for="name"> Name: </label>
    <input type="text" id="name" name="name" required>

    <label for="name"> Paterno: </label>
    <input type="text" id="name" name="name" required>

    </form>
'''
'''
@app.route("/OperasBas",methods=["GET","POST"])
def OperasBas():
    return render_template("OperasBas.html")
'''

@app.route("/OperasBas", methods=["GET", "POST"])
def OperasBas():
    resultado = None
    operacion_str = "Operación no válida"

    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if n1 and n2:
            n1 = int(n1)
            n2 = int(n2)
            if operacion == 'suma':
                resultado = n1 + n2
                operacion_str = 'Suma'
            elif operacion == 'resta':
                resultado = n1 - n2
                operacion_str = 'Resta'
            elif operacion == 'div':
                if n2 != 0:
                    resultado = n1 / n2
                    operacion_str = 'División'
                else:
                    resultado = "Error: División por cero"
                    operacion_str = "Operación no válida"
            elif operacion == 'mul':
                resultado = n1 * n2
                operacion_str = 'Multiplicación'
    
    return render_template("OperasBas.html", resultado=resultado, operacion=operacion_str)

@app.route("/cinepolis", methods=["GET", "POST"])
def cine():
    total = 0
    descuento = 0
    mensaje = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        cantCompradores = int(request.form.get("cantCompradores"))
        cantBoletos = int(request.form.get("cantBoletos"))
        tarjeta_cineco = request.form.get("tarjeta_cineco")

        total = cantBoletos * 12

        if 3 <= cantBoletos <= 5:
            descuento = total * 0.1
        elif cantBoletos > 5:
            descuento = total * 0.15

        total -= descuento

        if cantBoletos > (cantCompradores * 7):
            mensaje = f"No puedes comprar más de {cantCompradores * 7} boletos para {cantCompradores} personas."
            total = 0
        else:
            if tarjeta_cineco == 'si':
                descuentoTarjeta = total * 0.1
                total -= descuentoTarjeta

    return render_template("cinepolisFlask.html", mensaje=mensaje, total=total)

@app.route("/zodiaco", methods=["GET", "POST"])
def zodiaco():
    anio = 0
    dia = 0
    mes = 0
    edad = 0
    nombre = ""
    apellidoP = ""
    apellidoM = ""
    
    animales = [
        "Mono", "Gallo", "Perro", "Cerdo", "Rata", "Buey",
        "Tigre", "Conejo", "Dragón", "Serpiente", "Caballo", "Cabra"
    ]
    imagenes = [
        "mono.jpg", "gallo.jpg", "perro.jpg", "cerdo.jpg", "rata.jpg", "buey.jpg",
        "tigre.jpg", "conejo.jpg", "dragon.jpg", "serpiente.jpg", "caballo.jpg", "cabra.jpg"
    ]

    resultado = ""
    signo_imagen = ""
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellidoP = request.form.get("apellidoP")
        apellidoM = request.form.get("apellidoM")
        anio = int(request.form.get("anio"))
        edad = 2025 - anio
        iAnimal = anio % 12
        animal = animales[iAnimal]
        signo_imagen = imagenes[iAnimal]
        resultado = f"Hola, {nombre} {apellidoP} {apellidoM}, tienes {edad} años. Tu signo zodiacal es: {animal}."

    return render_template("zodiaco.html", animales=animales, resultado=resultado, signo_imagen=signo_imagen)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.before_request
def before_request():
    g.user = "Jaqui"
    print("before1")

@app.after_request
def after_request(response):
    print("after1")
    return response



@app.route("/alumnos", methods=["GET", "POST"])
def alumnos():
    mat=''
    nom=''
    ape=''
    email=''
    alummo_clas=forms.UserForm(request.form)
    if request.method == 'POST' and alummo_clas.validate():
        mat=alummo_clas.matricula.data
        nom=alummo_clas.nombre.data
        ape=alummo_clas.apellido.data
        email=alummo_clas.correo.data

        mensaje="Bienvenido {}".format(nom)
        flash(mensaje)

    return render_template("alumnos.html", form=alummo_clas,mat=mat,nom=nom,ape=ape,email=email)

@app.route("/hChino", methods=["GET", "POST"])
def chino():
    hChino = forms.hChino(request.form) 
    dia = ''
    mes = '' 
    anio = ''
    nombre = ''
    apellidoP = ''
    apellidoM = ''
    
    if request.method == 'POST' and hChino.validate():
        dia = hChino.dia.data
        mes = hChino.mes.data
        anio = hChino.anio.data
        nombre = hChino.nombre.data
        apellidoP = hChino.apellidoP.data
        apellidoM = hChino.apellidoM.data

        flash(f"Bienvenido {nombre}")

    return render_template("chinoHoros.html", form=hChino, dia=dia, mes=mes, anio=anio, nombre=nombre, apellidoP=apellidoP, apellidoM=apellidoM)

# Sin bajar el servidor se pone app.run(debug=True)
# Cambiar el puerto app.run(debug=True,port=3000)
if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)