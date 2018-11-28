import socket
import codecs
import scapy
from scapy.all import *
from netfilterqueue import NetfilterQueue
import json
from pprint import pprint

post = "POST"

def print_pacote(pacote):
    aux = "text="
    dados = Ether(bytes(pacote[0]))
    dados = dados[Raw].load
    index = dados.find(aux)
    print("\n{} ----HTTP---->{}\n".format(pacote[IP].src,pacote[IP].dst))
    if(index != -1):
       print("Conteudo: {}".format(dados[index:]))


def find_badword(dados):
    with open('badwords.json') as data_file:    
        data = json.load(data_file)
	for x in data["badwords"]:
	    dados = dados.replace(str(x["badword"]), len(str(x["badword"]))*"*")

    return dados


def packet_callback(pkt):
    packet = IP(pkt.get_payload())
    try:
        et = packet[IP].payload
    except:
        var = 1
    if((packet[IP].src == "10.0.2.15") and (packet[IP].dst == "10.0.2.17") and packet.haslayer(TCP)):
	    dados = str(et)
	    if(dados.find(post)!= -1):
	    	et = TCP(find_badword(dados))
		packet[IP].payload = et
		del packet[TCP].chksum
        	del packet[IP].ihl
        	del packet[IP].len
    		del packet[IP].chksum
    		packet.show2(dump=True)
    		pkt.set_payload(str(packet))
    		print("#######pacote alterado############")

    pkt.accept()
   
    
def forwarder(pkt):
    pkt.accept()


nfqueue = NetfilterQueue()
#nfqueue.bind(0, packet_callback)
nfqueue.bind(0, forwarder)
try:
    nfqueue.run()
except KeyboardInterrupt:
    var1 = 22
