import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_name="alraed_vault.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        # إنشاء قاعدة بيانات مشفرة لإدارة مشاريع المؤسسة
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS projects 
                          (id INTEGER PRIMARY KEY, name TEXT, status TEXT, encryption_key TEXT)''')
        conn.commit()
        conn.close()
        print(f"[DATABASE]: Vault {self.db_name} is Secure and Ready.")

if __name__ == "__main__":
    db = DatabaseManager()
