CREATE DATABASE linux;

USE linux;

CREATE TABLE comandos(
    nombre varchar(50) NOT NULL PRIMARY KEY,
    descripcion varchar(250) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;


INSERT INTO comandos (nombre, descripcion) VALUES 
('sudo','Permite ejecutar programas u otros comandos con privilegios administrativos'),
('cd','Cambiar el directorio de trabajo actual'),
('pwd','Muestra la ruta completa del directorio de trabajo actual'),
('ls','Lista todos los archivos y carpetas en el directorio de trabajo'),
('cp','Copy, permite copiar un archivo se debe especificar tanto el archivo que se desea copiar como la ubicacion'),
('mv','Mover, permite mover archivos se debe especificar tanto el archivo que se desea mover como la ubicacion'),
('rm','Eliminar un archivo especifico'),
('mkdir','permite crear un nuevo directorio'),
('nano','Abrir editor de texto'),
('gedit','Abrir editor de texto'),
('sort','Ordenar todos los archivos y carpetas del directorio de trabajo actual');

SHOW TABLES;

SELECT * FROM comandos;

DESCRIBE comandos;

CREATE USER 'lin'@'localhost' IDENTIFIED BY 'lin.2019';
GRANT ALL PRIVILEGES ON linux.* TO 'lin'@'localhost';
FLUSH PRIVILEGES;
