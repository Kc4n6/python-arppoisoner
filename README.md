# python-arppoisoner/arppoisoning.py

Bu araç python ile yazılmış, bulunduğunuz ağda aktif olan cihazlardan birinin ip adresini, gateway ip adresini ve ağ kartınızın
adını verdiğinizde gerekli bilgileri arp tablosundan alır ve ağda sizin için sahte arp paketlerini belirli aralıklar ile gönder-
meye başlar. Bu şekilde hedef ve gateway arasında gelip giden paketler sizin cihazınızın üstünden geçer. uçtan uca şifreleme 
sağlanmayan uygulamalarda kullanıcı adı, parola gibi önemli bilgilerin bulunduğu paketleri bir ağ dinleme aracı ile izleyerek
ele geçirmenize yardımcı olur. !!!!!Windows için henüz aktif değil. Bir sonraki geliştirmede onu da ekleyeceğim. 
Windows aktif değil neden seçim şansı veriyorsun diyenler olacaktır. Haklılar ama o kısmı yazmasam windows için de geliştirmez-
dim. Bena dürtü olması için sordum yani :D 

superuser yetkileri ile çalışması gerekmektedir.!!!!!

Gerektirdiği kütüphaneler:
  getmac
  binascii
  struct
  
# python-arppoisoner/changemac.py
Bu araç, parametre olarak verilen ag kartının mac adresini, hexadecimal karakterlerden rastgele yeni bir mac adresi oluşturarak değiştirir.
