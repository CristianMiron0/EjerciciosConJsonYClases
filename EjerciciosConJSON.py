# 1.
import json

'''
{"nombre": "Juan", "edad": 30, "email": "juan@acme.com", "trabajo": {"empresa": "Acme Corp", "puesto": "Ingeniero de software"}}
'''

nombre = input("Ingrese el nombre del usuario: ")
edad = int(input("Ingrese la edad del usuario: "))
email = input("Ingrese el correo electrónico del usuario: ")
empresa = input("Ingrese el nombre de la empresa en la que trabaja el usuario: ")
puesto = input("Ingrese el puesto del usuario en la empresa: ")

usuario = {
    "nombre": nombre,
    "edad": edad,
    "email": email,
    "trabajo": {
        "empresa": empresa,
        "puesto": puesto
    }
}

usuarioJson = json.dumps(usuario)

print(usuarioJson)

# 2.
import json

'''
{"id": 123456789, "fechayhora": "2023-04-18T12:30:00Z", "monto": 500.25, "tipo": "compra", "producto": {"nombre": "Smartphone", "precio": 450.00, "descripcion": "Un teléfono inteligente de última generación"}}
'''

id = int(input("Ingrese el ID: "))
fechayhora = input("Ingrese la fecha y hora (en formato ISO): ")
monto = float(input("Ingrese el monto: "))
tipo = input("Ingrese el tipo de transacción: ")
nombreProducto = input("Ingrese el nombre del producto: ")
precioProducto = float(input("Ingrese el precio del producto: "))
descripcionProducto = input("Ingrese una descripción del producto: ")

producto = {
    "nombre": nombreProducto,
    "precio": precioProducto,
    "descripcion": descripcionProducto
}
transaccion = {
    "id": id,
    "fechayhora": fechayhora,
    "monto": monto,
    "tipo": tipo,
    "producto": producto
}

transaccionJson = json.dumps(transaccion)

print(transaccionJson)

# 3.
import json
'''
{"nombre": "Pedro", "apellido": "Pérez", "edad": 45, "peso": 80.5, "altura": 1.75, 
"historial_medico": {"alergias": ["penicilina", "mariscos"], 
"problemas_cardiacos": false, 
"medicamentos": [{"nombre": "Ibuprofeno", "dosis": "200mg"}, {"nombre": "Paracetamol", "dosis": "500mg"}]}, 
"ultima_revision": "2022-10-01", "proximo_turno": "2023-05-15"}
'''
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

alergias = input("Ingrese sus alergias separadas por coma (si no tiene, deje vacío): ")
alergias = alergias.split(",") if alergias else []

problemas_cardiacos = input("¿Tiene problemas cardiacos? (s/n): ").lower()
if problemas_cardiacos == "s":
    problemas_cardiacos = True
else:
    problemas_cardiacos = False

medicamentos = []
while True:
    medicamento_nombre = input("Ingrese el nombre del medicamento (o 'fin' para terminar): ")
    if medicamento_nombre == "fin":
        break
    medicamento_dosis = input("Ingrese la dosis del medicamento: ")
    medicamento = {
        "nombre": medicamento_nombre,
        "dosis": medicamento_dosis
    }
    medicamentos.append(medicamento)

ultima_revision = input("Ingrese la fecha de su última revisión médica (formato YYYY-MM-DD): ")
proximo_turno = input("Ingrese la fecha de su próximo turno médico (formato YYYY-MM-DD): ")

informacion = {
    "nombre": nombre,
    "apellido": apellido,
    "edad": edad,
    "peso": peso,
    "altura": altura,
    "historial_medico": {
        "alergias": alergias,
        "problemas_cardiacos": problemas_cardiacos,
        "medicamentos": medicamentos
    },
    "ultima_revision": ultima_revision,
    "proximo_turno": proximo_turno
}
informacion = input("Entre JSON:")

json_informacion = json.dumps(informacion)

print(json_informacion)