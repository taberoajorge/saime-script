import smtplib
from email.mime.text import MIMEText
import requests
import time

# aqui puedes usar un correo de gmail el que vas a destinar para enviarte los correos
sender_email = "tucorreo@gmail.com" 

# aqui vas a configurar elc correo receptor 
receiver_email = "el correo al que le quieres enviar la notificacion"

# Aqui es la contraseña de aplicacion https://support.google.com/accounts/answer/185833?hl=es 
app_password = "la contraseña de applicacion que puede generar en gmail"

# aqui es donde puede haber cualquier url
url = "https://siic.saime.gob.ve/"

def check_website_status():
    try:
        response = requests.get(url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def send_email_notification():
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

while True:
    if check_website_status():
        print("La página está en línea.")
        send_email_notification()
        break
    else:
        print("La página no está en línea. Reintentando en 1 minuto.")
        time.sleep(60)
