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

Para este caso en particular, tendremos un docker-compose para crear nuestra base de datos, que ya nos facilitará un poco la ejecución del proyecto.
Entonces ejecutamos el siguiente comando

docker-compose up -d

Al tener la bd creada, entonces crearemos migraciones del proyecto con el siguiente comando

python manage.py makemigrations

Y aplicaremos estas sobre la bd, para poder registrar nuestras tablas con base a los modelos reconocidos

python manage.py migrate

Crearemos un superusuario para realizar las consultas en swagger posteriormente

python manage.py createsuperuser

Ingresaremos nuestro correo y una contraseña, evitando que el correo sea duplicado pues es un campo unique.

También ejecutaremos el comando collectstatic, para poder tener todos los archivos estáticos del proyecto

python manage.py collectstatic

Tras esto ya podemos ejecutar el proyecto

python manage.py runserver