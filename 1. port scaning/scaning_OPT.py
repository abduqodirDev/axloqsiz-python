from socket import *
import optparse
from threading import *
from termcolor import colored

def scan(tgthost, tgtport):
    try:
        soc = socket(AF_INET, SOCK_STREAM)
        soc.connect((tgthost, tgtport))
        print(colored(f"[*] {tgtport} /tcp porti ochiq", "red"))
    except:
        print(colored(f"[*] {tgtport} /tcp porti yopiq", "green"))
    finally:
        soc.close()

def portscaner(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(f"[*] {tgtHost} ning ip manzili topilmadi")
    try:
        tgtname = gethostbyaddr(tgtIP)
        print(f"[*] {tgtname} uchun scaner natijalar:")
    except:
        print(f"[*] {tgtIP} uchun scaner natijalar:")
    setdefaulttimeout(1)
    if tgtPorts[0]=="None":
        tgtPorts=list(range(1, 100))
    for tgtport in tgtPorts:
        t = Thread(target=scan, args=(tgtHost, int(tgtport)))
        t.start()

def main():
	parser = optparse.OptionParser("Programma foydalanish texnikasi: -t <Nishon ip manzili>, -p <Portlar ro'yxati>")
	parser.add_option('-t', dest="tgtHost", type="string", help="Ip manzilni aniqlashtirish")
	parser.add_option('-p', dest="tgtPort", type="string", help="Port manzilini kiriting")
	(options, args) = parser.parse_args()
	tgtHost = options.tgtHost
	tgtPorts = str(options.tgtPort).split(',')
	print(tgtHost)
	print(tgtPorts)
	if tgtHost == None:
		print(parser.usage)
		exit()
	else:
	    portscaner(tgtHost, tgtPorts)

main()
