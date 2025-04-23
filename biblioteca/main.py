from models import Libro, Usuario, IniciarSesion
from fastapi import FastAPI

app=FastAPI()

libros_db = []
usuarios_db = []
rol = str("invitado")

### CREAR LIBRO
@app.post("/libros/",response_model=Libro)
def crear_libro(nuevo_libro:Libro):
    libros_db.append(nuevo_libro)
    return nuevo_libro
###

### OBTENER TODOS LOS LIBROS
@app.get("/libros/",response_model=list[Libro])
def obtener_libros():
    return libros_db
###

### OBTENER LIBRO POR ID
@app.get("/libros/{libro_id}",response_model=Libro)
def obtener_libro(libro_id: int):
    for x in libros_db:
        if x.id == libro_id:
            return x
    return {"ERROR" : "Libro no encontrado"}
###

### BORRAR LIBRO
@app.delete("/libros/{libro_id}")
def eliminar_libro(libro_id: int):
    for x in libros_db:
        if x.id == libro_id:
            libros_db.remove(x)
            return {"Mensaje" : "Libro eliminado"}
    return {"ERROR" : "Libro no encontrado"}
###


###REGISTRAR USUARIO
@app.post("/usuarios/",response_model=Usuario)
def registrar_usuario(nuevo_usuario:Usuario):
    usuarios_db.append(nuevo_usuario)
    return nuevo_usuario
###

### INICAR SESION
@app.post("/usuarios/login")
def iniciar_sesion(usuario:IniciarSesion):
    for x in usuarios_db:
        if x.id == usuario.id:
            if x.contrasena == usuario.contrasena:
                rol= x.rol
                return {"Mensaje" : "Inicio de sesión exitoso"}
            return {"ERROR" : "Contraseña incorrecta"}
    return {"ERROR" : "Usuario no encontrado"}
###