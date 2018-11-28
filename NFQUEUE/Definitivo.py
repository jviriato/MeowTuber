import socket
import codecs
import scapy
from scapy.all import *
from netfilterqueue import NetfilterQueue

post = "POST"
filtro = "penis"

def print_pacote(pacote):
    aux = "text="
    dados = Ether(bytes(pacote[0]))
    dados = dados[Raw].load
    index = dados.find(aux)
    print("\n{} ----HTTP---->{}\n".format(pacote[IP].src,pacote[IP].dst))
    if(index != -1):
       print("Conteudo: {}".format(dados[index:]))

def packet_callback(pkt):
    packet = IP(pkt.get_payload())
    #print packet
    try:
        #et = Ether(str(packet[0]))
        et = packet[IP].payload
    except:
        var = 1
    #if((packet[IP].src == "10.0.2.15") and (packet[IP].dst == "10.0.2.17") and packet.haslayer(TCP)):
    if((packet[IP].src == "10.0.2.15") and packet.haslayer(TCP)):
	dados = str(et)
	#print_pacote(packet)
	if(dados.find(post)!= -1):#verifica se eh um post
 	    #print_pacote(packet)
	    index = dados.find(filtro);
	    if(index == -1):
		print("#######pacote limpo############")
  	    else:
	        dados = dados.replace(filtro, "****")
		print("Dados Editados: {}".format((dados)))
		#et[Raw].load = dados
		#print("Dados Editados: {}".format((dados)))
	    	#print "========================"
	    	#print("dados: {}".format(bytes(dados)))
	    	#print "========================"
	    	#print("dados: {}".format(bytes(packet[IP].payload)))
	    	#print "========================"
		#packet[IP].payload = Ether(dados)
		et = TCP(dados)
		
		packet[IP].payload = et
		del packet[TCP].chksum
        	del packet[IP].ihl
        	del packet[IP].len
		del packet[IP].chksum
		packet.show2(dump=True)
		pkt.set_payload(str(packet))
		print("#######pacote alterado############")
		#print_pacote(packet)


    pkt.accept()
   
    
def forwarder(pkt):
    pkt.accept()


nfqueue = NetfilterQueue()
nfqueue.bind(0, packet_callback)
#nfqueue.bind(0, forwarder)
try:
    nfqueue.run()
except KeyboardInterrupt:
    var1 = 22
