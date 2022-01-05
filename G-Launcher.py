from email import message
import os
import sys
from types import ClassMethodDescriptorType, prepare_class
import psutil
import socket
import subprocess
import requests
import smtplib
import webbrowser
import ssl
import time
import urllib.request
from bs4 import BeautifulSoup as bs
import speedtest
import platform as plat
from sys import platform


def command():
    name= os.getlogin()
    com = input("seal@"+name+":~# ")

    if com == 'dir' or com == 'ls':
        listdir()
    elif com == 'cpu-per':
        temp()
    elif com == 'localhost':
        localip()
    elif com == 'ntwname':
        ntwname()
    elif com == 'speed':
        speedtest2()
    elif com == 'system':
        system()
    elif com == 'ipcheck':
        ipcheck()
    elif com == 'myip':
        myip()
    elif com == 'logo':
        logo()
    elif com == 'exit':
        exit2()
    elif com == 'download':
        download()
    elif com == 'mail':
        mail()
    elif com == 'license':
        license()
    elif com == 'sysinfo':
        sysinfo()
    elif com == 'help':
        help()
    else :
        print("|!| Command Not Found |!|")
        print("|!| print help to help menu |!|  ")

def name():
    name = os.getlogin()
    print(name)

def listdir():
    file = sys.path
    lister = os.listdir(file[0])
    lenlist = len(lister)
    count = -1
    for n in range(0,lenlist):
        count += 1
        if count >= lenlist:
            break
        print("|"+str(count)+"| "+lister[count])

def temp():
    #GPUtil.showUtilization()
    ss = str(psutil.cpu_percent(1))
    print("|i| Percent Usage %"+ss+" |i|")

def localip():
    liste = socket.gethostbyname_ex(socket.gethostname())
    liste = liste[2]
    stra = '\n'.join(map(str, liste))
    print(stra)

def ntwname():
    wifi = (subprocess.check_output("netsh wlan show interfaces"))
    wifi = wifi.decode("UTF-8")
    print(wifi)

def speedtest2():
    st = speedtest.Speedtest()
    dow = st.download()
    up = st.upload() 
    print("|/| Download Speed "+str(dow/1000000)+" MBps |\|")
    print("|/| Upload Speed "+str(up/1000000)+" MBps |\|")

def system():
    sta = sys.platform
    if sta == "win32":
        sta = "Windows"
    elif sta == "linux" or "linux2":
        sta = "Linux"
    elif sta == "darwin":
        sta = "MacOS"
    print("|0x| System "+sta+" |0x|")

def ipcheck():
    host = input("|^| Set HostName |^| ")
    hostn = socket.gethostbyname(host)
    print("|IP| HostName | " +host+ " | IPv4 " +hostn+" |IP|")

def myip():
    ip2 = requests.get("https://ip-adresim.net/")
    source = bs(ip2.content,"lxml")
    head2 = source.find("strong",attrs={"class","mycurrentip"})
    rem2 = head2.text
    ips = rem2.split()
    print("|&| Remote IP | "+ips[0]+" |&|")

def logo():
    print(""" 
    
    
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░████████░░██░░░░░████░░░░░██░░░██░░░░░
░░░░░░░░░░██░░██░░░░██░░██░░░░██░░██░░░░░░
░░░░░░░░░██░░░██░░░██░░░░██░░░██░██░░░░░░░
░░░░░░░░██░░░░██░░██░░░░░░██░░████░░░░░░░░
░░░░░░░██░░░░░██░░██████████░░██░░██░░░░░░
░░░░░░██░░░░░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░░██░░░░░░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░████████░░██░░██░░░░░░██░░██░░░██░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░0x47░░░0x4F░░░0x4B░░░0x43░░░0x45░░░░░
    
    """)

def exit2():
    name = os.getlogin()
    print("|:| Bye "+name+" |:|")
    exit()

def download():
    urldow = input("|+| Download URL |+| ")
    docname = input("|+| Download File Name |+| ")
    urllib.request.urlretrieve(urldow,docname)
    print("|!| Success , Downloaded "+docname+" |!|")

def license():
    print("|-| Loading GitHub Link |-|")
    print("|-| Link : https://www.github.com/arda6/SEAL |-|")
    time.sleep(2)
    webbrowser.get("https://www.github.com/arda6/SEAL")

def mail():
    port = '587'
    server = input("|=| STMP Server |=| ")
    send = input("|=| Sender Mail Adress |=| ")
    rec = input("|=| Reciver EMAIL Adress |=| ")
    passw = input("|=| EMAIL Password |=| ")
    mesaj = input("|=| Send Message |=| ")
    context = ssl.create_default_context()
    with smtplib.SMTP(server, port) as server:
        server.ehlo()  
        server.starttls(context=context)
        server.ehlo()  
        server.login(send, passw)
        server.sendmail(send, rec, message)

def sysinfo():
    print("|?| Machine : "+str(plat.machine())+ " |?|\n|?| Version : "+str(plat.version())+" |?|\n|?| Platform : "+str(plat.platform())+" |?|\n|?| Architecture : "+str(plat.architecture())+" |?|\n|?| Processor : "+str(plat.processor())+" |?|")

def help():
    print("""
    1) system   | System Info
    2) speed    | Internet Speed Test
    3) myip     | Your Remote IP Adress
    4) ipcheck  | Domain to IP
    5) ntwname  | Connected Network Info
    6) locahost | Local IP Adress
    7) cpu-per  | CPU Info
    8) help     | Open Help Menu
    9) logo     | View Logo
   10) download | File Download
   11) mail     | Send Email
   12) license  | Get GitHub Link
   13) sysinfo  | Get Detailed System Info
   14) exit     | Exit the SEAL  
    
     """)


#listdir()
#name()

while True:
    command()

#print(os.listdir(file[0]))

#lenlist = len(lister)

#x = range(0,lenlist)
#count = 0
#for n in x:
#    count += 1
#    if count >= lenlist:
#        break
#    try:
#        print(count)
#        print(lenlist)
#        print(os.listdir(file[0]))
#    except Exception:
#        continue
