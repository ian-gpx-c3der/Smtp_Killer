import smtplib,getpass,email.utils,os
from email.mime.text import MIMEText
os.system("toilet 'The_end' |lolcat")    
print("")
print("")
os.system('echo "________________________________________________________________" |lolcat ')
print("")   
x = int(input("quantia a enviar "))
z = 0
para = input("para ")
msg1 = input("conteudo ")
s_email = input("Seu email ")
s_senha = input("Sua senha ")
if '@' and '.com' in para and s_email:
    while z < x:
        z += 1
        try:
            smtp = smtplib.SMTP("smtp.gmail.com",587)
            smtp.ehlo()
            smtp.starttls()
            smtp.set_debuglevel(False)
            smtp.login(s_email,s_senha)

            msg = MIMEText('')
            msg['From'] = email.utils.formataddr(('Author', 'de@gmail.com'))
            msg['To'] = email.utils.formataddr(('Recipient', 'para@gmail.com'))
            msg['Subject'] = msg1
            smtp.sendmail(s_email, [para], msg.as_string())
        except smtplib.SMTPAuthenticationError as e:
            os.system("echo 'user ou senhas incorretos ou login em aplicativos nao seguros desativado'|lolcat  ")   


else:
    os.system('echo invalido |lolcat ')
    

