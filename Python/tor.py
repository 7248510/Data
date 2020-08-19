#Testing tor, the script is designed to work on Linux
import socks
import socket
from urllib.request import urlopen
socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
socket.socket = socks.socksocket
print(urlopen("http://icanhazip.com").read())
