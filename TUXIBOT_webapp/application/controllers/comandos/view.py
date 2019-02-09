import web
import config as config


class View:
    def __init__(self):
        pass

    def GET(self, nombre):  
        comandos = config.model_comandos.select_nombre(nombre) # Selecciona el registro que coincida con nombre
        return config.render.view(comandos) # Envia el registro y renderiza view.html
