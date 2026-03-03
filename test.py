#!/usr/bin/env python3
import time
import os
from datetime import datetime

print("🚀 [DOCKER TEST] Сервер запущен!")
print(f"📅 {datetime.now().strftime('%H:%M:%S')}")
print(f"📁 {os.getcwd()}")
print("✅ GitHub → Docker → Python = OK")

# БЕСКОНЕЧНЫЙ ЦИКЛ ДЛЯ 24/7
counter = 0
print("🔄 Режим 24/7 активирован...")
while True:
    counter += 1
    print(f"⏰ Uptime: {counter}s | Docker: UP | GitHub: SYNC")
    time.sleep(2)
