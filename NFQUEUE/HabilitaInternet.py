
from scapy.all import *
from netfilterqueue import NetfilterQueue

def main():
    q = NetfilterQueue()
    q.bind(0, socket.AF_INET)
    q.set_callback(process)
    q.create_queue(0)
 
    try:
       q.try_run()
    except KeyboardInterrupt:
       print "Exiting..."
    q.unbind(socket.AF_INET)
    q.close()
    sys.exit(1)
 
main()
