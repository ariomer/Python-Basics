#!/usr/bin/env python
# coding: utf-8

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


# #### 6. Slice

# In[7]:


yazi_icin = arac_gerec[:4]
print(yazi_icin)

cantada = arac_gerec[0:6]

evde = arac_gerec[6:10]

print(cantada)
print(evde)


# #### 7. Alternatif slice

# In[16]:


yazi_icin = arac_gerec[:4]
print(yazi_icin)

cantada = arac_gerec[:6]

evde = arac_gerec[-4:]

print(cantada)
print(evde)


# #### 8. Cift indeks

# In[17]:


canta = [["defter", dftr], ["kalem", klm], ["kitap", ktp], ["silgi", slg], ["cetvel", ctvl]]

print( canta[-1][1] )


# #### 9. Listelerde degisiklik:

# In[41]:


arac_gerec = ["defter", dftr, "kalem", klm, "kitap", ktp, "silgi", slg, "cetvel", ctvl]

arac_gerec[-1] = 5  #  4 -> 5

arac_gerec[-2] = "pergel"  # cetvel -> pergel

print(arac_gerec)


# #### 10. Listeleri birlestirme:

# In[42]:


arac_gerec_1 = arac_gerec + ["uc", 1]

arac_gerec_2 = arac_gerec_1 + ['hesap makinesi', 15]

print(arac_gerec)
print(arac_gerec_1)
print(arac_gerec_2)


# #### SORU 2
# Soru1'de olusturdugunuz liste icin slice ile listenin bir altkumesini seciniz farkli bir ad ile kaydediniz ve yazdiriniz.
# Yeni olusturdugunuz bu listedeki notu degistiriniz ve yazdiriniz.

# #### COZUM

# In[16]:


notlar = ['Turkce: ', 50, 'Sosyal :', 60, 'Matematik :', 90, 'Fen :', 80]
sos_mat = notlar[2:6]


# In[7]:


notlar = ['Turkce: ', 50, 'Sosyal :', 60, 'Matematik :', 90, 'Fen :', 80]
sos_mat = notlar[2:6]
print(sos_mat)
sos_mat[1] = 50
print(sos_mat)


# #### 11. Liste elemani silmek .remove()

# In[43]:


del( arac_gerec_2[13] )
del( arac_gerec_2[12] )

arac_gerec_2.remove(1)
arac_gerec_2.remove('uc')

print( arac_gerec_2)


# #### 12. Liste yedegi uzerinde calismak:

# In[36]:


listem = [2,4,6,8,10] 

listem_yedek = listem.copy()

# veya:  listem_yedek = list(listem)

listem_yedek[0] = 12

print(listem_yedek)
print(listem)

NOT: 
    kod1
    kod2
yukarida iki ayri kod farkli satirlarda calistirilabildigi gibi tek satirda aralarina ; koyarak da calistirilabilir
    kod1; kod2
# #### 13. len( list1 )

# In[27]:


degisken = [1,2,3,4]

print(type(degisken))

print(len(degisken))


# #### 14. help() veya ?
help(ornek_fonksiyon) veya 
?ornek_fonksiyon 
ile ornek_fonksiyon adli bir fonksiyon hakkinda ayrintili bilgi alabilriz:
# In[ ]:


get_ipython().run_line_magic('pinfo', 'max')


# In[28]:


help(sum)


# #### 15. sorted() fonksiyonu veya .sort()

# In[48]:


tekler = [1,3,5,7,9]
ciftler = [0,2,4,6,8]

rakamlar = tekler + ciftler
print(rakamlar)

# rakamlar_sirali = rakamlar.sort()

rakamlar_sirali = sorted(rakamlar)
print(rakamlar_sirali)

rakamlar_sirali2 = sorted(rakamlar, reverse=True)
print(rakamlar_sirali2)


# #### SORU 3
# Soru1'de olusturdugunuz listenin bir kopyasi uzerinde calisip, Sosyal dersi ve notunu siliniz. Listenin son halini yazdiriniz.
# Bu listenin eleman sayisini yazdiriniz.

# #### COZUM

# In[27]:


notlar = ['Turkce: ', 50, 'Sosyal :', 60, 'Matematik :', 90, 'Fen :', 80]
notlar_copy = notlar.copy()
notlar_copy.remove('Sosyal :')
notlar_copy.remove(60)
print(notlar_copy)
len(notlar_copy)


# #### 16. liste metotlari: .upper() ve .count()

# In[22]:


# NOT: stringler ayni zamanda karakterlerden olusan birer listedir
kurs = "veribilimiegitimi"

kurs2 = kurs.upper()

print(kurs)
print(kurs2)

print(kurs.count('i'))


# #### 17. liste metotlari: .index()

# In[50]:


fiyatlar = [10, 8, 12, 3, 4, 3]

print(fiyatlar.index(8))

print(fiyatlar.count(3))


# #### 18. Liste metotlari: .append() .remove() .reverse()

# In[52]:


fiyatlar = [10, 8, 12, 3, 4, 3]

fiyatlar.append(20)
fiyatlar.append(15)
print(fiyatlar)

fiyatlar.reverse()

print(fiyatlar)


# #### SORU 4
# Soru1'de olusturdugunuz listeye Ingilizce dersini ve bir not ekleyiniz. Listeyi yazdiriniz.

# #### COZUM

# In[31]:


notlar = ['Turkce: ', 50, 'Sosyal :', 60, 'Matematik :', 90, 'Fen :', 80]
notlar.append('Ingilizce :')
notlar.append(80)
print(notlar)


# In[ ]:




