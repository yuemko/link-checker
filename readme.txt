# Link Checker - Basit URL Kontrol Uygulaması

✔ Belirtilen URL'nin alt dizinlerini brute-force yöntemiyle test eder.
✔ Güvenlik açığı olabilecek özel dizinleri dener (admin, login, backup, .env, vb.).
✔ HTTP yanıt kodlarına göre başarı/başarısız sonuçları listeler.

Kurulum ve Çalıştırma

 Gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
pip install flask requests
python app.py
http://127.0.0.1:5000/
