import os
import time
import sys
import subprocess
import requests
import random
import threading
from datetime import datetime
from stem import Signal
from stem.control import Controller
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

class Colors:
    CYAN = '\033[38;2;0;255;255m'      # Cyan
    WHITE = '\033[1;97m'               # White
    RED = '\033[38;2;255;50;50m'       # Bright Red
    GOLD = '\033[38;2;255;215;0m'      # Gold
    GREEN = '\033[38;2;0;255;127m'     # Spring Green
    INFO = '\033[38;2;175;238;238m'    # Light Blue
    RESET = '\033[0m'

def banner():
    """iP-CHANG-404 Professional Banner with 3 Colors"""
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # ব্যানারটি তিনটি রঙে ভাগ করা হয়েছে (Cyan, White, Red)
    art = f"""
{Colors.CYAN}    ██╗██████╗         ██████╗██╗  ██╗ █████╗ ███╗   ██╗ ██████╗ 
{Colors.CYAN}    ██║██╔══██╗      ██╔════╝██║  ██║██╔══██╗████╗  ██║██╔════╝ 
{Colors.WHITE}    ██║██████╔╝█████╗██║     ███████║███████║██╔██╗ ██║██║  ███╗
{Colors.WHITE}    ██║██╔═══╝ ╚════╝██║     ██╔══██║██╔══██║██║╚██╗██║██║   ██║
{Colors.RED}    ██║██║           ╚██████╗██║  ██║██║  ██║██║ ╚████║╚██████╔╝
{Colors.RED}    ╚═╝╚═╝            ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ 
{Colors.GOLD}      [ iP-CHANG-404 - ULTIMATE TOR IP ROTATOR V3.0 ]
{Colors.INFO}    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{Colors.GREEN}    📢 Telegram: https://t.me/FS_Zero404
    """
    print(art)
    print(f"{Colors.CYAN}╠══════════════════════════════════════════════════════════════════╣{Colors.RESET}")

class TorController:
    def __init__(self):
        self.rotation_count = 0
        self.is_running = True
        self.start_time = datetime.now()
        self.wait_time = 30 
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    def setup_tor_service(self, country=None):
        os.system("pkill -9 tor > /dev/null 2>&1")
        torrc_content = "SocksPort 9050\nControlPort 9051\nCookieAuthentication 0\n"
        if country:
            torrc_content += f"ExitNodes {{{country}}} StrictNodes 1\n"
        
        with open('torrc_custom', 'w') as f:
            f.write(torrc_content)
        
        subprocess.Popen(['tor', '-f', 'torrc_custom'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{Colors.INFO}◉ {Colors.WHITE}Initializing Tor Service...")
        time.sleep(5)

    def get_current_ip(self):
        proxies = {'http': 'socks5h://127.0.0.1:9050', 'https': 'socks5h://127.0.0.1:9050'}
        headers = {'User-Agent': random.choice(self.user_agents)}
        try:
            response = requests.get('https://api.ipify.org?format=json', proxies=proxies, headers=headers, timeout=10)
            return response.json()['ip']
        except:
            return None

    def rotation_thread(self):
        while self.is_running:
            try:
                print(f"\n{Colors.GOLD}↻ {Colors.WHITE}Requesting New Identity...")
                with Controller.from_port(port=9051) as controller:
                    controller.authenticate()
                    controller.signal(Signal.NEWNYM)
                
                self.rotation_count += 1
                new_ip = self.get_current_ip()
                
                if new_ip:
                    print(f"{Colors.GREEN}✓ {Colors.WHITE}IP Rotation {Colors.GREEN}SUCCESSFUL")
                    print(f"{Colors.GREEN}✓ {Colors.WHITE}Current IP: {Colors.GOLD}{new_ip}")
                else:
                    print(f"{Colors.RED}⚠ {Colors.WHITE}IP Changed but unable to verify")

                # Statistics Table
                uptime = str(datetime.now() - self.start_time).split('.')[0]
                print(f"\n{Colors.CYAN}┌──────────────────────────────────────────────────┐")
                print(f"{Colors.CYAN}│{Colors.GOLD}               SESSION STATISTICS                 {Colors.CYAN}│")
                print(f"{Colors.CYAN}├──────────────────────────────────────────────────┤")
                print(f"{Colors.CYAN}│{Colors.WHITE} Rotations: {Colors.GREEN}{self.rotation_count:<37}{Colors.CYAN}│")
                print(f"{Colors.CYAN}│{Colors.WHITE} Uptime:    {Colors.GREEN}{uptime:<37}{Colors.CYAN}│")
                print(f"{Colors.CYAN}└──────────────────────────────────────────────────┘")

                # Countdown Animation
                print(f"\n{Colors.INFO}├{Colors.WHITE} NEXT ROTATION IN {Colors.INFO}───────────────────────────┤")
                for i in range(self.wait_time, 0, -1):
                    if not self.is_running: break
                    percent = (i / self.wait_time)
                    bar_length = 10
                    filled = int(bar_length * (1 - percent))
                    bar = '●' * filled + '○' * (bar_length - filled)
                    
                    sys.stdout.write(f"\r{Colors.GOLD} ! {Colors.WHITE}{i:02d} seconds remaining {Colors.RED}{bar}{Colors.RESET}")
                    sys.stdout.flush()
                    time.sleep(1)
                print(f"\n{Colors.INFO}────────────────────────────────────────────────────")

            except Exception as e:
                print(f"\n{Colors.RED}✗ Rotation Failed: {e}")
                time.sleep(5)

    def run(self):
        banner()
        try:
            val = input(f"{Colors.INFO}[?] Enter Rotation Time (Seconds): {Colors.WHITE}")
            self.wait_time = int(val) if val.strip() else 30
            country = input(f"{Colors.INFO}[?] Enter Country Code (e.g. us, gb) [Enter for Any]: {Colors.WHITE}").strip().lower()
        except:
            self.wait_time = 30
            country = None

        self.setup_tor_service(country if country else None)
        
        threading.Thread(target=self.rotation_thread, daemon=True).start()

        try:
            while True: time.sleep(1)
        except KeyboardInterrupt:
            self.is_running = False
            os.system("pkill -9 tor > /dev/null 2>&1")
            print(f"\n\n{Colors.RED}⚠ STOPPING iP-CHANG-404 SERVICE...{Colors.RESET}")
            sys.exit()

if __name__ == "__main__":
    app = TorController()
    app.run()
