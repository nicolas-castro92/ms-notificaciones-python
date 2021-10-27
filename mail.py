 

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import variables
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask import request
from flask import Flask
from twilio.rest import Client

app = Flask(__name__)
'''
@app.route("/")
def hello():
    return "Hello, World!"
'''
@app.route("/correo")
def enviarCorreo():
    hashString = request.args.get("hash")
    #print(hashString)
    #print(os.environ.get('SECURITY_HASH'))
    #print(os.environ.get('SENDGRID_API_KEY'))
    if (hashString == os.environ.get('SECURITY_HASH')):
        destino = request.args.get("destino")
        asunto = request.args.get("asunto")
        mensaje = request.args.get("mensaje")
        #print(destino, asunto, mensaje, hashString)
        if destino == None or asunto == None or mensaje == None:
            print('campos invalidos')
            return 'mensaje no enviado, verifique que todos los campos esten correctos destino, asunto y mensaje'
        else:
            message = Mail(
                from_email=os.environ.get("email_from"),
                to_emails=destino,
                subject=asunto,
                html_content=mensaje)
            try:
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print("mensaje enviado")
                return "el mensaje fue enviado correctamente"
            except Exception as e:
                print(e.message)
                return "KO"
            print('error de exception')
            return 'ha ocurrido un error'

    else:
        print('hash invalido')
        return 'hash invalido, ingrese uno valido por favor'
    print('por aqui terminado')
    return 'terminado'

@app.route("/sms")
def enviarSms():
    hashString = request.args.get("hash")
    #print(hashString)
    #print(os.environ.get('SECURITY_HASH'))
    #print(os.environ.get('SENDGRID_API_KEY'))
    if (hashString == os.environ.get('SECURITY_HASH')):
        destino = request.args.get("destino")
        mensaje = request.args.get("mensaje")
        #print(destino, asunto, mensaje, hashString)
        if destino == None or mensaje == None:
            print('campos invalidos')
            return 'mensaje no enviado, verifique que todos los campos esten correctos destino, asunto y mensaje'
        else:
            try:
                account_sid = os.environ['TWILIO_ACCOUNT_SID']
                auth_token = os.environ['TWILIO_AUTH_TOKEN']
                client = Client(account_sid, auth_token)

                message = client.messages \
                    .create(
                    body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                    from_='+15017122661',
                    to='+15558675310'
                )

                print(message.sid)
                print("mensaje enviado")
                return "el mensaje fue enviado correctamente"
            except Exception as e:
                print(e.message)
                return "KO"
            print('error de exception')
            return 'ha ocurrido un error'

    else:
        print('hash invalido')
        return 'hash invalido, ingrese uno valido por favor'
    print('por aqui terminado')
    return 'terminado'


if __name__=="__main__":
    app.run()









'''

message = Mail(
    from_email='nicolas.1701322569@ucaldas.edu.co',
    to_emails='nicucg@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
'''
'''
    message = Mail(
        from_email='nicolas.1701322569@ucaldas.edu.co',
        to_emails='nicucg@gmail.com',
        subject='jaja',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
        return "enviado"
    except Exception as e:
        print(e.message)
        return "matanga"


'''

'''
@app.route("/correo")
def enviarCorreo():
    destino = request.args.get("destino")
    asunto = request.args.get("asunto")
    mensaje = request.args.get("mensaje")
    hashString = request.args.get("hash")
    if  hashString == os.environ.get("SECURITY_HASH"):
        message = Mail(
            from_email=os.environ.get("email_from"),
            to_emails=destino,
            subject=asunto,
            html_content=mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("enviado")
            return "OK"
        except Exception as e:
            print(e.message)
            return "KO"
    else:
        print("Hash error")
        return "KO"

'''



'''

message = Mail(
            from_email=os.environ.get("email_from"),
            to_emails=destino,
            subject=asunto,
            html_content=mensaje)
        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)
            print("enviado")
            return "el mensaje fue enviado correctamente"
        except Exception as e:
            print(e.message)
            return "KO"
        print('la key es valida, complete los demas campos')
        return 'el hash es valido, complete los demas campos'
    else:
        print('hash invalido')
        return 'hash invalido, ingrese uno valido por favor'

'''