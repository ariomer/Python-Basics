#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# # Python Programlamaya Giriş

# #### 1. Matematiksel islemler

# In[1]:


# toplama 
print(7 + 7)


# In[2]:


# cikarma
print(6 - 5)


# In[3]:


# carpma 
print(4 * 5)


# In[5]:


#bolme 
print(12 / 2)


# In[8]:


#bolme (// kullanilirsa sonucu integer verir)
print(12 // 2)


# In[6]:


#mod alma 
print(10 % 7)


# In[7]:


#ustel fonk
print(5 ** 2)


# #### 2. type()

# In[9]:


print(type(15))

print(type("ornek text"))

print(type(True))


# #### 3. atama islemi

# In[10]:


x = 10

print(x)


# #### 4. string + string

# In[11]:


print( 'kirmizi' + 'balon' )


# #### 5. bir integer'i string olarak okumak:

# In[14]:


x = 50
print(type(x))

print(type(str(x)))


# #### SORU 1
# Ali'nin yasi 25'tir. Ali'nin adini ve yasini iki degiskene atayiniz. Bu degiskenleri kullanip 'Ali25' seklinde yazdiriniz.

# #### COZUM

# In[11]:


ad = 'Ali'
yas = 25
print(ad + str(yas))


# #### SORU 2
# Problem: Bir surahide 500ml su vardir. 200ml lik bardaklardan 2 bardak su ilave edilirse surahideki toplam su miktarini 900ml olacagini degisken kullanarak gosteriniz

# #### COZUM

# In[14]:


surahi = 500
bardak = 200
surahi = surahi + bardak*2
surahi


# #### 6. string ve integer'in beraber kullanimi:

# In[15]:


boy = 120
kilo = 35

print("Cocugun boyu " + str(120) + " ve kilosu " + str(35) + "'tir")


# #### 7. string * int

# In[18]:


print( 'ornek' * 3 )


# #### 8. len() fonksiyonu

# In[15]:


len('Turkiye')


# In[16]:


len('Istanbul')


# In[17]:


len('data')


# #### 9.  True ile False toplanabilir mi? neden?

# In[18]:


True + False


# #### 10. del() fonksiyonu

# In[19]:


a = 'Machine Learning'
del(a)

print(a)


# #### SORU 3

# In[24]:


degisken1 = 'veri'
degisken2 = 'bilimi'
degisken3 = 'okulu'


# Yukarida verilen degiskenleri kullanarak asagidaki ciktiyi yazdiriniz:

# #### COZUM

# In[35]:


uzunluk = len(degisken1 + '_ '*3 + degisken2 + '_'*3 + degisken3)
print(degisken1 + '_ '*3 + degisken2 + '_ '*3 + degisken3 + ' ifadesinin karakter sayisi : ' + str(uzunluk) + " 'dir.")


# #### 11. .upper() ve .lower() metotlari (method)

# In[32]:


veri1 = "Veri Bilimi"
veri2 = "veri bilimi"

print( veri1 == veri2 )


# In[33]:


veri1 = "VERI BILIMI"
veri2 = "veri bilimi".upper()

print( veri1 == veri2 )


# In[34]:


veri1 = "VERI BILIMI".lower()
veri2 = "veri bilimi"

print( veri1 == veri2 )


# #### 12. .replace() metodu

# In[36]:


veri = veri2.replace('v','V')
veri = veri.replace('b','B')

print(veri)


# #### 13. .strip() metodu

# In[23]:


yazi = 'qqqqwwwweeeeVERI BILIMIrrrrrrr'

x = yazi.strip("qwer")

print(x)


# In[42]:


yazi = "www.veribilimiokulu.com"

x = yazi.strip("w.com")

print(x)


# #### 14. dir() fonksiyonu

# In[22]:


dir(x)


# #### 15. Index 

# In[43]:


x.index('o')


# #### SORU 4 
# 'DSMLBC: data science machine learning bootcamp' string ifadesini asagisaki cikti haline getiriniz

# #### COZUM

# In[51]:


z = 'DSMLBC: data science machine learning bootcamp'
z = z.replace('d','D')
z = z.replace('s','S')
z = z.replace('m','M')
z = z.replace('l','L')
z = z.replace('b','B')
z


# #### 16. int()

# In[48]:


a = "50"
b= "80"

print(a + b)

print( int(a) + int(b) )


# #### 17. str()

# In[35]:


"String ifadelere boyle " + str(3) + " integer ekliyoruz"


# #### 18. input()

# In[53]:


not1 = input()
not2 = input()

sonuc = ( int(not1) + int(not2) ) / 2

print(sonuc)


# #### 19.

# In[54]:


print(int(sonuc))


# #### 20. float()

# In[55]:


print(float(not1))


# #### SORU 5
# Klavyeden dogum tarihi girilen bir cocugun, 2020.12.30 tarihi itibari ile kac aylik oldugunu hesaplayan bir mini uygulama kodlarini yaziniz. (1 ayi 30 gun olarak aliniz)

# #### COZUM

# In[57]:


yil = int(input('Dogum tarihi yilini giriniz:'))
ay = int(input('Dogum tarihi ayini giriniz:'))
gun = int(input('Dogum tarihi gunu giriniz:'))
hesap = (2020-yil)*12 + (12-ay) + (30-gun)/30
hesap


# #### 21. print(x, y)

# In[58]:


a = 'DataScience'
b = 'MachineLearning'
c = 'BootCamp'

print(a, b, c)


# #### 22. print(x, sep='_')

# In[59]:


print(a,b,c,sep='_')


# #### 23. print() ile tek tirnak ve cift tirnak kullanimi

# In[60]:


print('Bir atasozu der ki: "Damlaya damlaya gol olur"')


# #### 24. Substrings

# In[65]:


tweet_text = "RT @kasimecer:'yine bir BootCamp dersindeyiz'" 

print( tweet_text[15:-1])


# In[66]:


#bir baska yol
print( tweet_text[15:len(tweet_text)-1])


# #### SORU 6
# tweet_text string degiskeni icin yukarida yapilan substring islemini bir baska alternatif ile yapiniz

# #### COZUM

# In[69]:


print( tweet_text[15:44])


# In[ ]:





# # Python Programlama 102

# ## Veri Yapilari: Liste

# #### 1. Listeler olusturma

# In[70]:


dftr = 10
klm = 8
ktp = 12
slg = 2
ctvl = 4

arac_gerec = [dftr, klm, ktp, slg, ctvl]

print(arac_gerec)


# #### 2. Farkli tipte elemanlar

# In[3]:


arac_gerec = ["defter", dftr, "kalem", klm, "kitap", ktp, "silgi", slg, "cetvel", ctvl]

print(arac_gerec)


# #### 3. Liste icinde listeler

# In[4]:


canta = [["defter", dftr], ["kalem", klm], ["kitap", ktp], ["silgi", slg], ["cetvel", ctvl]]

print(canta)

print(type(canta))


# #### 4. Listelerin indeksleri ile elemanlarina ulasmak:

# In[5]:


arac_gerec = ["defter", dftr, "kalem", klm, "kitap", ktp, "silgi", slg, "cetvel", ctvl]

print(arac_gerec[1])

print(arac_gerec[-1])

print(arac_gerec[5])


# #### 5. Liste elemanlari ve islemler

# In[6]:


kalem_ve_kitap = arac_gerec[3] + arac_gerec[5]

print(kalem_ve_kitap)


# #### SORU 1
# bir ogrencinin turkce sosyal matematik ve fen derslerinin notlarini iceren bir python listesi olusturunuz. (2.adimda oldugu gibi) ve indeks kullanip bir notu yazdiriniz

# #### COZUM

# In[74]:


notlar = ['Turkce: ', 50, 'Sosyal :', 60, 'Matematik :', 90, 'Fen :', 80]
print(notlar[4], notlar[5])

