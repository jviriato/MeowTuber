from scapy.all import *
from netfilterqueue import NetfilterQueue

def print_and_accept(pkt):
    data = pkt.get_payload()
    p = IP(data)
    #print p
    pkt.accept()

nfqueue = NetfilterQueue()
nfqueue.bind(0, print_and_accept)
try:
    nfqueue.run()
except KeyboardInterrupt:
    print
