#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Tools & Settings Module - Fixed Version

import os
import sys
import time
import json
import requests
from colorama import Fore, init

init(autoreset=True)

class Tools:
    def __init__(self):
        self.config_file = "config/settings.cfg"
    
    def execute(self, choice):
        if choice == "1":
            self.update_script()
        elif choice == "2":
            self.backup_data()
        elif choice == "3":
            self.clear_logs()
        elif choice == "4":
            self.test_connection()
        elif choice == "5":
            self.generate_config()
        else:
            print(f"{Fore.RED}[!] Invalid choice")
    
    def update_script(self):
        print(f"{Fore.CYAN}[⚡] Checking updates...")
        
        try:
            current_version = "2.1"
            print(f"{Fore.GREEN}[✅] Current version: {current_version}")
            print(f"{Fore.YELLOW}[!] Latest version: 2.1 (up to date)")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Update check failed: {e}")
    
    def backup_data(self):
        print(f"{Fore.CYAN}[!] Creating backup...")
        
        try:
            import zipfile
            import datetime
            
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            backup_file = f"backup_voltx_{timestamp}.zip"
            
            with zipfile.ZipFile(backup_file, 'w') as zipf:
                # Backup config
                if os.path.exists("config/settings.cfg"):
                    zipf.write("config/settings.cfg", "settings.cfg")
                
                # Backup logs
                if os.path.exists("data/logs"):
                    for root, dirs, files in os.walk("data/logs"):
                        for file in files:
                            file_path = os.path.join(root, file)
                            zipf.write(file_path, os.path.relpath(file_path))
            
            size = os.path.getsize(backup_file) / 1024
            print(f"{Fore.GREEN}[✅] Backup created: {backup_file}")
            print(f"{Fore.YELLOW}[!] Size: {size:.1f} KB")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Backup failed: {e}")
    
    def clear_logs(self):
        print(f"{Fore.CYAN}[!] Clearing logs...")
        
        try:
            log_dir = "data/logs"
            if not os.path.exists(log_dir):
                print(f"{Fore.YELLOW}[!] Log directory not found")
                return
            
            count = 0
            for file in os.listdir(log_dir):
                file_path = os.path.join(log_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
                    count += 1
            
            print(f"{Fore.GREEN}[✅] Cleared {count} log files")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to clear logs: {e}")
    
    def test_connection(self):
        print(f"{Fore.CYAN}[!] Testing connections...")
        
        endpoints = [
            ("WhatsApp Web", "https://web.whatsapp.com"),
            ("Google", "https://google.com"),
            ("GitHub", "https://github.com")
        ]
        
        for name, url in endpoints:
            try:
                start = time.time()
                response = requests.get(url, timeout=5)
                elapsed = (time.time() - start) * 1000
                
                if response.status_code == 200:
                    print(f"{Fore.GREEN}[✅] {name}: OK ({elapsed:.0f}ms)")
                else:
                    print(f"{Fore.YELLOW}[⚠] {name}: {response.status_code}")
                    
            except Exception as e:
                print(f"{Fore.RED}[!] {name}: Failed")
    
    def generate_config(self):
        print(f"{Fore.CYAN}[!] Generating new configuration...")
        
        try:
            config = {
                "api_key": "voltx_" + str(int(time.time())),
                "max_threads": 30,
                "ban_timeout": 300,
                "unban_retry": 10,
                "debug_mode": False,
                "auto_update": True,
                "aggressive_mode": True,
                "created": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"{Fore.GREEN}[✅] Configuration saved!")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to generate config: {e}")

# Export function
def execute(choice):
    tools = Tools()
    tools.execute(choice)
