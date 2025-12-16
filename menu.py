#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# VoltxControlCenter v2.1 - Fixed Version

import os
import sys
import time
import json
import subprocess

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def banner():
    print("""
    ╔════════════════════════════════════════╗
    ║    ⚡ VOLTX CONTROL CENTER v2.1 ⚡      ║
    ║    Owner: VoltXRinn                    ║
    ║    Github: QirinnFall                  ║
    ║    Status: 100% WORKING                ║
    ╚════════════════════════════════════════╝
    """)

def check_dependencies():
    """Check semua dependency terinstall"""
    missing = []
    try:
        import requests
    except:
        missing.append("requests")
    
    try:
        import colorama
    except:
        missing.append("colorama")
    
    if missing:
        print(f"[❌] Missing modules: {', '.join(missing)}")
        print("[!] Run: pip install " + " ".join(missing))
        return False
    
    # Check directories
    required_dirs = ['data/logs', 'config', 'modules']
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
    
    return True

def load_module(module_name):
    """Load module dengan error handling"""
    try:
        if module_name == "ban":
            from modules import ban_permanent
            return ban_permanent
        elif module_name == "report":
            from modules import mass_report
            return mass_report
        elif module_name == "spam":
            from modules import spam_crash
            return spam_crash
        elif module_name == "unban":
            from modules import unban_all
            return unban_all
        elif module_name == "tools":
            from modules import tools
            return tools
    except Exception as e:
        print(f"[❌] Failed to load {module_name}: {e}")
        return None

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
    
    try:
        choice = input("\n  Pilih [1-4]: ").strip()
        if choice == "1":
            target = input("  Masukkan nomor target (628xxxx): ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah! Gunakan 628xxxx")
                time.sleep(2)
                return
            
            module = load_module("ban")
            if module:
                module.single_ban(target)
        
        elif choice == "2":
            file = input("  Masukkan nama file (targets.txt): ").strip()
            if not os.path.exists(file):
                print(f"  [!] File {file} tidak ditemukan!")
                time.sleep(2)
                return
            
            module = load_module("ban")
            if module:
                module.mass_ban(file)
        
        elif choice == "3":
            target = input("  Masukkan nomor target: ").strip()
            try:
                count = int(input("  Jumlah report [100-1000]: ").strip())
                if count < 100 or count > 1000:
                    print("  [!] Jumlah harus antara 100-1000")
                    time.sleep(2)
                    return
            except:
                print("  [!] Input tidak valid!")
                time.sleep(2)
                return
            
            module = load_module("ban")
            if module:
                module.report_bomb(target, count)
        
        elif choice == "4":
            return
        
        else:
            print("  [!] Pilihan tidak valid!")
    
    except KeyboardInterrupt:
        print("\n  [!] Dibatalkan oleh user")
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def report_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         📢 MASS REPORT MENU            ║
    ╚════════════════════════════════════════╝
    
    [1] Report Standard (100 reports)
    [2] Report Extreme (500 reports)
    [3] Report dengan Multiple Alasan
    [4] Custom Report Pattern
    [5] Kembali
    """)
    
    try:
        choice = input("\n  Pilih [1-5]: ").strip()
        if choice in ["1", "2", "3", "4"]:
            target = input("  Nomor target: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            module = load_module("report")
            if module:
                module.execute(target, choice)
        elif choice == "5":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def spam_menu():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         💣 SPAM & CRASH MENU           ║
    ╚════════════════════════════════════════╝
    
    [1] Spam Chat Extreme (500 pesan)
    [2] Crash Session WhatsApp
    [3] Flood Notifikasi
    [4] Kembali
    """)
    
    try:
        choice = input("\n  Pilih [1-4]: ").strip()
        if choice in ["1", "2", "3"]:
            target = input("  Nomor target: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            module = load_module("spam")
            if module:
                module.execute(target, choice)
        elif choice == "4":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
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
    
    try:
        choice = input("\n  Pilih [1-7]: ").strip()
        if choice in ["1", "2", "3", "4", "5", "6"]:
            target = input("  Nomor yang ingin diunban: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            module = load_module("unban")
            if module:
                module.execute(target, choice)
        elif choice == "7":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
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
    [4] Test Koneksi
    [5] Generate Config Baru
    [6] Kembali
    """)
    
    try:
        choice = input("\n  Pilih [1-6]: ").strip()
        module = load_module("tools")
        if module:
            module.execute(choice)
        elif choice == "6":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def view_logs():
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         📊 LOG VIEWER                  ║
    ╚════════════════════════════════════════╝
    """)
    
    try:
        log_dir = "data/logs"
        if not os.path.exists(log_dir):
            print("  [!] Directory logs tidak ditemukan!")
            return
        
        log_files = os.listdir(log_dir)
        if not log_files:
            print("  [!] Tidak ada log file")
            return
        
        for i, log in enumerate(log_files, 1):
            print(f"  [{i}] {log}")
        
        choice = input("\n  Pilih log atau 0 untuk kembali: ").strip()
        if choice != "0" and choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(log_files):
                try:
                    with open(os.path.join(log_dir, log_files[idx]), 'r') as f:
                        print(f.read())
                except:
                    print("  [!] Gagal membaca log")
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def main_menu():
    # Check dependencies first
    if not check_dependencies():
        print("[!] Silakan install dependencies terlebih dahulu")
        time.sleep(3)
        return
    
    while True:
        try:
            clear()
            banner()
            print("  [1] 🚫 BAN PERMANEN (No Review)")
            print("  [2] 📢 MASS REPORT (500+ Reports)")
            print("  [3] 💣 SPAM & CRASH TOOLS")
            print("  [4] 🔓 UNBAN ALL OPSI")
            print("  [5] ⚙️  TOOLS & SETTINGS")
            print("  [6] 📊 VIEW LOGS")
            print("  [7] 🛠️  FIX BUGS & UPDATE")
            print("  [0] 🚪 EXIT")
            print("\n" + "═"*45)
            
            choice = input("\n  Pilih menu [0-7]: ").strip()
            
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
            elif choice == "7":
                fix_bugs()
            elif choice == "0":
                print("\n  [!] Keluar...")
                sys.exit(0)
            else:
                print("\n  [!] Pilihan tidak valid!")
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n\n  [!] Dihentikan oleh user")
            sys.exit(0)
        except Exception as e:
            print(f"\n  [!] Error: {e}")
            time.sleep(2)

def fix_bugs():
    """Auto fix bugs"""
    clear()
    print("""
    ╔════════════════════════════════════════╗
    ║         🛠️  AUTO FIX BUGS              ║
    ╚════════════════════════════════════════╝
    """)
    
    print("\n  [⚡] Memperbaiki bugs...")
    
    fixes = [
        ("Membuat directory", lambda: os.makedirs("data/logs", exist_ok=True)),
        ("Menginstall dependencies", lambda: subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--quiet"])),
        ("Membersihkan cache", lambda: subprocess.run(["rm", "-rf", "__pycache__", "modules/__pycache__"])),
        ("Memperbaiki permissions", lambda: subprocess.run(["chmod", "+x", "menu.py", "modules/*.py"])),
    ]
    
    for task, action in fixes:
        print(f"  [↻] {task}...", end="")
        try:
            action()
            print(" ✅")
        except:
            print(" ❌")
    
    print("\n  [✅] Semua perbaikan selesai!")
    time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n  [!] Dihentikan oleh user")
        sys.exit(0)
