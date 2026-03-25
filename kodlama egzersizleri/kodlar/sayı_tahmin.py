# sayı tahmin oyunu

import random
import time


rastgele_sayı= random.randint(500,984)

tahmin_hakkı=7

while True:

    tahmin=int(input("tahmininiz"))

    if tahmin < rastgele_sayı:
        print("bilgiler sorgulanıyor")
        time.sleep(1)
        print("daha yüksek bir sayı söyleyin")

        tahmin_hakkı-=1

  
    elif tahmin >rastgele_sayı:
        print("bilgiler sorgulanıyor")
        time.sleep(1)

        print("daha düşük bir sayı söyleyin")

        tahmin_hakkı-=1

    else:
        print("tebrikler doğru tahmin ettiniz")
        

    if tahmin_hakkı==0:
        print("tahmin hakkınız tükenmiştir")
        