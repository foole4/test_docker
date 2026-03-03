Имя файла: entrypoint.sh

#!/bin/bash
set -e

echo "🔄 Синхронизация с GitHub..."
cd /app
git pull origin main --ff-only || git reset --hard origin/main

echo "✅ Запускаем тестовый скрипт..."
exec python test.py

Commit changes
