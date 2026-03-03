#!/usr/bin/env python3
import time
import os
import threading
from datetime import datetime

print("🚀 === ДОКЕР ТЕСТ СЕРВЕР ЗАПУЩЕН ===")
print(f"📅 Время запуска: {datetime.now().strftime('%H:%M:%S')}")
print(f"📂 Рабочая папка: {os.getcwd()}")
print(f"📄 Файлы: {os.listdir('.')}")

# Имитация сетевого сервера (ваш proxy)
def fake_server():
    port = 8000
    print(f"🌐 Fake Proxy Server слушает порт {port}")
    counter = 0
    while True:
        counter += 1
        print(f"📨 Клиент #{counter}: команда обработана в {datetime.now().strftime('%H:%M:%S')}")
        time.sleep(3)

# Запуск сервера в фоне
server_thread = threading.Thread(target=fake_server, daemon=True)
server_thread.start()

# Основной цикл 24/7
print("✅ Сервер переходит в режим 24/7...")
uptime = 0

while True:
    uptime += 3
    print(f"⏰ Uptime: {uptime//60}м {uptime%60}с | Docker: OK | GitHub: SYNC")
    time.sleep(3)
