# import socket library and termcolor library
import socket
import termcolor

def scan(target,ports):
    print('\n'+' Starting scan for '+str(target))
    for port in range(1,ports):
        scan_port(target,port)

# define function
def scan_port(ipaddress,port):
   try:
      #initate socket object
      sock=socket.socket()
      # connect to our target and our port
      sock.connect((ipaddress,port))
      print("[+] port opened"+str(port))
      socket.close()

   except:
        pass


targets = input("[*] Enter targets to scan(split them by common):")
ports = int(input("[*] enter how many ports you want to scan:"))
if ',' in targets:
    print(termcolor.colored(("[*] scanning multiple targets"),'green'))
    for ip_addr in targets.split(','):
        scan(ip_addr.strip(' '),ports)
else:
    scan(targets,ports)        


