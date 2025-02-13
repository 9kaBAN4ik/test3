import sqlite3

from config import DB_PATH

# Подключение к базе данных
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Очистка таблицы lottery
cursor.execute("DELETE FROM lottery")

# Сброс автоинкрементного счетчика (если есть столбец id с AUTOINCREMENT)
cursor.execute("DELETE FROM sqlite_sequence WHERE name='lottery'")

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
