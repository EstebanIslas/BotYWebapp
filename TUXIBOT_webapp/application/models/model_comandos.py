import config as config # importa el archivo config

db = config.db # crea un objeto db del objeto db creado en config


#Metodo para seleccionar todos los registros de la tabla clientes

def select_comandos():
    try:
        return db.select('comandos') # Selecciona todos los registros de la tabla clientes
    except Exception as e:
        print "Model select_comandos Error {}".format(e.args)
        print "Model select_comandos Message {}".format(e.message)
        return None


#Metodo para seleccionar un registro que coincida con el nombre dado

def select_nombre(nombre):
    try:
        return db.select('comandos',where='nombre=$nombre', vars=locals())[0] # selecciona el primer registro que coincida con el nombre
    except Exception as e:
        print "Model select_nombre Error {}".format(e.args)
        print "Model select_nombre Message {}".format(e.message)
        return None


#Metodo para insertar un nuevo registro 

def insert_comandos(nombre,descripcion):
    try:
        return db.insert('comandos', 
        nombre=nombre,
        descripcion=descripcion) # inserta un registro en producto
    except Exception as e:
        print "Model insert_comandos Error {}".format(e.args)
        print "Model insert_comandos Message {}".format(e.message)
        return None


#Metodo para eliminar un registro que coincida con el nombre recibido

def delete_comandos(nombre):
    try:
        return db.delete('comandos', where='nombre=$nombre',vars=locals()) # borra un registro de clientes
    except Exception as e:
        print "Model delete_comandos Error {}".format(e.args)
        print "Model delete_comandos Message {}".format(e.message)
        return None


#Metodo para actualizar los datos, del nombre recibido

def update_comandos(nombre,descripcion): # actualiza los datos de la tabla clientes que coincidan con el nombre
    try:
        return db.update('comandos',
            descripcion=descripcion, 
            where='nombre=$nombre',
            vars=locals())
    except Exception as e:
        print "Model update_comandos Error {}".format(e.args)
        print "Model update_comandos Message {}".format(e.message)
        return None
