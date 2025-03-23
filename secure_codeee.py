# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 23:13:29 2025

@author: TR
"""

import sqlite3

# Veritabanı bağlantısını oluştur
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Tabloyu oluştur
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Örnek kullanıcı ekleyelim (Injection test etmek için)
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES ('admin', 'admin123')")
conn.commit()

conn.close()

# Kullanıcı girişini kontrol eden işlev
def login(username, password):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    
    # GÜVENLİ SORGU (Prepared Statement)
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    
    if result:
        print("Giriş başarılı!")
    else:
        print("Giriş başarısız!")

    conn.close()

# Kullanıcı girişini al
username = input("Kullanıcı Adı: ")
password = input("Şifre: ")

# Giriş fonksiyonunu çalıştır
login(username, password)
