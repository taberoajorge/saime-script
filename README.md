# Advertencias y descargos de responsabilidad: 
El presente script no es para ser utilizado con fines maliciosos, y que el usuario es responsable de cualquier uso indebido del script.


# Verificación del estado de la página web y notificación por correo electrónico

Este script de Python verifica si una página web está en línea y, si lo está, envía una notificación por correo electrónico utilizando la cuenta de Gmail del remitente. El script está escrito en Python 3 y utiliza las bibliotecas smtplib y requests.

## Requisitos previos

1. Python 3 instalado en tu sistema.
   - Windows: Descarga e instala Python 3 desde https://www.python.org/downloads/windows/
   - macOS: Descarga e instala Python 3 desde https://www.python.org/downloads/mac-osx/
   - Linux: La mayoría de las distribuciones de Linux tienen Python 3 preinstalado. Si no es así, consulta la documentación de tu distribución para obtener instrucciones sobre cómo instalar Python 3.

2. Biblioteca requests:

- `pip install requests`

3. Configura la verificación en dos pasos para tu cuenta de Google:
- Sigue las instrucciones en https://www.google.com/landing/2step/

4. Establece una contraseña de aplicación para tu cuenta de Google:
- Sigue las instrucciones en https://support.google.com/accounts/answer/185833?hl=es

## Configuración

1. Abre el script en un editor de texto y actualiza las siguientes variables con tus propios valores:

sender_email = "tucorreo@gmail.com"
receiver_email = "el correo al que le quieres enviar la notificacion"
app_password = "la contraseña de aplicacion que puede generar en gmail"


2. (Opcional) Cambia la URL en la función `check_website_status()` si deseas verificar una página web diferente.

## Uso

1. Abre una terminal o símbolo del sistema.

2. Navega hasta el directorio donde se encuentra el script.

3. Ejecuta el script con el siguiente comando:

- `python script.py`


Reemplaza "script.py" con el nombre del archivo si lo has cambiado.

El script verificará continuamente el estado de la página web e imprimirá un mensaje en la terminal cada minuto. Cuando la página esté en línea, enviará un correo electrónico de notificación y luego finalizará la ejecución.

## Nota importante

Este script utiliza una conexión SMTP segura para enviar correos electrónicos a través de Gmail. Sin embargo, no es recomendable almacenar contraseñas en texto plano en un archivo de código. Asegúrate de proteger tus credenciales adecuadamente y considera utilizar soluciones de almacenamiento seguro, como un administrador de contraseñas o variables de entorno.
