from wtforms import Form
from wtforms import StringField,PasswordField,EmailField,BooleanField,SubmitField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula=IntegerField("Matricula",[validators.DataRequired(message="El campo es requerido"),])
    nombre=StringField("Nombre",[validators.DataRequired(message="El campo es requerido"),
   ])
    apellido=StringField("Apellido",[validators.DataRequired(message="El campo es requerido"),
   ])
    correo=EmailField("Correo",[validators.DataRequired(message="El campo es requerido"),
   ])

class hChino(Form):
    dia = IntegerField("Día", [validators.DataRequired(message="El campo es requerido")])
    mes = IntegerField("Mes", [validators.DataRequired(message="El campo es requerido")])
    anio = IntegerField("Año", [validators.DataRequired(message="El campo es requerido")])
    nombre = StringField("Nombre", [validators.DataRequired(message="El campo es requerido")])
    apellidoP = StringField("Apellido Paterno", [validators.DataRequired(message="El campo es requerido")])
    apellidoM = StringField("Apellido Materno", [validators.DataRequired(message="El campo es requerido")])