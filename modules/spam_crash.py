#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# spam_crash.py - Modul Spam & Crash
# Owner: VoltXRinn

import time
import random
from colorama import Fore, init

init(autoreset=True)

class SpamCrash:
    def __init__(self):
        self.messages = [
            "⚠️ PERINGATAN: AKUN DALAM BAHAYA",
            "SISTEM MENDETEKSI AKTIVITAS MENcurigakan",
            "BAN AKAN DILAKUKAN",
            "LAPORKAN KE SUPPORT",
            "AKUN TELAH DIHACK"
        ]
    
    def execute(self, target, mode):
        print(f"{Fore.RED}[💣] SPAM & CRASH: {target}")
        
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
        """Spam chat"""
        print(f"{Fore.RED}[!] Spam Chat (100 pesan)")
        
        sent = 0
        for i in range(100):
            try:
                msg = random.choice(self.messages)
                print(f"{Fore.YELLOW}[!] Mengirim: {msg}")
                sent += 1
                
                if (i + 1) % 20 == 0:
                    print(f"{Fore.CYAN}[↻] {i+1}/100")
                
                time.sleep(0.1)
                
            except:
                continue
        
        print(f"{Fore.GREEN}[✅] {sent}/100 pesan terkirim")
    
    def crash_session(self, target):
        """Crash session"""
        print(f"{Fore.RED}[💀] Crash Session...")
        
        methods = 3
        for i in range(methods):
            print(f"{Fore.YELLOW}[{i+1}/{methods}] Eksekusi method...")
            time.sleep(1)
        
        print(f"{Fore.GREEN}[✅] Crash sequence selesai")
    
    def flood_notification(self, target):
        """Flood notification"""
        print(f"{Fore.CYAN}[!] Flood Notification...")
        
        for i in range(30):
            try:
                print(f"{Fore.YELLOW}[!] Notification #{i+1}")
                
                if (i + 1) % 10 == 0:
                    print(f"{Fore.CYAN}[↻] Progress: {i+1}/30")
                    
                time.sleep(0.1)
                
            except:
                pass
        
        print(f"{Fore.GREEN}[✅] Flood complete")

# Export function
def execute(target, mode):
    sc = SpamCrash()
    sc.execute(target, mode)
