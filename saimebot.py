import argparse
import asyncio
import aiohttp
import smtplib
import os

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

url = "https://siic.saime.gob.ve/"



async def check_website_status():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return response.status == 200
    except aiohttp.ClientError:
        return False

async def take_screenshot():
    options = Options()
    options.add_argument("--headless")
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    try:
        driver.get(url)
        screenshot_path = os.path.join(os.getcwd(), 'screenshot.png')
        loop = asyncio.get_event_loop()
        screenshot_data = await loop.run_in_executor(None, driver.get_screenshot_as_png)

        with open(screenshot_path, 'wb') as f:
            f.write(screenshot_data)

    finally:
        driver.quit()

    return screenshot_path

async def send_email_notification(screenshot_path):
    message = MIMEMultipart()
    message["Subject"] = "Notificación: Página en línea"
    message["From"] = sender_email
    message["To"] = receiver_email
    message.attach(MIMEText("La página está en línea.", "plain", "utf-8"))

    with open(screenshot_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header("Content-Disposition", "attachment", filename="screenshot.png")
        message.attach(img)

    try:
        loop = asyncio.get_event_loop()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            await loop.run_in_executor(None, server.login, sender_email, app_password)
            await loop.run_in_executor(None, server.sendmail, sender_email, receiver_email, message.as_string())
            print("Correo electrónico enviado correctamente.")
    except Exception as e:
        print(f"Error al enviar el correo electrónico: {e}")

async def main(sender_email, receiver_email, app_password):
    while True:
        if await check_website_status():
            print("La página está en línea.")
            screenshot_path = await take_screenshot()
            #await send_email_notification(screenshot_path)
            break
        else:
            print("La página no está en línea. Reintentando en 1 minuto.")
            await asyncio.sleep(60)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Este script monitorea el estado de una página web y envía una notificación por correo electrónico con una captura de pantalla cuando la página está en línea.')

    parser.add_argument('-s', '--sender', required=True, help='Dirección de correo electrónico del remitente. Ejemplo: "tucorreo@gmail.com"')
    parser.add_argument('-r', '--receiver', required=True, help='Dirección de correo electrónico del destinatario. Ejemplo: "destinatario@gmail.com"')
    parser.add_argument('-p', '--password', required=True, help='Contraseña de aplicación del remitente. Puedes generar una contraseña de aplicación en la configuración de tu cuenta de correo electrónico.')

    args = parser.parse_args()

    sender_email = args.sender
    receiver_email = args.receiver
    app_password = args.password

    asyncio.run(main(sender_email, receiver_email, app_password))
