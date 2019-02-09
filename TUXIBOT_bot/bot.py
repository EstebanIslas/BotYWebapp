from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO) #configura una variable para guardar los sucesos
logger = logging.getLogger(__name__)

# Database connection
db = web.database( #Conexion de base de datos
    dbn = 'mysql',
    host = 'localhost',
    db = 'linux',
    user = 'lin',
    pw = 'lin.2019',
    port = 3306
    )

 
token = '667739360:AAHVyE7XitbjwO4TqaRa1e-kRAts1RGw8Qk' #Clave con la se conecta el bot BotFather Icono de nave apuntando hacia arriba En este campo se coloca la url de la api use this token to api

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update): #Define Start para ser lo primero que se ejecuta
    username = update.message.from_user.username #Almacena el nombre de usuario a cuenta de telegram 
    update.message.reply_text('Bienvenido!! {} Utiliza este comando para consultar informacion:\n/comand + <<Comando que deseas>>'.format(username)) #Busqueda de informacion

def help(bot, update): #Funcion basica para la ayuda explicacion
    username = update.message.from_user.username
    update.message.reply_text('Bienvenido!! {} Utiliza este comando para consultar informacion:\n/comand + <<Comando que deseas>>'.format(username))

def search(update): #
    text = update.message.text.split() #Variable text guarda la cadena que el usuario escribe split corta cadena cada que escribe un espacio
    username = update.message.from_user.username
    try:
        nombre = str(text[1]) 
        print "Send comand to {}".format(username) #imprimir lo que sucede en la consola
        print "Key search {}".format(nombre)
        result = db.select('comandos', where='nombre=$nombre', vars=locals())[0] #Consulta de la base de datos var locals reconoce como variable $nombre [0] primer registro que encuentra
        print result #imprime resultado de la consulta
        respuesta = str(result.nombre) + "\nY consiste en " + str(result.descripcion) #Concatena los tres parametros


        update.message.reply_text('El comando que ingresaste {}es:\n{}'.format(username, respuesta)) #regresa la informacion al usuario
    except Exception as e:
        print "Error: " + str(e.message)
        update.message.reply_text('El comando que ingresaste {} es incorreto'.format(nombre))

def comand(bot, update):
    search(update)

def echo(bot, update): #Comportamiento del bot repite lo que escribe
    update.message.reply_text(update.message.text)
    print update.message.text #Cuando
    print update.message.date #Cuando
    print update.message.from_user #Quien
    print update.message.from_user.username #
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'TUXIBOT init token'
        
        updater = Updater(token) #Se crea el usuario y se conecta con la api 

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'TUXIBOT init dispatcher'

        # on different commands - answer in Telegram
        dp.add_handler(CommandHandler("start", start)) #Comandos que queremos que utilice nuestro bot
        dp.add_handler(CommandHandler("help", help)) #apunta a las definiciones
        dp.add_handler(CommandHandler("comand", comand)) #apunta a las definiciones

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo)) #Prepara el bot para que regrese lo que escribe el usuario

        # log all errors
        dp.add_error_handler(error) #Almacena errores

        # Start the Bot
        updater.start_polling() #Inicializa el bot para recibir peticiones

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'TUXIBOT ready'
        updater.idle() #Modo de espera
    except Exception as e:
        print "TUXIBOT found Error 100: ", e.message

if __name__ == '__main__': #Ejecutar el bot
    main()
