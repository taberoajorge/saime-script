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
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def send_email_notification(sender_email,receiver_email,app_password):
    message = MIMEText("La página está en línea.", "plain", "utf-8")
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

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    global_config = load_config()
    logging.debug(str(global_config))
    while global_config['url']:
        logging.debug(f"Intentando url: {global_config['url']}")
        if check_website_status(global_config["url"]):
            print(f"La página {global_config['url']} está en línea.")
            email_config_ready = all([global_config["sender_email"], global_config["receiver_email"], global_config["app_password"]])
            if not email_config_ready:
                print("No se puede enviar el correo porque falta configuración. Revise el archivo config.json (ignorando error...)")
            else:
                send_email_notification(global_config["sender_email"], global_config["receiver_email"], global_config["app_password"])
            break
        else:
            print("La página no está en línea. Reintentando en 1 minuto.")
            time.sleep(60)
