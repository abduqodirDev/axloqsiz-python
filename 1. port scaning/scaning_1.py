import socket
from termcolor import colored

internet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(3)

host = input("target ip manzilini kiriting: ")
#port = int(input("portni kiriting: "))

def scaning(port):
	if internet.connect_ex((host, port)):
		print(colored(f"{port} porti yopiq", "red"))
	else:
		print(colored(f"___]]]]]{port} porti ochiq[[[[[____", "green"))

for port in range(1, 100):
    scaning(port)

