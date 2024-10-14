# MB_Inn_lab_OLCE
Prueba técnica de MB para puesto de backend

# Primeros pasos

De inicio instalaremos por medio de un comando de python (pip) un ambiente virtual, para instalar nuestros requerimientos

pip install venv

Una vez instalado, entonces procedemos a crear un ambiente virtual

python -m venv env

En este caso, yo le puse env al ambiente virtual, para que sea un poco descriptivo por sí solo sobre qué es

Ya que creamos el ambiente, entonces podemos proseguir y usarlo

source env/Scripts/activate

# Instalación de dependencias del proyecto

Ya que tenemos nuestro ambiente listo, entonces podemos instalar todo lo que se requiere para inicializar el proyecto

pip install -r requirements.txt

# Ejecución del proyecto

Para este caso en particular, tendremos un docker-compose y un Dockerfile, que ya nos facilitarán un poco la ejecución del proyecto y de la base de datos requerida.
Entonces ejecutamos el siguiente comando

docker-compose up -d
