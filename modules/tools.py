#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Tools & Settings Module

import os
import sys
import time
import json
import requests
import subprocess
from colorama import Fore, init

init(autoreset=True)

class Tools:
    def __init__(self):
        self.config_file = "config/settings.cfg"
        self.github_repo = "https://github.com/QirinnFall/VoltxControlCenter"
    
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
    
    def update_script(self):
        print(f"{Fore.CYAN}[⚡] Checking for updates...")
        
        try:
            # Get latest version from GitHub
            response = requests.get(
                f"{self.github_repo}/raw/main/version.txt",
                timeout=10
            )
            
            if response.status_code == 200:
                latest_version = response.text.strip()
                current_version = "2.0.0"
                
                if latest_version != current_version:
                    print(f"{Fore.YELLOW}[!] Update available: {latest_version}")
                    print(f"{Fore.CYAN}[!] Current version: {current_version}")
                    
                    update = input(f"{Fore.GREEN}[?] Update now? (y/n): ").lower()
                    if update == 'y':
                        self.perform_update()
                else:
                    print(f"{Fore.GREEN}[✅] You have the latest version!")
            else:
                print(f"{Fore.YELLOW}[⚠] Cannot check updates")
                
        except:
            print(f"{Fore.RED}[!] Update check failed")
    
    def perform_update(self):
        print(f"{Fore.CYAN}[!] Updating VoltxControlCenter...")
        
        try:
            # Backup current config
            if os.path.exists(self.config_file):
                subprocess.run(["cp", self.config_file, "config/settings.backup"], check=True)
            
            # Pull latest changes
            subprocess.run(["git", "pull", "origin", "main"], check=True)
            
            # Update requirements
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--upgrade"], check=True)
            
            print(f"{Fore.GREEN}[✅] Update successful!")
            print(f"{Fore.YELLOW}[!] Please restart the application")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Update failed: {e}")
    
    def backup_data(self):
        print(f"{Fore.CYAN}[!] Creating backup...")
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        backup_file = f"backup_voltx_{timestamp}.tar.gz"
        
        try:
            # Create backup archive
            subprocess.run([
                "tar", "-czf", backup_file,
                "config/", "data/logs/", "modules/"
            ], check=True)
            
            print(f"{Fore.GREEN}[✅] Backup created: {backup_file}")
            print(f"{Fore.YELLOW}[!] Size: {os.path.getsize(backup_file) // 1024} KB")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Backup failed: {e}")
    
    def clear_logs(self):
        print(f"{Fore.CYAN}[!] Clearing logs...")
        
        try:
            log_dir = "data/logs"
            for file in os.listdir(log_dir):
                file_path = os.path.join(log_dir, file)
                if os.path.isfile(file_path):
                    os.remove(file_path)
            
            print(f"{Fore.GREEN}[✅] Logs cleared!")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed to clear logs: {e}")
    
    def test_connection(self):
        print(f"{Fore.CYAN}[!] Testing WhatsApp API connections...")
        
        endpoints = [
            ("Main API", "https://web.whatsapp.com"),
            ("Report API", "https://www.whatsapp.com/api/report"),
            ("GraphQL", "https://graph.whatsapp.com/graphql")
        ]
        
        for name, url in endpoints:
            try:
                start = time.time()
                response = requests.get(url, timeout=10)
                elapsed = (time.time() - start) * 1000
                
                if response.status_code < 500:
                    print(f"{Fore.GREEN}[✅] {name}: {response.status_code} ({elapsed:.0f}ms)")
                else:
                    print(f"{Fore.YELLOW}[⚠] {name}: {response.status_code}")
                    
            except Exception as e:
                print(f"{Fore.RED}[!] {name}: Failed - {str(e)[:30]}")
    
    def generate_config(self):
        print(f"{Fore.CYAN}[!] Generating new configuration...")
        
        config = {
            "api_key": "voltx_" + str(int(time.time())),
            "max_threads": int(input("Max threads [10-100]: ") or "50"),
            "ban_timeout": int(input("Ban timeout (seconds): ") or "300"),
            "unban_retry": int(input("Unban retry count: ") or "10"),
            "debug_mode": input("Debug mode (true/false): ").lower() == "true",
            "auto_update": True,
            "backup_on_start": False,
            "aggressive_mode": True
        }
        
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"{Fore.GREEN}[✅] New configuration saved!")
        print(f"{Fore.YELLOW}[!] Restart application for changes to take effect")

# Export function
def execute(choice):
    tools = Tools()
    tools.execute(choice)
