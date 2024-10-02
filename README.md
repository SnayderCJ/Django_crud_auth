# Django CRUD con Autenticación y Despliegue Gratuito

✨ *Descripción*  

Este proyecto es una aplicación web completa desarrollada con Django, el framework de Python para el desarrollo de aplicaciones web backend.  El proyecto implementa un CRUD (Crear, Leer, Actualizar, Eliminar) completo, autenticación de usuarios (login y registro), protección de rutas y despliegue gratuito en Render.com.

🚀 *Características Principales*

* *CRUD Completo* Permite realizar operaciones CRUD sobre una base de datos (crear, leer, actualizar y eliminar registros).
* *Autenticación de Usuarios:* Incluye funcionalidades de registro de usuarios, inicio de sesión y cierre de sesión.
* *Protección de Rutas:* Restringe el acceso a ciertas partes de la aplicación a usuarios autenticados.
* *Panel de Administración de Django:* Aprovecha el potente panel de administración de Django para gestionar los datos de la aplicación.
* *Despliegue Gratuito:* La aplicación se puede desplegar de forma gratuita en Render.com, lo que facilita su acceso público.
* *Uso de Bootstrap 5:* La interfaz de usuario está diseñada con Bootstrap 5, proporcionando una apariencia moderna y responsiva.

🛠️ *Requerimientos*

* *Python (versión 3.7 o superior)*
* *Django (versión 3 o superior)*
* *Un editor de código o IDE (recomendado Visual Studio Code)*
* *Git (opcional, para el control de versiones)*

## ⚙️ Cómo Ejecutar la Aplicación  

1. *Clonar el repositorio:*
   ```bash
   git clone https://github.com/SnayderCJ/Django_crud_auth.git
   cd Django_crud_auth
   ```
    
3. *Crear (o activar) un entorno virtual::*   
    ```bash
    py -m venv venv  # Windows
    venv\Scripts\activate 

    python3 -m venv venv #Linux
    source venv/bin/activate
    ```

4. *Instalar las dependencias:*
    ```bash
    pip install -r requirements.txt
    ```

5. *Aplicar las migraciones:*
    ```bash
    py manage.py makemigrations
    py manage.py migrate
    ```

6. *Crear un superusuario:*
    ```bash
    py manage.py createsuperuser
    ```

7. *Ejecutar el servidor de desarrollo:*
    ```bash
    py manage.py runserver
    ```

8. *Acceder a la aplicación en tu navegador:*
    
    *   Abre tu navegador web y visita: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (para la interfaz principal)
    

9. *Iniciar sesión en el panel de administración:*
    
    *   Accede al panel de administración: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) (utiliza las credenciales del superusuario). que creaste en el paso 5.
    

## Despliegue en Render.com
Sigue las instrucciones detalladas en el video tutorial para desplegar tu aplicación en Render.com de forma gratuita.

## Contribuciones
Si encuentras algún error o tienes alguna sugerencia para mejorar el proyecto, no dudes en abrir un issue o enviar un pull request.

## Créditos
Este proyecto se basa en el tutorial de Fazt Code: Django CRUD con Autenticacion y Despliegue Gratuito
El código fuente original del curso de Django se encuentra en: https://github.com/fazt/django-notes

## Si tienes alguna pregunta o sugerencia, no dudes en contactarme. 😊 