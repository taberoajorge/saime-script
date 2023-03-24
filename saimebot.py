import smtplib
import requests
import time
import json

from email.mime.text import MIMEText

# aqui puedes usar un correo de gmail el que vas a destinar para enviarte los correos
#sender_email = "tucorreo@gmail.com" 

# aqui vas a configurar elc correo receptor 
#receiver_email = "el correo al que le quieres enviar la notificacion"

# Aqui es la contraseña de aplicacion https://support.google.com/accounts/answer/185833?hl=es 
#app_password = "la contraseña de applicacion que puede generar en gmail"

def load_config():
    with open("./config.json","r") as f:
        config = json.load(f)
    return config or {}

def check_website_status(url):
    try:
        response = requests.get(url)
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
    global_config = load_config()
    while True:
        if check_website_status(global_config["url"]):
            print(f"La página {global_config['url']} está en línea.")
            if global_config["sender_email"] is None or global_config["receiver_email"] is None or global_config["app_password"] is None:
                print("No se puede enviar el correo porque falta configuración. Revise el archivo config.json (ignorando error...)")
            else:
                send_email_notification(global_config["sender_email"],
                                        global_config["receiver_email"], 
                                        global_config["app_password"])
            break
        else:
            print("La página no está en línea. Reintentando en 1 minuto.")
            time.sleep(60)
