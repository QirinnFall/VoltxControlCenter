#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# menu.py - Menu Utama VoltxControlCenter v2.1
# Owner: VoltXRinn | Github: QirinnFall

import os
import sys
import time

def clear_screen():
    """Bersihkan layar"""
    os.system('clear' if os.name != 'nt' else 'cls')

def show_banner():
    """Tampilkan banner"""
    print("""
    ╔════════════════════════════════════════╗
    ║    ⚡ VOLTX CONTROL CENTER v2.1 ⚡      ║
    ║    Owner: VoltXRinn                    ║
    ║    Status: 100% WORKING - FIXED        ║
    ║    Github: QirinnFall                  ║
    ╚════════════════════════════════════════╝
    """)

def check_environment():
    """Cek environment dan dependencies"""
    print("[🔍] Memeriksa environment...")
    
    # Cek directory
    required_dirs = ['data/logs', 'config', 'modules']
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)
            print(f"  [✓] Membuat directory: {dir_path}")
    
    # Cek dependencies
    try:
        import requests
        import colorama
        print("  [✓] Dependencies: OK")
        return True
    except ImportError as e:
        print(f"  [✗] Error: {e}")
        print("  [⚠] Jalankan: pip install requests colorama")
        return False

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
        print(f"[✗] Gagal load module {module_name}: {e}")
        return None

def menu_ban():
    """Menu Ban Permanen"""
    clear_screen()
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
        pilihan = input("\n  Pilih [1-4]: ").strip()
        
        if pilihan == "1":
            target = input("  Masukkan nomor target (628xxxx): ").strip()
            if len(target) < 10:
                print("  [!] Nomor tidak valid!")
                time.sleep(2)
                return
            
            modul = load_module("ban")
            if modul:
                modul.single_ban(target)
        
        elif pilihan == "2":
            file = input("  Nama file target (contoh: targets.txt): ").strip()
            if not os.path.exists(file):
                print(f"  [!] File {file} tidak ditemukan!")
                time.sleep(2)
                return
            
            modul = load_module("ban")
            if modul:
                modul.mass_ban(file)
        
        elif pilihan == "3":
            target = input("  Masukkan nomor target: ").strip()
            try:
                jumlah = int(input("  Jumlah report [100-500]: ").strip())
                if jumlah < 100 or jumlah > 500:
                    print("  [!] Jumlah harus 100-500")
                    time.sleep(2)
                    return
            except:
                print("  [!] Input tidak valid!")
                time.sleep(2)
                return
            
            modul = load_module("ban")
            if modul:
                modul.report_bomb(target, jumlah)
        
        elif pilihan == "4":
            return
        
        else:
            print("  [!] Pilihan tidak valid!")
    
    except KeyboardInterrupt:
        print("\n  [!] Dibatalkan")
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def menu_report():
    """Menu Mass Report"""
    clear_screen()
    print("""
    ╔════════════════════════════════════════╗
    ║         📢 MASS REPORT MENU            ║
    ╚════════════════════════════════════════╝
    
    [1] Report Standard (100 reports)
    [2] Report Extreme (300 reports)
    [3] Report Multi-Alasan
    [4] Kembali
    """)
    
    try:
        pilihan = input("\n  Pilih [1-4]: ").strip()
        if pilihan in ["1", "2", "3"]:
            target = input("  Nomor target: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            modul = load_module("report")
            if modul:
                modul.execute(target, pilihan)
        elif pilihan == "4":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def menu_spam():
    """Menu Spam & Crash"""
    clear_screen()
    print("""
    ╔════════════════════════════════════════╗
    ║         💣 SPAM & CRASH MENU           ║
    ╚════════════════════════════════════════╝
    
    [1] Spam Chat (100 pesan)
    [2] Crash Session
    [3] Flood Notifikasi
    [4] Kembali
    """)
    
    try:
        pilihan = input("\n  Pilih [1-4]: ").strip()
        if pilihan in ["1", "2", "3"]:
            target = input("  Nomor target: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            modul = load_module("spam")
            if modul:
                modul.execute(target, pilihan)
        elif pilihan == "4":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def menu_unban():
    """Menu Unban All"""
    clear_screen()
    print("""
    ╔════════════════════════════════════════╗
    ║         🔓 UNBAN ALL OPSI              ║
    ╚════════════════════════════════════════╝
    
    [1] Unban via Appeal Bombing
    [2] Unban via Database Simulation
    [3] Unban via Device Randomization
    [4] Unban All Methods
    [5] Cek Status Ban
    [6] Kembali
    """)
    
    try:
        pilihan = input("\n  Pilih [1-6]: ").strip()
        if pilihan in ["1", "2", "3", "4", "5"]:
            target = input("  Nomor target: ").strip()
            if not target.startswith("628"):
                print("  [!] Format nomor salah!")
                time.sleep(2)
                return
            
            modul = load_module("unban")
            if modul:
                modul.execute(target, pilihan)
        elif pilihan == "6":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def menu_tools():
    """Menu Tools & Settings"""
    clear_screen()
    print("""
    ╔════════════════════════════════════════╗
    ║         ⚙️  TOOLS & SETTINGS            ║
    ╚════════════════════════════════════════╝
    
    [1] Update Script
    [2] Backup Data
    [3] Hapus Logs
    [4] Test Koneksi
    [5] Generate Config
    [6] Kembali
    """)
    
    try:
        pilihan = input("\n  Pilih [1-6]: ").strip()
        modul = load_module("tools")
        if modul:
            modul.execute(pilihan)
        elif pilihan == "6":
            return
        else:
            print("  [!] Pilihan tidak valid!")
    
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def view_logs():
    """Lihat logs"""
    clear_screen()
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
        
        files = os.listdir(log_dir)
        if not files:
            print("  [!] Tidak ada log file")
            return
        
        for i, file in enumerate(files, 1):
            print(f"  [{i}] {file}")
        
        pilihan = input("\n  Pilih log (0 untuk kembali): ").strip()
        if pilihan != "0" and pilihan.isdigit():
            idx = int(pilihan) - 1
            if 0 <= idx < len(files):
                try:
                    with open(os.path.join(log_dir, files[idx]), 'r') as f:
                        print(f"\n{'='*40}")
                        print(f.read())
                        print(f"{'='*40}")
                except:
                    print("  [!] Gagal membaca file")
    except Exception as e:
        print(f"  [!] Error: {e}")
    
    input("\n  Tekan Enter untuk kembali...")

def main_menu():
    """Menu utama"""
    if not check_environment():
        print("[✗] Environment check gagal!")
        time.sleep(3)
        return
    
    while True:
        try:
            clear_screen()
            show_banner()
            print("  [1] 🚫 BAN PERMANEN (No Review)")
            print("  [2] 📢 MASS REPORT (300+ Reports)")
            print("  [3] 💣 SPAM & CRASH TOOLS")
            print("  [4] 🔓 UNBAN ALL OPSI")
            print("  [5] ⚙️  TOOLS & SETTINGS")
            print("  [6] 📊 VIEW LOGS")
            print("  [0] 🚪 EXIT")
            print("\n" + "═"*45)
            
            pilihan = input("\n  Pilih menu [0-6]: ").strip()
            
            if pilihan == "1":
                menu_ban()
            elif pilihan == "2":
                menu_report()
            elif pilihan == "3":
                menu_spam()
            elif pilihan == "4":
                menu_unban()
            elif pilihan == "5":
                menu_tools()
            elif pilihan == "6":
                view_logs()
            elif pilihan == "0":
                print("\n  [!] Keluar dari VoltxControlCenter...")
                sys.exit(0)
            else:
                print("\n  [!] Pilihan tidak valid!")
                time.sleep(1)
        
        except KeyboardInterrupt:
            print("\n\n  [!] Program dihentikan")
            sys.exit(0)
        except Exception as e:
            print(f"\n  [!] Error: {e}")
            time.sleep(2)

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\n  [!] Dihentikan oleh user")
        sys.exit(0)
