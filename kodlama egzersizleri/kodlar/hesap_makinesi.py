import math 
işlem = input(" yapmak istdeniz işlemi giriniz")

if işlem == "factorial":
     sayı= int(input("lütfen sayı giriniz"))

     print(math.factorial(sayı))

elif işlem== "toplama":
     sayı= int(input("sayı giriniz"))
     sayı1=int(input("sayı giriniz"))
     print(sayı+sayı1)

elif işlem== "çıkarma":
     sayı= int(input("sayı giriniz"))
     sayı1=int(input("sayı giriniz"))
     print(sayı-sayı1)

elif    işlem== "çarpma":
     sayı= int(input("sayı giriniz"))
     sayı1=int(input("sayı giriniz"))
     print(sayı*sayı1)  

elif işlem== "bölme":
     sayı= int(input("sayı giriniz"))
     sayı1=int(input("sayı giriniz"))
     print(sayı/sayı1)  

elif  işlem== "kök alma":
     sayı= int(input("sayı giriniz"))
     
     print(sayı*1/2)

elif işlem== "mutlak değer":
     sayı= int(input("sayı giriniz"))


 
elif işlem  == "negatif karekök":
     sayı = int(input("sayı giriniz"))

     print(math.isqrt(sayı))


elif  işlem  == "küpkök":
     sayı = int(input("sayı giriniz"))

     print(sayı *1/3)

else :
   print("hatalı işlem girdiniz")
   
     
