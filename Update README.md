Monitoreo y notificación de estado de página web

Este script monitorea el estado de una página web y envía una notificación por correo electrónico con una captura de pantalla cuando la página está en línea.

Requisitos

Para ejecutar este script se requiere tener instalado Python 3 y las siguientes librerías:

aiohttp
aiofiles
selenium
webdriver_manager
smtplib
Además, se necesita tener acceso a una cuenta de correo electrónico y una contraseña de aplicación para el remitente.

Uso

Para utilizar este script, sigue los siguientes pasos:

Clona este repositorio en tu máquina local.
Abre una terminal y navega hasta la carpeta donde se encuentra el script.
Ejecuta el siguiente comando en la terminal:
bash
Copy code
python main.py -s <correo electrónico remitente> -r <correo electrónico destinatario> -p <contraseña de aplicación>
Reemplaza <correo electrónico remitente> con la dirección de correo electrónico del remitente, <correo electrónico destinatario> con la dirección de correo electrónico del destinatario y <contraseña de aplicación> con la contraseña de aplicación generada para el remitente.

Una vez que se ejecuta el comando, el script monitoreará la página web especificada en la variable url (línea 11) y enviará una notificación por correo electrónico cuando la página esté en línea.

Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir a este proyecto, sigue los siguientes pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza los cambios necesarios y haz commit de tus cambios (git commit -am 'Agrega nueva funcionalidad').
Haz push a la rama (git push origin feature/nueva-funcionalidad).
Crea un pull request.
Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más información.