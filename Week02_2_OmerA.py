#!/usr/bin/env python
# coding: utf-8

# # Uygulama: 2. Hafta

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

