import web
import config as config


class Index:
    def __init__(self):
        pass

    def GET(self):  
        comandos = config.model_comandos.select_comandos().list() # Selecciona todos los registros de producto
        return config.render.index(comandos) # Envia registros y renderiza index.html
