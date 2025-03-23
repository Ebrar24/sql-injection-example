
import sqlite3

# Kullanıcıdan giriş alınıyor (zafiyet burada)
username = input("Kullanıcı Adı: ")
password = input("Şifre: ")

# Veritabanı bağlantısı
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Zafiyetli SQL sorgusu
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)

result = cursor.fetchone()

if result:
    print("Giriş başarılı!")
else:
    print("Geçersiz kullanıcı adı veya şifre.")

conn.close()
