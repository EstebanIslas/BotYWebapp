import web
        
urls = (
    '/', 'application.controllers.comandos.index.Index',
    '/insert', 'application.controllers.comandos.insert.Insert',
    '/update/(.*)', 'application.controllers.comandos.update.Update',
    '/delete/(.*)', 'application.controllers.comandos.delete.Delete',
    '/viewcomandos/(.*)', 'application.controllers.comandos.view.View',
    
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
