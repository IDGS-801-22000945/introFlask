from flask import Flask, render_template #IMPORTANTE IMPORTAR FLASK

app=Flask(__name__)

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
@app.route("/")
def index():
    titulo="IDGS801"
    lista=["Jaqueline","Rafael","Viviana"]
    return render_template("index.html",titulo=titulo,lista=lista)


@app.route("/ejemplo1")
def ejemplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejemplo2():
    return render_template("ejemplo2.html")

# Sin bajar el servidor se pone app.run(debug=True)
# Cambiar el puerto app.run(debug=True,port=3000)
if __name__ == "__main__":
    app.run(debug=True,port=3000)