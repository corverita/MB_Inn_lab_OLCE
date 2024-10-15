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

También habrá que modificar nuestras variables de entorno (.env-example) para tener nuestros puertos y otras configuraciones funcionando.
Para leer y tener en cuenta las variables de entorno al ejecutar el proyecto, ejecutaremos el siguiente comando

source .env-example

Con esto se cargarán las variables y podremos tener toda nuestra configuración de conexión y de autenticación/autorización para las bases de datos.

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

# Uso del proyecto

Podemos utilizar la url

http://localhost:8000/swagger/

Para entrar al API desarrollado y poder utilizar la misma como si fuera desde postman aunque a un nivel más sencillo o automatizado.

También podemos entrar a 

http://localhost:8000/admin/

Para entrar al panel de administración, que realmente en este caso se dejó medio vacío, pero si es necesario pues este está habilitado