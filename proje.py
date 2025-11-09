
#HURİYE DURSUN 24100011012

def kitap_ekle():
    try :
        adet = int(input("Kaç Adet Kitap Girişi Yapacaksınız?:"))
        if adet<=0 :
            raise ValueError #adet negatif olamaz
        for i in range(adet) :
            ad=input(f"{i+1}.KİTABIN ADINI GİRİNİZ:")
            yazar=input("KİTABIN YAZARININ ADINI GİRİNİZ:")
            s_s= int(input("KİTABIN SAYFA SAYISINI GİRİNİZ:"))
            tur=input("KİTABIN TÜRÜNÜ GİRİNİZ:")
            s_a= int(input("KİTABIN STOK ADETİNİ GİRİNİZ:"))

            with open("kitaplar.txt", "a", encoding="utf-8") as dosya :
                dosya.write(ad + " > ")
                dosya.write(yazar + " > ")
                dosya.write(str(s_s)+ " > ")
                dosya.write(tur + " > ")
                dosya.write(str(s_a) + "\n")
            print(f"{i+1}.KİTAP BAŞARIYLA KÜTÜPHANEMİZE EKLENMİŞTİR..")
    except ValueError :
        print("GEÇERSİZ GİRİŞ LÜTFEN POZİTİF VE SIFIRDAN FARKLI BİR SAYI GİRİNİZ")
    except IOError as e :
        print(f"DOSYA İŞLEMLERİNDE HATA OLUŞTU/{e}")

def kitap_sil():
    dosya='kitaplar.txt'
    try :
        def kitap_oku() :
            try:
                with open("kitaplar.txt", "r", encoding="utf-8") as f:
                    item = f.readlines()  # okunan satırlar geri gönderiliyor
                return item
            except FileNotFoundError:
                print("DOSYA BULUNAMADI.")
                return [] #none dönmesin diye
        def istenilen_kitap_sil(satirlar_gelen,kitap_silinecek):
            yenisatirlar = []
            kontrol = False #kitap silinmedi
            try :
                for item in satirlar_gelen:
                    satir_parcalari = item.strip().split('>')
                    if satir_parcalari[0].strip().lower() != kitap_silinecek.strip().lower(): # ilk elemanda kitapların adı var o yüzden 0'ı alıyoruz
                        #girilen adın buyuk kucuk harfe duyarsız olması için lower kullandım
                        #dosyaya kaydederken boşluklu olması durumunda strip ile boşlukları temizledim ki kıyaslama doğru yapılabilsin
                        yenisatirlar.append(item) #silmek istediğimiz dışındakileri listeye ekliyoruz
                    else:
                        kontrol = True #kitap silindi
                return yenisatirlar,kontrol
            except (IndexError, AttributeError) as error :  # satır parçaları aldığımız kısım index hatası oluşturabilir
                print(f"HATA OLUŞTU/{error}")               #strip kullandığımız değişkenlerde sıkıntı çıkabilir
                return []
        satirlar =kitap_oku() #fonksiyon bize satır satır okuma bilgisi verecek
        if not satirlar : # okunan dosyada hiç kayıt yoksa uyarı verir
            print("KÜTÜPHANEDE KAYITLI KİTAP YOK DOLAYISIYLA ŞUAN KİTAP SİLEMEZSİNİZ")
            return
        sil =input("SİLMEK İSTEDİĞİNİZ KİTABIN İSMİNİ GİRİNİZ:").strip()
        yeni_satirlar, silindi_mi=istenilen_kitap_sil(satirlar,sil) # silmek istediğimiz kitap için fonk.çağırıyoruz

        if silindi_mi  : # 1 ise çalışır ve yeni satırları aynı dosyaya geri yazarsak silmiş oluruz
            with open(dosya, 'w', encoding="utf-8") as file: # w moduyla açıyoruzki baştaki verilerin hepsini silsin
                file.writelines(yeni_satirlar)
            print("..KİTAP BAŞARIYLA SİLİNDİ..")
        else : # kontrolun 0 olduğu durum yani istenen kitap bulunamamış
            print("..KİTAP BULUNAMADI..")
    except TypeError as type_error :  # yukardan ındex error gelirse değişkenler none olduğu için type error alabiliriz
        print(f"BİR HATA OLUŞTU/{type_error}")
    except UnicodeDecodeError as hata :   # türkçe karakterlerde sıkıntı çıkabilir
        print(f"HATA OLUŞTU/{hata}")

def arama_yap():

    aranan_ad=input("ARAMAK İSTEDİĞİNİZ KİTABIN ADINI GİRİNİZ:").strip()

    try :
        with open("kitaplar.txt", "r", encoding="utf-8") as f :
            data_kitaplar=f.readlines()
    except FileNotFoundError:
        print("DOSYA BULUNAMADI!")
        return
    if len(data_kitaplar)==0 :
        print("KÜTÜPHANEDE ARANACAK KİTAP BİLGİSİ BULUNMAMAKTADIR!")
        return

    try :
        bulundu_mu= False
        for item in data_kitaplar :
            kitap=item.strip().split(">")
            if kitap[0].strip().lower()==aranan_ad.lower() :
                bulundu_mu= True
                print(f"{kitap[0]}ADLI KİTAP BULUNDU NE YAPMAK İSTERSİNİZ?")
                while True :
                    secim=int(input("1-)KİTABI SİL\n2-)ÖDÜNÇ AL\nSEÇİMİNİZİ YAPINIZ:"))
                    if secim==1 :
                        kitap_sil()
                        break
                    elif secim==2 :
                        kitap_odunc()
                        break
                    else:
                        print("LÜTFEN GEÇERLİ BİR SEÇİM YAPINIZ!")
        if not bulundu_mu :
            print(f"{aranan_ad} ADLI BİR KİTAP KÜTÜPHANEMİZDE BULUNMAMAKTADIR!")
    except ValueError :
        print("LÜTFEN BİR SAYI GİRİŞİ YAPINIZ!")
    except IndexError as e:
        print(f"BİR HATA OLUŞTU/{e}")

def uyelik_olustur():

    def kullanici_adi_uygun_mu(nickname) :
        try:
            kontrol= False
            with open("uyeler.txt", "r", encoding="utf-8") as file :
                data= file.readlines() # liste halinde satirlari döndürüyor
            for item in data :
                satir= item.strip().split('>')
                if satir[3].strip() == nickname :
                    print("BU KULLANICI ADI BİR BAŞKASI TARAFINDAN KULLANILMAKTADIR!")
                    return False #aynı nicknamei kullanan bulunca direkt geri dönecek
                else:
                    kontrol= True #nickname alınabilirse true
            return kontrol
        except FileNotFoundError :
            print("DOSYA BULUNAMADI")
            return []
        except IndexError as e :
            print(f"HATA/{e}")
            return []

    try :
        with open("uyeler.txt", "a", encoding="utf-8") as dosya :
            yas = int(input("YAŞINIZI GİRİNİZ:"))
            dosya.write(str(yas) + " > ")
            dosya.write(input("İSMİNİZ NEDİR?:") + " > ")
            dosya.write(input("SOYADINIZ NEDİR?:") + " > ")
        while True :
            kul_adi = input("KULLANICI ADINIZI BELİRLEYİNİZ:")
            if kullanici_adi_uygun_mu(kul_adi) : #fonk.True gelirse gircek
                with open("uyeler.txt", "a", encoding="utf-8") as f :
                    f.write(kul_adi + " > ")
                break

        while True :
            sifre=input("ŞİFRENİZİ BELİRLEYİNİZ:")
            if sifre_uygun_mu(sifre) : # fonk.true geldiyse bloğun içine gircek
                print("Belirlediğiniz şifre uygun")
                with open("uyeler.txt", "a", encoding="utf-8") as dosya :
                    dosya.write(sifre + " ")
                    dosya.write("\n")
                break
        print("..ÜYELİĞİNİZ BAŞARIYLA OLUŞTURULMUŞTUR..")
        print("ÖDÜNÇ İŞLEMİ İÇİN MENÜDEN TEKRAR SEÇİM YAPABİLİRSİNİZ")
    except IOError as hata :
        print(f"DOSYA İŞLEMLERİNDE HATA OLUŞTU/{hata}")
    except ValueError :
        print("LÜTFEN YAŞ BİLGİLERİNİZİ DÜZGÜN GİRİNİZ!")

def listele():

    def kitap_listele() :
        try :
            with open("kitaplar.txt", "r", encoding="utf-8") as file :
                satirlar =file.readlines()#okunan satirları satır satır liste halinde tutuyor

                if len(satirlar)==0 :
                    print("KÜTÜPHANEDE LİSTELENECEK KİTAP BİLGİSİ BULUNMAMAKTADIR")
                    return

                print("\033[1;45m" + "═" * 94 + "\033[0m")
                print("\033[1;45m║ {:<25} │ {:<25} │ {:<8} │ {:<15} │ {:<5} ║\033[0m".format("AD", " YAZAR", " SAYFA", " TÜR", "STOK"))

                for item in satirlar :
                    data = item.strip().split(">")
                    if len(data) >= 5 : # kitap eklerken hatalı eklenen satır varsa atlamak için
                        print("║ {:<25} │ {:<25} │ {:<8} │ {:<15} │ {:<5} ║".format(*data))
                        #print("-" * 69)
        except FileNotFoundError :
            print("DOSYA BULUNAMADI")
        except Exception as error :
            print(f"BEKLENMEYEN BİR HATA OLUŞTU/{error}")
    def uye_listele() :
        try :
            with open("uyeler.txt", "r", encoding="utf-8") as file :
                satirlar= file.readlines()

                if len(satirlar) ==0 :
                    print("KÜTÜPHANEDE KAYITLI ÜYE BİLGİSİ BULUNMAMAKTADIR")
                    return

                print("\033[1;44m" + "═" * 57 + "\033[0m")
                print("\033[1;44m║ {:<5} │ {:<13} │ {:<13} │ {:<13} ║\033[0m".format("YAŞ", " İSİM", " SOYAD", " NICKNAME"))

                for item in satirlar :
                    data = item.strip().split(">")
                    if len(data) >= 4 : #uye eklerken hatalı eklenen satır varsa atlamak için
                        print("║ {:<5} │ {:<13} │ {:<13} │ {:<13} ║".format(*data))
                        #print("-" * 45)
        except FileNotFoundError :
            print("DOSYA BULUNAMADI")
        except Exception as error :
            print(f"BEKLENMEYEN BİR HATA OLUŞTU/{error}")
    try :
        while True :
            secim=int(input("1-)KİTAPLAR\n2-)ÜYELER\nLİSTELEMEK İSTEDİĞİNİZ KATEGORİYİ SEÇİNİZ:"))
            if secim==1 :
                kitap_listele()
                break
            elif secim==2 :
                uye_listele()
                break
            else : #1,2 dışında bişey girildiğinde
                raise ValueError

    except ValueError :
        print("LÜTFEN GEÇERLİ BİR SEÇİM YAPINIZ!")
        listele()
    except Exception as e :
        print(f"BEKLENMEYEN BİR HATA OLUŞTU/{e}")

def kitap_odunc():

    uyelik_durumu=input("KÜTÜPHANEYE ÜYE MİSİNİZ? (E/H)\nSADECE ÜYE OLAN KULLANICILAR ÖDÜNÇ İŞLEMLERİNE DEVAM EDEBİLİR:")

    if uyelik_durumu.lower()=='h' : # uye değilse
        secim=input("ÜYE OLMAK İSTER MİSİNİZ?(E/H):")
        if secim.lower()=='e' :
            uyelik_olustur()
        else :
            return
    #BUNUN ALTINDAKİ TÜM KODLAR ELSE BLOĞU İÇİNDE
    else : #üye olduğu durum
        kul_adi=input("KULLANICI ADINIZI GİRİNİZ:")
        sifre=input("ŞİFRENİZİ GİRİNİZ:")

        try :
            with open("uyeler.txt", "r", encoding="utf-8") as f :   #dosyadan uyeleri satir satir okuyup liste halinde uyeler değişkenine attık
                uyeler=f.readlines()
        except FileNotFoundError :
            print("DOSYA BULUNAMADI")

        giris_kontrol= False
        for item in uyeler :
            uye=item.strip().split(">") #uyenin bilgilerini uye değişkenine aldık
            if len(uye) < 5 : # dosyada bilgileri eksik olan uye varsa atlamak için
                continue
            if uye[3].strip()==kul_adi and uye[4].strip()== sifre :
                giris_kontrol= True
                print("GİRİŞ BAŞARILI!")
                break        # uye bulunduysa devamını okumaya gerek yok o yüzden break kullanıyoruz

        if not giris_kontrol :
            print("\033[1;31mKULLANICI ADI VEYA ŞİFRE HATALI!\033[0m")
            return #hatalı bilgi varsa sisteme giriş yapamayacak o yüzden return kullanıyoruz

        try :
            with open("kitaplar.txt", "r", encoding="utf-8") as f :
                kitaplar=f.readlines()
        except FileNotFoundError :
            print("DOSYA BULUNAMADI!")
            return # dosya bulunamadıysa devam etmeyecek
        if len(kitaplar)==0 :  #eğer kitap bilgisi yoksa işlemlere devam etmesin
            print("KÜTÜPHANEDE KAYITLI KİTAP BİLGİSİ BULUNMAMAKTADIR!")
            return
        odunc_istenen_ad=input("ÖDÜNÇ ALMAK İSTEDİĞİNİZ KİTABIN ADINI GİRİNİZ:").strip()
        odunc_alinan_tarih= input("TARİHİ GİRİNİZ (GG-AA-YYYY) :").strip()
        yeni_satirlar= [] # odunc alınan kitabın stok durumunu güncelleyeceğimiz için yeni satirlar listesine ihtiyacımız var
        kitap_bulundu_mu= False
        stok_var =False

        for item in kitaplar :
            kitap=item.strip().split(">")
            ad_kitap= kitap[0].strip()
            stok=int(kitap[4].strip()) #dosyada string şeklindeydi stok sayısını değiştireceğimiz için int değere çevirdik

            if ad_kitap.strip().lower()== odunc_istenen_ad.strip().lower() :
                kitap_bulundu_mu= True
                if stok>0 : # stok durumu kitabı almaya uygunsa
                    stok_var= True
                    kitap[4]= str(stok-1) # kitap bulundu ve stok yeterliyse stok 1 azaltılarak tekrar dosyaya yazılmalı

                    try :
                        global iade_suresi, gecen_gun_ucreti
                        with open("odunc_kayit.txt", "a", encoding="utf-8") as file :
                            file.write(f"{kul_adi} > {odunc_istenen_ad} > {odunc_alinan_tarih}\n")
                        print("..KİTAP BAŞARIYLA ÖDÜNÇ ALINDI..")
                        print(f"\033[1:32mÖDÜNÇ ALDIĞINIZ KİTAPLARI {iade_suresi} GÜN İÇERİSİNDE KÜTÜPHANEMİZE İADE ETMELİSİNİZ\033[0m")
                        print(f"\033[1:32mHER GEÇEN GÜN {gecen_gun_ucreti}TL İLE ÜCRETLENDİRİLMEKTEDİR\033[0m")
                    except FileNotFoundError :
                        print("KAYITLAR DOSYAYA YAZILAMADI")

                else :
                    print("KİTAP STOKTA BULUNMAMAKTADIR ÜZGÜNÜZ!")

                yeni_satir = ">".join(kitap) + "\n"  #stok durumu değiştirilen kitap satırı yeniden yazılıp yeni_satir değişkenine atılıyor
            else :    # gelen itemin istenen kitap olmadığı durumda
                yeni_satir =item #kitabın stok durumu değiştirilmeden yenisatira yazılıyor

            yeni_satirlar.append(yeni_satir) # hala for döngüsündeyiz her kitabın bilgileri listeye eklenecek
        if kitap_bulundu_mu and stok_var :
            try :
                with open("kitaplar.txt", "w", encoding="utf-8") as f : #w moduyla açıyoruz ki önceki bilgiler silinip stokları güncellenmiş hali yeniden yazılsın
                    f.writelines(yeni_satirlar)
            except FileNotFoundError :
                print("KİTAPLAR DOSYASI BULUNAMADI!")
            except Exception as e :
                print(f"KİTAP DOSYASINA YAZILAMADI!/{e}")
        elif not kitap_bulundu_mu : #istenilen kitabın bulunamadığı durum
            print("KİTAP BULUNAMADI")

def kitap_iade():

    def gun_sayisina_cevirme(day,month,year) :
        ayin_gunleri = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #ayın günlerini liste halinde tutuyoruz
        ay_toplam=0
        for i in range(month-1) : #girilen ayın önceswindeki günleri toplayacak
            ay_toplam+=ayin_gunleri[i]
        toplam_gun=year*365 + ay_toplam +day
        return toplam_gun

    def tarih_farki_hesaplama(iade,odunc) : #iade ve odunc suan GG-AA-YYYY formatında bunları ayırıp gün ay yıl şeklinde almalıyız
        d1, m1, y1 = map(int, iade.split("-"))
        d2, m2, y2 = map(int, odunc.split("-"))
        gun1=gun_sayisina_cevirme(d1,m1,y1)  #iade alınan tarihin güne çevrilmiş hali buyuk
        gun2=gun_sayisina_cevirme(d2,m2,y2)  #odunc alınan tarihin güne çevrilmiş hali kucuk
        return gun1 - gun2 #aradaki farkı döndürdük

    kul_ad=input("KULLANICI ADINIZI GİRİNİZ:")
    sifre= input("ŞİFRENİZİ GİRİNİZ:")

    try:
        with open("uyeler.txt", "r", encoding="utf-8") as f:  # dosyadan uyeleri satir satir okuyup liste halinde uyeler değişkenine attık
            uyeler = f.readlines()
    except FileNotFoundError:
        print("DOSYA BULUNAMADI")
        return

    giris_kontrol = False
    for item in uyeler :
        uye = item.strip().split(">")  # uyenin bilgilerini uye değişkenine aldık
        if len(uye) < 5:  # dosyada bilgileri eksik olan uye varsa atlamak için
            continue
        if uye[3].strip() == kul_ad and uye[4].strip() == sifre:
            giris_kontrol = True
            print("GİRİŞ BAŞARILI!")
            break  # uye bulunduysa devamını okumaya gerek yok o yüzden break kullanıyoruz

    if not giris_kontrol:
        print("\033[1;31mKULLANICI ADI VEYA ŞİFRE HATALI!\033[0m")
        return  # hatalı bilgi varsa sisteme giriş yapamayacak o yüzden return kullanıyoruz

    try :
        with open("odunc_kayit.txt", "r", encoding="utf-8") as f :
            data_odunc=f.readlines()
    except FileNotFoundError :
        print("DOSYA BULUNAMADI!")
        return
    if len(data_odunc)==0 :
        print("KÜTÜPHANEDE KAYITLI ÖDÜNÇ BİLGİSİ BULUNMAMAKTADIR")
        return

    iade_kitap=input("İADE ETMEK İSTEDİĞİNİZ KİTABIN ADINI GİRİNİZ:").strip()
    iade_tarih=input("İADE TARİHİNİ GİRİNİZ (GG-AA-YYYY):").strip()

    yeni_kayit=[]
    iade_edildi_mi= False

    for item in data_odunc :
        one_person= item.strip().split(">")
        if len(one_person)<3 :
            yeni_kayit.append(item) #eksik bilgisi olanı değiştirmeden ekledik
            continue
        # one_person: [kullanıcı_adı, kitap_adı, tarih]
        if one_person[0].strip()==kul_ad and one_person[1].strip().lower()==iade_kitap.lower() :
            #global iade_suresi ,gecen_gun_ucreti
            iade_edildi_mi= True
            odunc_tarih=one_person[2].strip()
            fark=tarih_farki_hesaplama(iade_tarih,odunc_tarih)
            print("..KİTAP BAŞARIYLA İADE EDİLDİ..")
            if fark>iade_suresi :
                gecikme_bedeli=(fark-iade_suresi) * gecen_gun_ucreti
                print(f"KİTABI {fark} GÜN SONRA İADE ETTİNİZ")
                print(f"KÜTÜPHANEYE {gecikme_bedeli}TL GECİKME BEDELİ ÖDEMENİZ GEREKMEKTEDİR")
            continue #iade edilen kitabı dosyadan sileceğimiz için devam ediyoruz
        else: #gelen kullanıcı bizimki değilse yeni_kayıta ekliyoruz
            yeni_kayit.append(item)

    kitap_yeni=[]
    try :
        if iade_edildi_mi :
            with open("odunc_kayit.txt", "w", encoding="utf-8") as f:
                f.writelines(yeni_kayit) # iade edilen silinip kalanlar tekrar dosyaya yazıldı
            with open("kitaplar.txt", "r", encoding="utf-8") as f :
                kitaplar=f.readlines()
            for item in kitaplar :   #iade edilen kitabın stok durumu güncellenecek
                kitap=item.strip().split(">")
                stok=int(kitap[4].strip())
                if kitap[0].strip().lower()==iade_kitap.lower() :
                    kitap[4]=str(stok+1)#iade için arttırıyoruz
                    kitapyeni_satir = ">".join(kitap) + "\n"
                else :
                    kitapyeni_satir = item

                kitap_yeni.append(kitapyeni_satir)
            with open("kitaplar.txt", "w", encoding="utf-8") as f :
                f.writelines(kitap_yeni)
        else :
            print("BU KİTAP ADINA ÖDÜNÇ BİLGİSİ BULUNMAMAKTADIR!")
    except FileNotFoundError :
        print("DOSYA BULUNAMADI!")

def sifre_guncelle():

    try :
        with open("uyeler.txt", "r", encoding="utf-8") as f :
            satirlar=f.readlines()
    except FileNotFoundError :
        print("DOSYA BULUNAMADI!")
        return

    kul_adi=input("KULLANICI ADINIZI GİRİNİZ:")
    kontrol= False
    sifre_file=-1
    satir= None
    i=0
    for item in satirlar :
        satir=item.strip().split('>') #satir satir aldık

        if satir[3].strip() == kul_adi and len(satir) >= 5:  # 5 veriden eksik ya da fazla olan satirlari atlasın diye
            sifre_file = satir[4].strip() #eski şifreyi kaydettik
            kontrol = True #kullanıcı adı doğru ve eski şifre alındı
            break
        i += 1 # daha sonra aldığımız yeni şifreyi dosyaya yazabilmek için hangi satirda olduğunu bilmeliyiz bu yüzden eski sifreyi bulduğumuz yerden
        #en son kalan i bizim satir numaramızdır
    if kontrol :#kullanıcıyı bulduk
        sifre_eski=input("ESKİ ŞİFRENİZİ GİRİNİZ:")
        if sifre_file == sifre_eski :
            while True:
                sifre_yeni = input("YENİ ŞİFRENİZİ GİREBİLİRSİNİZ:")
                if sifre_uygun_mu(sifre_yeni) and satir is not None : #şifre şartları sağlıyorsa gircek
                    satir[4] = sifre_yeni  # yeni şifreyi liste üzerinde değiştirdik
                    satirlar[i] = '>'.join(satir) + '\n'
                    #bütün satirların olduğu yere i'yi yukarda almıştık değiştirdiğimiz satirı ekliyoruz
                    break
            try:
                with open("uyeler.txt", "w", encoding="utf-8") as file:
                    file.writelines(satirlar)
                    print("..ŞİFRENİZ BAŞARIYLA GÜNCELLENMİŞTİR..")
            except Exception as e:
                print(f"DOSYA YAZILAMADI/{e}")
        else :
            print("ŞİFREYİ YANLIŞ GİRDİNİZ!")
            return
    else : # kullanıcı bulunamadı
        print("GİRDİĞİNİZ KULLANICI ADI BULUNAMADI!")
        return

def cikis():
    print("ÇIKIŞ YAPILIYOR...")
    exit()
1

def sifre_uygun_mu(sifre) :
    global sifreuzunluk
    try :
        kontrol= True # şifre uygun
        sifrekumesi= set(sifre)
        tr_karakter=set('ığüşöçİĞÜŞÖÇ')
        rakamlar=set('1234567890')
        buyuk_harf=set('QWERTYUIOPLKJHGFDSAZXCVBNM')
        kucuk_harf= set('qwertyuopilkjhgfdsazxcvbnm')
        if sifrekumesi & tr_karakter :
            kontrol= False #şifre uygun değil
            print("Şifreniz türkçe karakter içermemelidir!")
        if not sifrekumesi & rakamlar :
            kontrol = False #şifre uygun değil
            print("Şifreniz en az bir tane rakam içermelidir!")
        if not sifrekumesi & buyuk_harf :
            kontrol= False
            print("Şifreniz en az bir tane büyük harf içermelidir!")
        if not sifrekumesi & kucuk_harf :
            kontrol= False
            print("Şifreniz en az bir tane küçük harf içermelidir!")
        if len(sifre)< sifreuzunluk :
            kontrol= False
            print(f"Şifreniz en az {sifreuzunluk} karakter uzunluğunda olmalıdır!")

        return  kontrol
    except TypeError as error :
        print(f"ŞİFRE ALINIRKEN BİR HATA OLUŞTU/{error}")
        return None
    except Exception as e :
        print(f"BEKLENMEYEN BİR HATA OLUŞTU/{e}")
        return None

def temel_kontrol():
    while True :
        fonksiyonlar={1:kitap_ekle, 2:kitap_sil, 3:arama_yap, 4:uyelik_olustur, 5:listele, 6:kitap_odunc, 7:kitap_iade, 8:sifre_guncelle, 9:cikis}
        #fonksiyon çağrısı yapmak icin sozluk kullandım
        #fonksiyonlara sadece atıfta bulunuyoruz daha sonra çağıracağız
        try :
            print("-"*40)
            print("\t\tKÜTÜPHANE İŞLEM MENÜSÜ")
            print("-"*40)
            print("1.KİTAP EKLE")
            print("2.KİTAP SİL")
            print("3.ARAMA YAP")
            print("4.ÜYELİK OLUŞTUR")
            print("5.LİSTELE")
            print("6.KİTAP ÖDÜNÇ İŞLEMLERİ")
            print("7.KİTAP İADE İŞLEMLERİ")
            print("8.ÜYE ŞİFRE GÜNCELLE")
            print("9.ÇIKIŞ YAP")

            tercih= int(input("YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ (1-9):"))
            fonksiyonlar[tercih]() #burada fonksiyonları çağırıyoruz
        except ValueError as value_error :   #girilen değer sayı değilse hata verirdi onu engelledik
            print(f"GEÇERSİZ GİRİŞ LÜTFEN SADECE SAYI GİRİNİZ!\n{value_error}")
        except KeyError :  #sözlükte olmayan bir seçim yapıldığında hata verirdi onu engelledik
            print("GEÇERSİZ GİRİŞ LÜTFEN 1-9 ARASI BİR SAYI GİRİNİZ!")
        except KeyboardInterrupt :  # Programı stop tuşuna basarak durduğumuzda hata gibi algılayıp sonlandırıyordu onu daha hoş görünmesi için burda kullandım
            print("\nKULLANICI TARAFINDAN PROGRAM SONLANDIRILDI")
            break


sifreuzunluk=6
iade_suresi=15
gecen_gun_ucreti=10
temel_kontrol() # ana fonksiyonu çağırıyoruz
