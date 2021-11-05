from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import json
from usuario import Usuario

app = Flask(__name__)
CORS(app)

listaUsuarios = []

@app.route("/", methods=["GET"])
def get():
   global listaUsuarios
   
   Datos = []
   
   print("GET method")
   
   for user in listaUsuarios:
       usuario = {
           "Id":user.getId(),
           "Nombre":user.getNombre(),
           "Apellido":user.getApellido(),
           "Telefono":user.getTelefono()
       }
       Datos.append(usuario)
       
   return jsonify(Datos)


@app.route("/", methods=["POST"])
def post():
    global listaUsuarios
    
    userId = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    telefono = request.json['telefono']
    
    print("POST data:", [userId,nombre,apellido,telefono])
    
    listaUsuarios.append(Usuario(userId,nombre,apellido,telefono)) 
    
    mensaje = {
        "Mensaje":"Se ha agregado el usuario: " + nombre
    }

    return jsonify(mensaje)


@app.route("/", methods=["PUT"])
def put():
    global listaUsuarios
    
    userId = request.json['id']
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    telefono = request.json['telefono']
    
    print("PUT data:", [userId,nombre,apellido,telefono])
    
    found = False
    
    for user in listaUsuarios:
        if userId == user.getId():
            user.id = userId
            user.nombre = nombre
            user.apelido = apellido
            user.telefono = telefono
            found = True
    
    mensaje = {
        "Mensaje":"Se ha actualizado el usuario: " + nombre
    }
    
    if not found:
        listaUsuarios.append(Usuario(userId,nombre,apellido,telefono)) 
        mensaje = {
            "Mensaje":"Se ha creado el usuario: " + nombre
        }
        
    return jsonify(mensaje)
    


@app.route("/", methods=["DELETE"])
def delete():
    global listaUsuarios
    listaUsuarios = []
    
    print("DELETE method")
    
    objeto = {
        "Index":"Se ha borrado la lista"
    }

    return jsonify(objeto)


if __name__ == "__main__":
    app.run(threaded=True, debug=True)