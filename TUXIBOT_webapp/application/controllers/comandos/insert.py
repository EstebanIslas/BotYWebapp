import web
import config as config


class Insert:
    def __init__(self):
        pass

    def GET(self):  
        return config.render.insert() # renderiza la pagina insert.html
    
    def POST(self):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        descripcion = formulario['descripcion'] # almacena el contenido escrito en el input
        config.model_comandos.insert_comandos(nombre, descripcion) # llama al metodo insert_clientes y le paso los datos guardados
        raise web.seeother('/') # redirecciona al index.html
