import subprocess
import threading
import configparser
from colorama import init
from colorama import Fore, Back, Style
init()
config = configparser.ConfigParser()
config.read('config.ini')

found = False
foundagain = False
mailsent = False
failed = 0

def sniff():
	global found, foundagain, mailsent, failed
	address = config['GENERAL']['IP_OF_DEVICE']
	res = subprocess.call(['ping', '-n', '1', "-w", "200", address])
	if res == 0:
		failed = 0
		print (Fore.GREEN + "ping to", address, "OK")
		print(Fore.RED, foundagain)
		print(Fore.RED, mailsent)
		print(Style.RESET_ALL)
		if foundagain == True and mailsent == False:
			email()
			mailsent = True
			print(Fore.GREEN + "-----MAIL GESENDET-----")
			print(Style.RESET_ALL)

		if foundagain == False and mailsent == False:
			foundagain = True

		if foundagain == False and mailsent == True:
			foundagain = True
			mailsent = False



	elif res == 2:
		print ("no response from", address)
		foundagain = False
	else:
		print (Fore.YELLOW + "ping to", address, "failed!")
		print(Style.RESET_ALL)
		print(Fore.RED, foundagain)
		print(Fore.RED, mailsent)
		print(Style.RESET_ALL)
		failed += 1
		print(failed)
		if failed >= 3:
			failed = 0
			foundagain = False
			mailsent = False
	threading.Timer(2, sniff).start()

def email():
    import smtplib
    from socket import gaierror
    from email.mime.text import MIMEText as text
    from datetime import datetime

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")


    # Now you can play with your code. Let’s define the SMTP server separately here:
    port = 587
    smtp_server = config['SMTP']['SERVER']
    sender = config['SMTP']['EMAIL']
    password = config['SMTP']['PASSWORD']
    # Specify the sender’s and receiver’s email addresses:
    receiver = config['SMTP']['RECEIVER']

    # type your message: use two newlines (\n) to separate the subject from the message body, and use 'f' to  automatically insert variables in the text
    message="Miris Handy hat sich um "+ current_time+ " mit dem WLAN verbunden"
    m = text(message)

    m['Subject'] = config['SMTP']['SUBJECT']
    m['From'] = sender
    m['To'] = receiver


    try:
      # Send your message with credentials specified above
        server = smtplib.SMTP(smtp_server, port)
        server.connect(smtp_server,port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, m.as_string())
        server.quit()
    except (gaierror, ConnectionRefusedError):
      # tell the script to report if your message was sent or which errors need to be fixed
      print('Failed to connect to the server. Bad connection settings?')
    except smtplib.SMTPServerDisconnected:
      print('Failed to connect to the server. Wrong user/password?')
    except smtplib.SMTPException as e:
      print('SMTP error occurred: ' + str(e))
    else:
      print('Sent')

sniff()
