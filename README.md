# Library-Automation-in-PYTHON
Bu otomasyon bir kütüphanenin ihtiyacı olabilecek 9 temel fonksiyondan oluşmaktadır. 1 adette şifre_uygun_mu fonksiyonu bulunmaktadır. Bütün fonksiyonları kontrol ettiğimiz bir tanede temel_kontrol() fonksiyonu bulunmaktadır.

## GENEL BİLGİLER
Otomasyonda ihtiyacımız olan 3 adet dosya vardır. Bunlar;
kitaplar.txt: İçinde kitapların adı, yazarı, sayfa sayısı, türü ve stok durumu sırayla yazılmıştır.
uyeler.txt: İçinde üyelerin yaşı, adı, soyadı, kullanıcı adları ve şifreleri sırasıyla bulunmaktadır.
odunc_kayıt.txt: içinde kullanıcı adı, kitap adı ve ödünç alınan tarihi(GG-AA-YYYY) şeklinde tutmaktadır.
Kütüphaneye üye olmayan kullanıcılar ödünç ve iade işlemlerini kullanamazlar.
Ödünç alınan kitaplar 15 gün içerisinde iade edilmelidir aksi takdirde her geçen gün için kütüphaneye 10TL ceza bedeli ödenmek zorundadır.

## Kitap_ekle() Fonksiyonu
Kaç adet kitap bilgisi girileceği alınarak daha kullanışlı bir fonksiyon oluşturdum. Kullanıcıdan yukarıda bahsettiğim sırada kitap bilgileri alınır. Try-except bloğu herhangi bir hata yakalamazsa bilgiler kitaplar.txt dosyasına yazılır.

## Kitap_sil() Fonksiyonu
kitaplar.txt dosyası okunarak bilgiler tutulur. Kullanıcıdan silmek istediği kitabın ismi alınır. Dosyadan gelen bilgilerle kontrol edilerek eğer kitap dosyada varsa dosya tekrar yazılırken eklenmez sonucunda silinmiş olur.

## Arama_yap() Fonksiyonu
Kullanıcıya aramak istediği kitabın adı sorulur. Eğer dosya okunduktan sonra bulunamazsa KİTAP KÜTÜPHANEMİZDE BULUNMAMAKTADIR! Uyarısı verip temel_kontrol fonksiyonuna geri dönmektedir. Kitap bulunduğu durumda kullanıcıya iki seçenek sunulur; 
1-)KİTABI SİL 2-)ÖDÜNÇ AL kullanıcı seçimini yapınca seçilen fonksiyonların çağrısı yapılır.
Kütüphanede herhangi bir kitap bilgisi yoksa KÜTÜPHANEDE ARANACAK KİTAP BİLGİSİ BULUNMAMAKTADIR! Uyarısı vermektedir.

## Uyelik_olustur() Fonksiyonu
Kullanıcıdan yukarıda bahsedilen sırada bilgileri alır. Kullanıcı adı eşsiz olmalıdır bu yüzden kontrolleri yapılması için kullanici_adi_uygun_mu(nickname) fonksiyonu yazılmıştır uyelik_olustur fonksiyonunun içerisine. Girilen şifrenin şu özellikleri sağlaması gerekmektedir: 
Türkçe karakter içermemelidir. 
En az bir tane rakam içermelidir. 
En az bir tane büyük harf ve bir tane küçük harf içermelidir. 
En az 6 karakter uzunluğunda olmalıdır.
Bu kontrolleri yapması için girilen şifreyi parametre olarak alan sifre_uygun_mu() fonksiyonu yazılmıştır.
Üyelik bilgileri uyeler.txt dosyasına yazılır.

## Listele() Fonksiyonu
Kullanıcıya üyeler ya da kitapları listelemek için seçenek sunulur yapılan seçime göre listele fonksiyonunun içerisinde bulunan kitap_listele() ve uye_listele() fonksiyonları çağrılır. Seçime göre hangi dosya varsa okunur eğer dosya boşsa yani bilgi bulunmuyorsa gerekli uyarı mesajları verilerek temel_kontrol fonksiyonuna döner.

## kitap_odunc() Fonksiyonu
Kullanıcıya üyelik durumu sorulur yoksa ve üye olmak istiyorsa uyelik_olustur fonksiyonu çağrılır.
Üyeyse kullanıcı adı ve şifre sorulur yanlış girilmesi halinde uyarı mesajı verilir ve temel_kontrol fonksiyonuna dönülür.
Kullanıcıya ödünç almak istediği kitap sorulur, tarih alınır ve kitabı getirmesi gereken gün sayısı bilgisi verilir.
Kullanıcının aldığı kitabın stok sayısı azaltılır.
İstenilen kitabın stokta olmaması halinde gerekli uyarı mesajı verilir.
Ödünç alınma bilgileri odunc_kayıt.txt dosyasına yazılır.

## kitap_iade() Fonksiyonu
Kullanıcıya kullanıcı adı ve şifresi sorulur. Yanlış olması durumunda hata mesajı verilerek temel_kontrol fonksiyonuna dönülür.
İade edilecek kitabın ismi sorulur, tarih alınır ve ödünçteki tarihten çıkarmak için kitap_iade fonksiyonunun içerisindeki fonksiyonlara gider. Asgari günü geçtiyse uyarı mesajı verilir ödemesi gereken ücret hesaplanır ve bildirilir.
İade alınan kitabın stok durumu arttırılır.
Girilen isimde bir kitap ödünç alınmadıysa gerekli uyarı mesajını verir temel_kontrol fonksiyonuna döner.
odunc_kayıt.txt dosyasından silinir.

## sifre_guncelle() Fonksiyonu
Kullanıcıya kullanıcı adı ve eski şifresi sorulur. Yanlış girildiğinde uyarı mesajları verilir. Doğru olduğunda yeni şifre sorulur ve sifre_uygun_mu() fonksiyonuna gönderilir. Şifre uygun olana kadar tekrar alınır. Yeni şifre uyeler.txt dosyasında da güncellenir.

## cikis() Fonksiyonu
ÇIKIŞ YAPILIYOR... mesajı vererek sistemden çıkar.

## sifre_uygun_mu() Fonksiyonu
Harfleri büyük ve küçük şeklinde bir kümeye dönüştürür. Rakamları ve Türkçe karakterleri de kümeye dönüştürür. Parametre olarak gelen şifreyi de kümeye dönüştürür. Kümelerin kesişimlerine bakarak False ya da True döndürür.

## temel_kontrol() Fonksiyonu
Kullanıcıya bir menü sunar. Kullanıcının seçim yapması istenir.
Bütün fonksiyonların atıflarını bir sözlükte tutar ve kullanıcının girdiği değere göre fonksiyonların çağrısı sağlanır.
