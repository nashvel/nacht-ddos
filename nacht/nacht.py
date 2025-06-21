import os
import sys
import time
import subprocess
from module.l7 import *
from module.l4 import *
from module.l3 import *

nacht = "\033[38;5;118m"
white = "\033[97m"
red = "\033[38;5;196m"
green = "\033[38;5;34m"
clear = "\033[0m"

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nacht}
███╗   ██╗ █████╗  ██████╗██╗  ██╗████████╗
████╗  ██║██╔══██╗██╔════╝██║  ██║╚══██╔══╝
██╔██╗ ██║███████║██║     ███████║   ██║   
██║╚██╗██║██╔══██║██║     ██╔══██║   ██║   
██║ ╚████║██║  ██║╚██████╗██║  ██║   ██║   
╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝       
{clear}""")
    
    print(f"[{nacht}NACHT{clear}] {white}Welcome NACHT DDoS Attack Tools{clear}")
    print(f"[{nacht}NACHT{clear}] {white}Join DoxGroup !! https://rvlt.gg/PnjMbQwH{clear}")
    os.system("pip install aiohttp --break-system-packages")
    input(f"[{nacht}NACHT{clear}] {white}Enter the continue...{clear}")
    
def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{nacht}
███╗   ██╗ █████╗  ██████╗██╗  ██╗████████╗
████╗  ██║██╔══██╗██╔════╝██║  ██║╚══██╔══╝
██╔██╗ ██║███████║██║     ███████║   ██║   
██║╚██╗██║██╔══██║██║     ██╔══██║   ██║   
██║ ╚████║██║  ██║╚██████╗██║  ██║   ██║   
╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝{clear}
          
╔═════════════════════════════════════════════════════╗
║ {nacht}*{clear} Github    {nacht}:{clear}   https://github.com/madanokr001      ║
║ {nacht}*{clear} DoxServer {nacht}:{clear}   https://rvlt.gg/PnjMbQwH            ║
║ {nacht}*{clear} version   {nacht}:{clear}   4.0                                 ║
║ {nacht}*{clear} Created   {nacht}:{clear}   CyberMAD                            ║
╚═════════════════════════════════════════════════════╝

╔═════════════════════════════════════════════════════╗
║ {nacht}[{clear}1{nacht}]{clear} Update NACHT                                     ║
║ {nacht}[{clear}2{nacht}]{clear} Layer3 Attack Methods                           ║     
║ {nacht}[{clear}3{nacht}]{clear} Layer4 Attack Methods                           ║               
║ {nacht}[{clear}4{nacht}]{clear} Layer7 Attack Methods                           ║
║ {nacht}[{clear}5{nacht}]{clear} nmap                                            ║                                    
║ {nacht}[{clear}6{nacht}]{clear} Exit NACHT                                       ║          
╚═════════════════════════════════════════════════════╝                              
""")


def main():
    while True:
        logo()
        select = input(f"""
╔═══[{nacht}root{clear}@{nacht}NACHT{clear}]
╚══{nacht}>{clear} """)
                                        
        if select == "1" or select.lower() == "u":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{nacht}
██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗
██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝
██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  
██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  
╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗
 ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                  {clear}""")
            subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
            print(f"[{nacht}NACHT{clear}] Update Success!")
            input(f"[{nacht}NACHT{clear}] Enter the continue...")

        elif select == "6" or select.lower() == "e":
            sys.exit()

        elif select == "5" or select.lower() == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"""{nacht}
███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
████╗  ██║████╗ ████║██╔══██╗██╔══██╗
██╔██╗ ██║██╔████╔██║███████║██████╔╝
██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝     
                {clear}""")
            
            target = input(f"[{nacht}NACHT{clear}] IP       {nacht}>{clear} ")
            
            os.system(f"nmap {target}")
            input(f"[{nacht}NACHT{clear}] Enter the continue...")

        elif select == "2" or select.lower() == "2":
            layer3()

        elif select == "3" or select.lower() == "3":
            layer4()

        elif select == "4" or select.lower() == "4":
            layer7()
            
    
             


if __name__ == "__main__":
    check_main()
    main()
