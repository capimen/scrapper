import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sendMailHelper
from SqlHelper import SqlHelper

def sendMail():
    sqlHelper = SqlHelper()
    cAllUser = sqlHelper.select_all_users()

    for row in cAllUser:
        # Configura los datos de tu cuenta de Gmail
        email_usuario = "capimen@gmail.com"
        contrasena = "juvw gppi fnvq ohkq"

        # Crea el mensaje
        mensaje = MIMEMultipart()
        mensaje["From"] = email_usuario
        mensaje["To"] = str(row[2])
        mensaje["Subject"] = "libros destacados para " + str(row[1])

        # Cuerpo del mensaje
        cuerpo = sendMailHelper.get_HTMLHighLight(row[1])

        if cuerpo is not None:

            mensaje.attach(MIMEText(cuerpo, "html"))

            # Conéctate al servidor SMTP de Gmail
            servidor_smtp = smtplib.SMTP("smtp.gmail.com", 587)
            servidor_smtp.starttls()

            # Inicia sesión en tu cuenta de Gmail
            servidor_smtp.login(email_usuario, contrasena)

            # Envía el mensaje
            texto_del_mensaje = mensaje.as_string()
            servidor_smtp.sendmail(email_usuario, row[2], texto_del_mensaje)

            # Cierra la conexión
            servidor_smtp.quit()

            print("El correo ha sido enviado correctamente.")
        else:
            print("usuario "+row[1]+" sin datos")

