
OBS: SE VCS FIZERAM MERDA NO PASSO QUE FICA SEM INTERNET, SÓ REINICIA O PC QUE VOLTA
Então, tem q instalar um monte de merda, scapy, python 3.8(acho que o 3.7 serve tbm), http perf, flask e
NFQUEUE. Cata ai como instalar, a maioria resolve com apt-get, se der alguns erros cata no google o erro que deve ter algum outro apt-get pra instalar o negócio. 

Bom, dps de instalado, vai no terminal e da um "ifconfig" vai mostrar a tua interface, ip e mascara.
no meu caso, a interface era enp0s3, ip 10.0.2.15(pq é vm) e mascara 255.255.255.0.
Abrem o arquivo create_iterface.sh e mudem pro comando ficar no mesmo modelo que o meu:

ifconfig interface:0 ip+1
ifconfig interface:0 netmask mascara

ifconfig interface:1 ip+2
ifconfig interface:1 netmask mascara

Então executem o arquivo: sudo ./create_interface.sh

Feito isso, as iterfaces virtuais estão criadas, então baixem o zip ServerTeste, que é a versão inicial
do server do josé, extraiam, vão no diretório que foi extraido, abrão o terminal la e executem os comandos:

export FLASK_APP=main.py
flask run --host=IP

Onde o IP vai ser o ip da interface:1 que vcs configuraram antes, no meu caso 10.0.2.17
Feito isso o server vai estar rodando, pra testar, abram outro terminal e executem o comando:

curl IP:5000/submit -d "text=testando"

Onde o IP do host do server que foi colocado no comando antes. Se tudo deu certo vcs devem receber
uma resposta como: You entered: testando.
Pra ver se o http perf esta funcionando, baixem o session.txt e abram o terminal onde ele foi baixado, então digite o comando que ta dentro das ######## do arquivo comandos_perf.txt mas mudem o --server=10.0.2.17 pro IP do server de vcs. Ele deve dar 100 acessos ao servidor se foi instalado certo.
Depois disso executem o comando que ta no txt comandos_iptables, mas mudando o ip pro ip da interface normal de vcs, a que não tem o :0 ou :1, o /24 é por causa da mascara, se for igual a minha pode deixar assim.

Depois de executar esse comando, se foi feito certo, vcs vão ficar sem internet, pra ela voltar a funcionar tem q executar o programa do python, o Definitivo2.py, ele deve fazer a internet funcionar dnv, mas caso não funcione, use o HabilitaInternet.py

Baixem o badwords.json do josé pra fazer a filtragem das palavras, e então só precisa mudar uma coisa no código do Definitivo2.py, que é novamente os IPs, na linha:

if((packet[IP].src == "10.0.2.15") and (packet[IP].dst == "10.0.2.17") and packet.haslayer(TCP)):

mude o 10.0.2.15 pro ip da interface normal(sem o :0 ou :1, da pra ver o ip com o comando ifconfig), e o ip 10.0.2.17 pro ip do server, deve funcionar apartir dai.







