# =============================================================================
# Liste icinde elemanlardan buyuk olanlari kucuk yapip kucuk olanlari da buyuk 
# yapan sonrasinda ayri bir listeye kaydeden fonksiyon
# =============================================================================

list1 = ['merhaba', 'YABANCI', 'ali', 'Veli']

def any_func():
    
    list_temp = list1.copy()
    for i in list1:
        if i.islower():
            list_temp.append(i.upper())
        else:
            list_temp.append(i.lower())
            
        list_temp.remove(i)
       
    return list_temp
         

list2 = any_func()



