# calculator


# ..::HESAPLAMAYI YAPAN FONKSIYON
def calculator():
    a = int(input('\n1.sayiyi giriniz: '))
    b = int(input('\n2.sayiyi giriniz: '))
    if islem == 1:
        print('\n..::Toplama Islemi Sonucu::.. => ', a+b)
    elif islem == 2:
        print('\n..::Cikarma Islemi Sonucu:::.. => ', a-b)
    elif islem == 3:
        print('\n..::Carpma Islemi Sonucu:::.. => ', a*b)
    else:
        print('\n..::Bolme Islemi Sonucu:::.. => ', a/b)


while True: # KULLANICI CIKMAK ISTEYENE KADAR PROGRAM CALISMAYA DEVAM EDER
    print("""
          \n=> Toplama: 1
          \n=> Cikarma: 2
          \n=> Carpma: 3
          \n=> Bolme: 4
          \n=> Yeter Bu Kadar, Cikar Beni Buradan:): 5 \n""")
    islem = int(input('\nYukaridan Yapmak Istediginiz Islemi Seciniz(1-5 Arasi Olmali): '))
    if 0 < islem <= 4: # 1 ILE 4 ARASINDA BIR SAYI GIRILDIGINDE 'CALCULATOR' FONKSIYONU CAGRILIR
        calculator()
        print('\nBaska bir islem yapmak ister misiniz?(Y/N)')
        devam = str(input('\nSeciminizi yapiniz: ')) # KULLANICIYA ISLEME DEVAM EDIP ETMEYECEGINI SORULUR
        if devam == 'Y' or 'y':  # BUYUK 'Y' YA DA 'y' GIRILMESI DURUMUNDA DEVAM EDER, DEGILSE PROGRAMDAN CIKAR
            continue
        else:
            quit()
    elif islem == 5: # PROGRAMDAN CIKMAK ICIN 5'E BASILMASI YETERLIDIR
         quit()
    else: # 1 ILE 5 ARASINDAKI SAYILARDAN FARKLI BIR SAYI GIRILIRSE KULLANICIYA TEKRARDAN SECIM YAPILMASI SOYLENIR
        print('\n\!!!!!!\nYALNIS SECIM YAPTINIZ TEKRARDAN BIR DEGER GIRINIZ:\n!!!!!!')
