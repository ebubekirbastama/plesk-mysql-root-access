
🔐 Plesk MySQL Root Access CLI Tool
===================================

Bu araç, Plesk paneli kurulu Linux sunucularda MySQL root erişimini kolaylaştırmak için geliştirilmiştir. 
Plesk sisteminde admin MySQL şifresi "/etc/psa/.psa.shadow" dosyasında saklanır. Bu CLI aracı, şifreyi bu dosyadan otomatik alır ve istenilen MySQL komutunu admin yetkisiyle çalıştırır.

🚀 Özellikler
------------
✅ Otomatik şifre çekme: Plesk sistem dosyasından şifreyi alır  
✅ Admin (root) yetkili MySQL bağlantısı  
✅ Komut satırından MySQL sorgusu gönderme  
✅ Kolay taşınabilir ve sade bir Python betiği  
✅ Geliştirilebilir yapı

🧩 Gereksinimler
----------------
- Python 3.x  
- MySQL client (`mysql` komutu) yüklü olmalı  
- Root yetkisine sahip bir kullanıcı

📦 Kurulum
----------
1. Bu betiği sunucunuza indirin:
   `plesk_mysql.py`

2. Çalıştırılabilir yapın:
   chmod +x plesk_mysql.py

3. Ardından doğrudan çalıştırabilirsiniz:
   ./plesk_mysql.py "SHOW DATABASES;"

🛠️ Örnek Kullanımlar
---------------------
🔹 Tüm veritabanlarını listelemek için:
./plesk_mysql.py "SHOW DATABASES;"

🔹 Kullanıcıları listelemek için:
./plesk_mysql.py "SELECT User, Host FROM mysql.user;"

⚠️ Güvenlik Notları
-------------------
⚠️ Bu araç yalnızca sistem yöneticileri veya DevOps ekipleri tarafından kullanılmalıdır.  
⚠️ /etc/psa/.psa.shadow dosyasına erişim, yalnızca yetkili kullanıcılar için sağlanmalıdır.  
⚠️ Şifreyi stdout'a yazmaz, doğrudan kullanır.

📣 Lisans
---------
MIT License ile yayınlanmıştır. İstediğiniz gibi kullanabilir, değiştirebilir , dağıtabilirsiniz fakat satamazsınız.

📞 Destek / Katkı
-----------------
Herhangi bir öneri, katkı veya hata bildirimi için GitHub üzerinden issue veya pull request gönderebilirsiniz.

👨‍💻 Hazırlayan: Ebubekir Bastama  

