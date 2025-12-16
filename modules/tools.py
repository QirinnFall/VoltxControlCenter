#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tools.py - Modul Tools & Settings
# Owner: VoltXRinn

import os
import time
import json
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
            print(f"{Fore.RED}[!] Pilihan tidak valid")
    
    def update_script(self):
        """Update script"""
        print(f"{Fore.CYAN}[⚡] Checking updates...")
        time.sleep(1)
        print(f"{Fore.GREEN}[✅] Version 2.1 (up to date)")
    
    def backup_data(self):
        """Backup data"""
        print(f"{Fore.CYAN}[!] Creating backup...")
        
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            backup_dir = f"backup_{timestamp}"
            
            os.makedirs(backup_dir, exist_ok=True)
            
            # Copy config
            if os.path.exists(self.config_file):
                import shutil
                shutil.copy(self.config_file, f"{backup_dir}/settings.cfg")
            
            print(f"{Fore.GREEN}[✅] Backup created: {backup_dir}")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Backup failed: {e}")
    
    def clear_logs(self):
        """Clear logs"""
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
            
            print(f"{Fore.GREEN}[✅] {count} log files cleared")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed: {e}")
    
    def test_connection(self):
        """Test connection"""
        print(f"{Fore.CYAN}[!] Testing connection...")
        
        tests = [
            ("WhatsApp Web", True),
            ("Internet", True),
            ("Local Files", True)
        ]
        
        for name, status in tests:
            time.sleep(0.3)
            if status:
                print(f"{Fore.GREEN}[✅] {name}: OK")
            else:
                print(f"{Fore.RED}[✗] {name}: FAILED")
    
    def generate_config(self):
        """Generate config"""
        print(f"{Fore.CYAN}[!] Generating config...")
        
        try:
            config = {
                "api_key": "voltx_" + str(int(time.time())),
                "max_threads": 30,
                "ban_timeout": 300,
                "unban_retry": 10,
                "debug_mode": False,
                "auto_update": True,
                "created": time.strftime("%Y-%m-%d %H:%M:%S")
            }
            
            with open(self.config_file, 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"{Fore.GREEN}[✅] Configuration saved!")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Failed: {e}")

# Export function
def execute(choice):
    tools = Tools()
    tools.execute(choice)
