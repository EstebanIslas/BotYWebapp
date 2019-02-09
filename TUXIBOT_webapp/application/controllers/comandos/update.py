import web
import config as config


class Update:
    def __init__(self):
        pass

    def GET(self, nombre): 
        comandos = config.model_comandos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.update(comandos) # Envia el registro y renderiza update.html
    
    def POST(self,nombre):
        formulario = web.input() # almacena los datos del formulario
        nombre = formulario['nombre'] # almacena el nombre escrito en el input
        descripcion = formulario['descripcion'] # almacena el contenido escrito en el input
        config.model_comandos.update_comandos(nombre, descripcion)
        raise web.seeother('/') # redirecciona al index
