#!/usr/bin/env python
# coding: utf-8

# # Uygulama: 2. Hafta

# 1. En basit hali ile bir fonksiyon tanimlayip fonksiyonu cagiriniz. (Calistiriniz.)

# In[1]:


def func_1():
    print('Function')


# In[2]:


func_1()


# 2. Tek argumanli (parametreli), return'u olmayan bir fonksiyon tanimlayiniz, fonksiyonu cagiriniz.

# In[3]:


def func_1(a):
    print('Fonksiyonun icine yazilan deger: ', a)

func_1(100)


# 3. Tek argumanli, return'u (geri donutu) olan bir fonksiyon tanimlayiniz, fonksiyonu cagiriniz.

# In[4]:


def func_1(a, b = 100):
    return a + b

func_1(100)


# 4. Tek argumanli, return ile geri donutu olan bir fonksiyon tanimlayiniz, fonksiyonu cagiriniz, 'sonuc' adli bir degisken ile geri donutu yakalayiniz (atama ile kaydediniz), 'sonuc' degiskenini yazdiriniz.

# In[5]:


def func_1(a, b = 100):
    return a + b

sonuc = func_1(100)
sonuc


# 5. Asagida bir dataframe'in bir degiskeni secilmis tweets_lang adi ile kaydedilmistir. 
# sonuc olarak  {'en': 97, 'et': 1, 'und': 2} seklinde sozluk yapisinda bir ciktisi olan kodlari yaziniz

# In[13]:


import pandas as pd 
tweets_df = pd.read_csv('tweets.csv')
tweets_lang = tweets_df['lang']
tweets_lang.head(10)


# In[48]:


tweets_lang.value_counts()


# In[49]:


sozluk = tweets_lang.value_counts()


# In[50]:


sozluk.to_dict()


# 6. Yukarida yazmis oldugunuz kodlara fonksiyon giydirerek tekrar ayni sonucu yazdiriniz.

# In[51]:


def dict1():
    sozluk = tweets_lang.value_counts()
    sozluk = sozluk.to_dict()
    return sozluk


# In[52]:


dict1()


# 7. Default argumani olan bir fonksiyon tanimlayiniz, fonksiyonu argumansiz calistiriniz, ayrica argumana farkli bir deger girerek calistiriniz.

# In[53]:


def default_arg(a = 10):
    print(a**2)


# In[55]:


default_arg()


# In[56]:


default_arg(5)


# 8. Uc adet argumani olan bir fonksiyon tanimlayiniz, iki tanesinin default degeri olsun. Farkli varyasyonlarda fonksiyonu cagiriniz.

# In[58]:


def func3(c, a = 2, b = 4):
    print(a * b * c)


# In[60]:


func3(1)


# In[64]:


func3(1,3)


# 9. Sicaklik birimlerinden Celsius'u Kelvine ceviren fonksiyonu yaziniz.

# In[72]:


def temp(c):
    k = c + 273.15
    print (str(c),'Celcius derece =>', str(k) + ' Kelvin derecedir')      


# In[73]:


temp(30)


# 10. Input fonksiyonu ile 24h formatinda girilen saat icin asagidaki kurallara gore belirtilen arsilama mesajini yazdiriniz.

# In[83]:


saat = input('Saati giriniz: ')
dakika = input('Dakikayi giriniz: ')
print (str(saat), ':', str(dakika))


# 11. Altinci soruda yazdiginiz fonksiyonun argumanini degistirerek ayni sonucu default arguman kullanarak yazdiriniz. Not: kolon_adi='lang' ifadesini kullaniniz.

# In[ ]:





# 12. 'python' ile 'Python' ifadelerinin esit olup olmadigini gosteriniz

# In[86]:


'python' == 'Python'


# 13. Asagidaki degiskenleri kullanarak dersin matematik olup olmadigini kontrol eden, matematik ise "Matematik sinavi aciklandi" ifadesi yazdiran, ayrica puanin 65'ten buyuk olup olmadigini kontrol eden ve 65'ten buyuk ise 'Sinavi Gectiniz' ifadesini cikti olarak yazan kodlari yaziniz.
ders = "matematik"
puan = 90
# In[2]:


ders = str(input('Ders Adi :'))

if ders == 'matematik':
    print('Matematik Sinavi Aciklandi')
    puan = int(input('Puani Giriniz: '))
    if puan > 65:
        print('Sinavi Gectiniz')
    else:
        print('Kaldiniz')
else:
    print('Sinav sonucu henuz aciklanmadi')


# 14. Bir ustteki kodu editleyip tekrar yaziniz: Eger ders 'matematik' degil ise "Matematik sinavi aciklanmadi" yazilsin. Ayrica puan'in 65'ten kucuk olmasi halinde "Sinavdan kaldiniz" ifadesi yazilsin.

# In[3]:


ders = str(input('Ders Adi :'))

if ders == 'matematik':
    print('Matematik Sinavi Aciklandi')
    puan = int(input('Puani Giriniz: '))
    if puan > 65:
        print('Sinavi Gectiniz')
    else:
        print('Kaldiniz')
else:
    print('Sinav sonucu henuz aciklanmadi')


# 15. Bir liste olusturunuz ve for ile bu listenin elemanlarini yazdiriniz

# In[4]:


liste = [1,10,100,40,30]
for i in liste:
    print(i)


# 16. Bir ustte yapiginiz islemi elemanlari otomatik numaralandirarak tekrar yazdiriniz

# In[12]:


import random
liste = []

for i in range(5):
    n = random.randint(0,10)
    liste.append(n)
liste


# 17. Asagida verilen A listesindeki elemanlari for dongusu kullanarak B listesine tasiyiniz.

# In[13]:


A = [10,11,12,13,14,15,16]
B = []

for i in A:
    B.append(i)
B


# 18. Asagida verilen A listesindeki cift sayilari for dongusu kullanarak B listesine tasiyiniz.

# In[18]:


A = [10,11,12,13,14,15,16]
B = []

for i in A:
    if i % 2 == 0:
        B.append(i)
B


# 19. Asagidaki listeleri kullanarak belirtilen sonucu for dongusu kullanarak yazdiriniz.

# In[28]:


adj = ["yellow", "big", "tasty"]
fruits = ["apple", "banana"]
print('CIKTI:')
for x in adj:
    for y in fruits:
        print(x,y)


# 20. Carpim tablosunu for donguleri ile yazdiriniz.

# In[30]:


for x in range(1,10):
    for y in range(1,11):
        print(x, '*', y, '=', x*y)


# 21. 2000 yilinin subat ayi 29 gun olduguna gore, 2100 yilina kadar subat ayinin 29 gun oldugu yillari for dongusu kullanarak yazdiriniz.

# In[38]:


subat_29 = 0
for i in range(2000,2101):
    if i % 4 == 0:
        subat_29 = subat_29 + 1
subat_29


# 22. 2000 ile 2100 (yillari dahil olmak uzere) arasinda subat ayinin 29 oldugu yillarin sayisini hesaplayiniz.

# In[39]:


for i in range(2000,2101):
    if i % 4 == 0:
        print(i)


# 23. Basitlestirilmis bir Bowling oyunu icin bir puan hesaplama yapilmasi isteniyor.
# - atis_yap() adinda bir fonksiyon yaziniz, bu fonksiyon 0'dan 10'a kadar olan sayilardan rasgele birini secsin, ve yazdirsin.
# - Eger atis_yap() fonksiyonu 10 sayisini tutturursa Ekrana "Strike!" yazilsin.

# In[100]:


import random
def atis_yap():
    n = random.randint(0,10)
    return n
    if n == 10:
        print('Strike!')


# In[80]:


atis_yap()


# 24. For dongusu kullanarak arguman olarak girilen sayinin faktöriyelini hesaplayan fonksiyonu yaziniz.

# In[157]:


sonuc = 1
f = int(input('Bir deger giriniz:'))
for i in range(1,(f+1)):
    sonuc = sonuc * i
print(sonuc)   


# 25. Arguman olarak aldigi kelimeyi tersten yazdiran ayrica ilk harfini buyuk, kalani kucuk harfle yazdiran fonksiyonu yaziniz.

# In[171]:


a = input('Kelime giriniz:')
b = a[::-1].title()
print(a, '=>', b )

ORNEK:
Armut -> Tumra
Kalem -> Melak