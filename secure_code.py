
import sqlite3

# Kullanıcıdan giriş alınıyor
username = input("Kullanıcı Adı: ")
password = input("Şifre: ")

# Veritabanı bağlantısı
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Hazırlanmış ifadeler (SQL Injection önleniyor)
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Giriş başarılı!")
else:
    print("Geçersiz kullanıcı adı veya şifre.")

conn.close()
