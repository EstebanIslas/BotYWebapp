import web
import application.models.model_comandos as model_comandos # importa el modelo_comandos


render = web.template.render('application/views/comandos/', base='master')
