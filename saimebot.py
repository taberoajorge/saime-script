import smtplib
from email.mime.text import MIMEText
import requests
import time

# Configuración del correo
# SENDER_EMAIL: La dirección de correo electrónico que se utilizará para enviar la notificación
SENDER_EMAIL = "tucorreo@gmail.com"
# RECEIVER_EMAIL: La dirección de correo electrónico a la que se enviará la notificación
RECEIVER_EMAIL = "elcorreoalquelequieresenviarlanotificacion"
# APP_PASSWORD: La contraseña de la aplicación que se generó en la cuenta de Gmail del remitente
APP_PASSWORD = "lacontraseñadeaplicacionquepuedesgenerarenGmail"

# Configuración del temporizador (en segundos)
# TIMER_INTERVAL: Intervalo entre intentos de verificación del estado de la página web
TIMER_INTERVAL = 5 * 60  # 5 minutos

def check_website_status(url):
    """
    Verifica el estado de la página web dada por la URL.
    
    Args:
        url (str): La URL de la página web a verificar.

    Returns:
        bool: True si la página está en línea (código de estado 200), False en caso contrario.
    """
    try:
        response = requests.get(url)
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

def main():
    """
    Verifica continuamente el estado de la página web y envía una notificación por correo electrónico cuando esté en línea.
    """
    # La URL de la página web que se desea verificar
    URL = "https://siic.saime.gob.ve/"

    # Bucle principal que verifica el estado de la página web
    while True:
        # Si la página web está en línea
        if check_website_status(URL):
            print("La página está en línea.")
            # Envía la notificación por correo electrónico
            send_email_notification(SENDER_EMAIL, RECEIVER_EMAIL, APP_PASSWORD, URL)
            # Detiene el bucle
            break
        else:
            # Si la página web no está en línea, espera TIMER_INTERVAL segundos antes de volver a intentarlo
            print(f"La página no está en línea. Reintentando en {TIMER_INTERVAL // 60} minutos.")
            time.sleep(TIMER_INTERVAL)

if __name__ == "__main__":
    main()
