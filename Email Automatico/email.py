# PRIMEIRO JEITO DE SE ENVIAR UM EMAIL
import os
import win32com.client  # instalar a biblioteca pywin32


def send_mail():
    Msg = win32com.client.Dispatch("Outlook.Application").CreateItem(0)
    Msg.To = 'rafael_hmartins@outlook.com'
    Msg.Subject = "Exemplo 1"
    Msg.HtmlBody = texto
    Msg.Attachments.Add(os.path.dirname(__file__) + '/imagem.png')
    #MSG.display()  # apenas abre o email para ser enviado manualmente pela pessoa


# Msg.Send() trocar para esta função quand for enviar automaticamente

testo = ''' mensagem/script HTML e CSS'''
send_mail()
