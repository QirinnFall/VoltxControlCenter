#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mass Report Module - Fixed Version

import time
import random
import requests
from colorama import Fore, init

init(autoreset=True)

class MassReport:
    def __init__(self):
        self.templates = {
            "violence": ["kekerasan", "pembunuhan", "senjata", "ancaman"],
            "spam": ["penipuan", "scam", "phishing", "iklan illegal"],
            "harassment": ["pelecehan", "bullying", "intimidasi"],
            "child": ["eksploitasi anak", "konten anak", "minor"]
        }
    
    def execute(self, target, mode):
        print(f"{Fore.RED}[📢] MASS REPORT ACTIVATED")
        print(f"{Fore.YELLOW}[!] Target: {target}")
        
        try:
            if mode == "1":
                self.standard_report(target)
            elif mode == "2":
                self.extreme_report(target)
            elif mode == "3":
                self.multi_reason_report(target)
            elif mode == "4":
                self.custom_report(target)
            else:
                print(f"{Fore.RED}[!] Mode tidak valid")
        except Exception as e:
            print(f"{Fore.RED}[!] Error: {e}")
    
    def standard_report(self, target):
        """100 reports standard"""
        print(f"{Fore.CYAN}[!] Standard Report (100 reports)")
        self.send_reports(target, count=100)
    
    def extreme_report(self, target):
        """500 reports extreme"""
        print(f"{Fore.RED}[💀] EXTREME MODE: 500 REPORTS")
        self.send_reports(target, count=500)
    
    def multi_reason_report(self, target):
        """Report dengan berbagai alasan"""
        print(f"{Fore.CYAN}[!] Multi-Reason Report (200 reports)")
        
        reasons = list(self.templates.keys())
        total_sent = 0
        
        for reason in reasons:
            print(f"{Fore.YELLOW}[!] Mengirim report: {reason}")
            sent = self.send_reports(target, count=50, reason_type=reason)
            total_sent += sent
            time.sleep(1)
        
        print(f"{Fore.GREEN}[✅] Total {total_sent} reports terkirim")
    
    def custom_report(self, target):
        """Custom report pattern"""
        print(f"{Fore.CYAN}[!] Custom Pattern Report")
        
        # Predefined pattern
        pattern = [
            ("violence", 40),
            ("spam", 30),
            ("harassment", 20),
            ("child", 10)
        ]
        
        total_sent = 0
        for reason, count in pattern:
            print(f"{Fore.YELLOW}[!] {count} {reason} reports")
            sent = self.send_reports(target, count=count, reason_type=reason)
            total_sent += sent
            time.sleep(0.5)
        
        print(f"{Fore.GREEN}[✅] Total {total_sent} reports terkirim")
    
    def send_reports(self, target, count=100, reason_type=None):
        """Send multiple reports - SIMPLE VERSION"""
        successful = 0
        
        for i in range(count):
            try:
                if self.send_single_report(target, reason_type):
                    successful += 1
                
                # Progress indicator
                if (i + 1) % 20 == 0:
                    print(f"{Fore.CYAN}[↻] {i+1}/{count} reports")
                
                # Delay
                time.sleep(0.2)
                
            except:
                continue
        
        return successful
    
    def send_single_report(self, target, reason_type=None):
        """Send single report"""
        try:
            if not reason_type:
                reason_type = random.choice(list(self.templates.keys()))
            
            # Get keywords based on reason
            keywords = self.templates[reason_type]
            message = f"User melakukan {random.choice(keywords)}"
            
            # WhatsApp report endpoint
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 13) AppleWebKit/537.36',
                'Accept': 'application/json',
            }
            
            data = {
                'phone': target,
                'reason': reason_type.upper(),
                'message': message,
                'context': 'CHAT'
            }
            
            response = requests.post(
                'https://www.whatsapp.com/ajax/report/',
                headers=headers,
                data=data,
                timeout=5
            )
            
            return response.status_code == 200
            
        except:
            return False

# Export function
def execute(target, mode):
    mr = MassReport()
    mr.execute(target, mode)
