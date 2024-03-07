"""
Run:
"""
from tokenbag.settings import *
from mailjet_rest import Client

mailjet = Client(auth=(API_KEY, SECRET_KEY), version='v3.1')

def enviar_email(destinatario,codigo,nome):

        data = {
        'Messages': [
                        {
                        "From": {
                                "Email": HOST_EMAIL,
                                "Name": "Token"
                        },
                        "To": [
                                {
                                        "Email": destinatario,
                                        "Name": "You"
                                }
                        ],
                        "TemplateID":4770501,
                        "TemplateLanguage": True,
                        "Subject": "Código de validação",
                        ##"HTMLPart": f"<h3> {codigo}</h3>",
                        "Variables":{
                                'codigo':codigo
                                        }

                        }
                ]
        }
        
        result = mailjet.send.create(data=data)

        if result.status_code == 200:

                print (result.json())

                return True
        else:
                erro=result.json()

                return erro