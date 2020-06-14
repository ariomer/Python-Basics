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
