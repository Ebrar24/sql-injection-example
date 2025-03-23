
# Zafiyetli Kod Örneği

## 🚨 Zafiyet Türü:
- SQL Injection

## 🌐 OWASP Kategorisi:
- A03:2021 – Injection

## 🧬 Vektör String:
`CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

## 🎯 CVSS Skoru:
**9.8** (Critical)

## ✅ Düzeltme Yöntemi:
- Hazırlanmış ifadeler (prepared statements) kullanıldı.
- Doğrudan kullanıcı girdisi sorguya dahil edilmedi.

## 📹 İstismar Videosu:
[![Watch the video](https://img.youtube.com/vi/YOUTUBE_VIDEO_ID/maxresdefault.jpg)](https://www.youtube.com/watch?v=YOUTUBE_VIDEO_ID)

## 💡 Çalıştırma Talimatları:
1. Kod dosyasını çalıştır.
2. Zafiyeti tetiklemek için aşağıdaki girdileri kullan:
   ```
   Kullanıcı Adı: ' OR '1'='1
   Şifre: ' OR '1'='1
   ```
3. Zafiyetin etkisini gözlemle.
4. Güvenli sürümü çalıştır ve düzeltmenin etkisini test et.
