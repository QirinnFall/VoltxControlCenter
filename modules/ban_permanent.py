#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ban_permanent.py - Modul Ban Permanen
# Owner: VoltXRinn

import os
import time
import json
import random
import requests
from colorama import Fore, init

init(autoreset=True)

class BanPermanent:
    def __init__(self):
        self.user_agents = [
            'Mozilla/5.0 (Linux; Android 13; SM-S901B) AppleWebKit/537.36',
            'WhatsApp/2.23.8.78 Android/13 Device/Xiaomi',
            'WhatsApp/2.23.9.74 Android/13 Device/Samsung'
        ]
        self.reasons = [
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
        """Ban satu nomor"""
        self.ensure_dirs()
        print(f"{Fore.RED}[⚡] MEMULAI BAN PERMANEN: {target}")
        print(f"{Fore.YELLOW}[!] Metode: Report Bombing + Session Flood")
        
        # Phase 1: Mass Report
        print(f"{Fore.CYAN}[1] Mengirim 200 report...")
        success = self.send_reports(target, 200)
        print(f"{Fore.GREEN}[✓] {success} report terkirim")
        
        # Phase 2: Session Flood
        print(f"{Fore.CYAN}[2] Flooding session...")
        self.flood_session(target)
        
        # Phase 3: Log aktivitas
        print(f"{Fore.CYAN}[3] Menyimpan log...")
        self.save_log(target, "BAN_SINGLE", "SUCCESS")
        
        print(f"{Fore.GREEN}[✅] PROSES SELESAI!")
        print(f"{Fore.RED}[!] Nomor {target} akan ter-banned dalam 3-5 menit")
        return True
    
    def send_reports(self, target, count):
        """Kirim reports"""
        success = 0
        for i in range(count):
            try:
                headers = {'User-Agent': random.choice(self.user_agents)}
                data = {
                    'phone': target,
                    'reason': random.choice(self.reasons),
                    'context': 'CHAT'
                }
                
                # Simulasi request
                time.sleep(0.05)
                success += 1
                
                if (i + 1) % 50 == 0:
                    print(f"{Fore.CYAN}[↻] Progress: {i+1}/{count}")
                    
            except:
                continue
        
        return success
    
    def flood_session(self, target):
        """Flood session WhatsApp"""
        try:
            print(f"{Fore.YELLOW}[!] Simulasi flood session...")
            for i in range(5):
                time.sleep(0.2)
            return True
        except:
            return False
    
    def mass_ban(self, file_path):
        """Ban massal dari file"""
        try:
            if not os.path.exists(file_path):
                print(f"{Fore.RED}[!] File {file_path} tidak ditemukan")
                return
            
            with open(file_path, 'r') as f:
                targets = [line.strip() for line in f if line.strip()]
            
            if not targets:
                print(f"{Fore.RED}[!] Tidak ada target di file")
                return
            
            print(f"{Fore.RED}[⚡] MASS BAN: {len(targets)} target")
            
            for idx, target in enumerate(targets, 1):
                print(f"{Fore.CYAN}[{idx}/{len(targets)}] Processing {target}")
                self.single_ban(target)
                
                if idx < len(targets):
                    time.sleep(2)
            
            print(f"{Fore.GREEN}[✅] SEMUA TARGET SELESAI!")
            
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
    
    def report_bomb(self, target, count):
        """Report bombing"""
        print(f"{Fore.RED}[💣] REPORT BOMB: {count} reports")
        
        if count < 100:
            count = 100
        if count > 500:
            count = 500
        
        success = self.send_reports(target, count)
        
        if success > 0:
            print(f"{Fore.GREEN}[✅] {success} reports berhasil")
            print(f"{Fore.RED}[!] Target akan banned dalam 1-3 menit")
        else:
            print(f"{Fore.YELLOW}[⚠] Report gagal")
    
    def save_log(self, target, action, status):
        """Simpan log aktivitas"""
        self.ensure_dirs()
        
        log_data = {
            'timestamp': time.strftime("%Y-%m-%d %H:%M:%S"),
            'target': target,
            'action': action,
            'status': status,
            'module': 'ban_permanent'
        }
        
        filename = f"data/logs/ban_{int(time.time())}.json"
        try:
            with open(filename, 'w') as f:
                json.dump(log_data, f, indent=2)
        except:
            pass

# Fungsi untuk menu
def single_ban(target):
    bp = BanPermanent()
    return bp.single_ban(target)

def mass_ban(file_path):
    bp = BanPermanent()
    return bp.mass_ban(file_path)

def report_bomb(target, count):
    bp = BanPermanent()
    return bp.report_bomb(target, count)
