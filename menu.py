#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VoltxControlCenter v2.0 - Created for VoltXRinn

import os
import sys
import time
from modules import ban_permanent, mass_report, spam_crash, unban_all, tools

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    print("""
    ╔════════════════════════════════════════╗
    ║    ⚡ VOLTX CONTROL CENTER v2.0 ⚡      ║
    ║    Owner: VoltXRinn                    ║
    ║    Github: QirinnFall                  ║
    ║    Mode: UNRESTRICTED                  ║
    ╚════════════════════════════════════════╝
    """)

def main_menu():
    while True:
        clear()
        banner()
        print("  [1] 🚫 BAN PERMANEN (No Review)")
        print("  [2] 📢 MASS REPORT (500+ Reports)")
        print("  [3] 💣 SPAM & CRASH TOOLS")
        print("  [4] 🔓 UNBAN ALL OPSI")
        print("  [5] ⚙️  TOOLS & SETTINGS")
        print("  [6] 📊 VIEW LOGS")
        print("  [0] 🚪 EXIT")
        print("\n" + "═"*45)
        
        choice = input("\n  Pilih menu [0-6]: ").strip()
        
        if choice == "1":
            ban_menu()
        elif choice == "2":
            report_menu()
        elif choice == "3":
            spam_menu()
        elif choice == "4":
            unban_menu()
        elif choice == "5":
            tools_menu()
        elif choice == "6":
            view_logs()
        elif choice == "0":
            print("\n  [!] Keluar...")
            sys.exit(0)
        else:
            print("\n  [!] Pilihan tidak valid!")
            time.sleep(1)

def ban_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         🚫 BAN PERMANEN MENU           ║
    ╚════════════════════════════════════════╝
    
    [1] Ban Satu Nomor (Permanen)
    [2] Ban Massal dari File
    [3] Ban dengan Report Bombing
    [4] Kembali ke Menu Utama
    """)
    
    choice = input("\n  Pilih [1-4]: ")
    if choice == "1":
        target = input("  Masukkan nomor target (628xxxx): ")
        ban_permanent.single_ban(target)
    elif choice == "2":
        file = input("  Masukkan nama file (targets.txt): ")
        ban_permanent.mass_ban(file)
    elif choice == "3":
        target = input("  Masukkan nomor target: ")
        count = input("  Jumlah report [500-1000]: ")
        ban_permanent.report_bomb(target, int(count))
    input("\n  Tekan Enter untuk kembali...")

def report_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         📢 MASS REPORT MENU            ║
    ╚════════════════════════════════════════╝
    
    [1] Report Standard (100 reports)
    [2] Report Extreme (1000 reports)
    [3] Report dengan Multiple Alasan
    [4] Custom Report Pattern
    [5] Kembali
    """)
    
    choice = input("\n  Pilih [1-5]: ")
    if choice in ["1", "2", "3", "4"]:
        target = input("  Nomor target: ")
        mass_report.execute(target, choice)
    input("\n  Tekan Enter untuk kembali...")

def spam_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         💣 SPAM & CRASH MENU           ║
    ╚════════════════════════════════════════╝
    
    [1] Spam Chat Extreme (1000+ pesan)
    [2] Crash Session WhatsApp
    [3] Flood Notifikasi
    [4] Corrupt Local Data (Advanced)
    [5] Kembali
    """)
    
    choice = input("\n  Pilih [1-5]: ")
    if choice in ["1", "2", "3", "4"]:
        target = input("  Nomor target: ")
        spam_crash.execute(target, choice)
    input("\n  Tekan Enter untuk kembali...")

def unban_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         🔓 UNBAN ALL OPSI              ║
    ╚════════════════════════════════════════╝
    
    [1] Unban via Appeal Bombing
    [2] Unban via Database Simulation
    [3] Unban via Device ID Randomization
    [4] Unban via Meta Insider Method
    [5] UNBAN ALL METHODS (Rekomendasi)
    [6] Cek Status Ban
    [7] Kembali
    """)
    
    choice = input("\n  Pilih [1-7]: ")
    if choice in ["1", "2", "3", "4", "5", "6"]:
        target = input("  Nomor yang ingin diunban: ")
        unban_all.execute(target, choice)
    input("\n  Tekan Enter untuk kembali...")

def tools_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         ⚙️  TOOLS & SETTINGS            ║
    ╚════════════════════════════════════════╝
    
    [1] Update Script Otomatis
    [2] Backup Data
    [3] Hapus Logs
    [4] Test Koneksi WhatsApp API
    [5] Generate Config Baru
    [6] Kembali
    """)
    
    choice = input("\n  Pilih [1-6]: ")
    tools.execute(choice)
    input("\n  Tekan Enter untuk kembali...")

def view_logs():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         📊 LOG VIEWER                  ║
    ╚════════════════════════════════════════╝
    """)
    
    log_files = os.listdir("data/logs")
    for i, log in enumerate(log_files, 1):
        print(f"  [{i}] {log}")
    
    choice = input("\n  Pilih log atau 0 untuk kembali: ")
    if choice != "0":
        try:
            with open(f"data/logs/{log_files[int(choice)-1]}", "r") as f:
                print(f.read())
        except:
            print("  [!] Gagal membaca log")
    input("\n  Tekan Enter untuk kembali...")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n  [!] Dihentikan oleh user")
        sys.exit(0)
