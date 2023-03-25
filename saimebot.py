import smtplib
import requests
import time
import json
import logging

from email.mime.text import MIMEText

def load_config():
    with open("./config.json","r") as f:
        config = json.load(f)

    return config or {"url":""}

def check_website_status(url, timeout=30):
    """
    Verifica el estado de la página web dada por la URL.
    
    Args:
        url (str): La URL de la página web a verificar.

    Returns:
        bool: True si la página está en línea (código de estado 200), False en caso contrario.
    """
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def send_email_notification(sender_email, receiver_email, app_password, url):
    """
    Envía una notificación por correo electrónico utilizando la dirección de correo electrónico del remitente.
    
    Args:
        sender_email (str): La dirección de correo electrónico del remitente.
        receiver_email (str): La dirección de correo electrónico del destinatario.
        app_password (str): La contraseña de la aplicación para la cuenta del remitente.
        url (str): La URL de la página web que fue verificada.
    """
    message = MIMEText(f"La página está en línea, puedes acceder desde {url}", "plain", "utf-8")
    message["Subject"] = "Notificación: Página en línea"
    message["From"] = sender_email
    message["To"] = receiver_email
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

def main(global_config, logging):
    """
    Verifica continuamente el estado de la página web y envía una notificación por correo electrónico cuando esté en línea.
    """

    while global_config['url']: # el loop va a ejecutar siempre y cuando la url se haya proporcionado en el config.json
        logging.debug(f"Intentando url: {global_config['url']}") 
        if check_website_status(global_config["url"], global_config["timeout"]):
            print(f"La página {global_config['url']} está en línea.")
            email_config_ready = all([global_config["sender_email"], global_config["receiver_email"], global_config["app_password"]]) # validar que todos los requerimientos para enviar el email se cumplen
            if not email_config_ready:
                print("No se puede enviar el correo porque falta configuración. Revise el archivo config.json (ignorando error...)")
            else:
                send_email_notification(global_config["sender_email"], global_config["receiver_email"], global_config["app_password"], global_config["url"])
            break
        else:
            print(f"La página no está en línea. Reintentando en {global_config['wait_time_interval']} segundos.")
            time.sleep(global_config["wait_time_interval"])

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    ) # usar logging para separar los mensajes de desarrollo y producción
    global_config = load_config() # cargar valores de config.json
    logging.debug(str(global_config))
    main(global_config, logging)
