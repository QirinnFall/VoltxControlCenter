#!/bin/bash
# setup_fix.sh - Installer Utama VoltxControlCenter
# Created for VoltXRinn

echo "[⚡] MEMULAI INSTALASI VOLTXCONTROLCENTER..."
echo "[!] Pastikan koneksi internet stabil!"

# Fix directory utama
cd /data/data/com.termux/files/home 2>/dev/null || cd ~

# Hapus instalasi lama
rm -rf VoltxControlCenter_old 2>/dev/null
mv VoltxControlCenter VoltxControlCenter_old 2>/dev/null

# Buat directory baru
mkdir -p VoltxControlCenter
cd VoltxControlCenter

echo "[1] Membuat struktur directory..."
mkdir -p data/logs config modules
mkdir -p modules/__pycache__

echo "[2] Menginstall dependencies..."
pkg install python -y > /dev/null 2>&1
pip install requests colorama --quiet > /dev/null 2>&1

echo "[3] Membuat file konfigurasi..."
cat > config/settings.cfg << 'EOF'
{
  "api_key": "voltx_rinn_fixed",
  "max_threads": 30,
  "ban_timeout": 300,
  "unban_retry": 10,
  "debug_mode": false,
  "auto_update": true,
  "aggressive_mode": true,
  "version": "2.1"
}
EOF

echo '[]' > config/targets.json

echo "[4] Mengatur permissions..."
chmod 755 data data/logs config modules
chmod 644 config/*.cfg config/*.json

echo "[✅] STRUKTUR DASAR SELESAI!"
echo "[📁] Directory: ~/VoltxControlCenter"
echo "[🚀] Lanjutkan dengan membuat file menu.py"
