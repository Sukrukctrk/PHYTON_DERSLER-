# Adam asmaca oyunu

import random # Rastgele modülünü içe aktar

# Adam asmaca resimleri
resim = [
"""
 +---+
 |   |
     |
     |
     |
     |
--------""",
"""
 +---+
 |   |
 O   |
     |
     |
     |
--------""",
"""
 +---+
 |   |
 O   |
 |   |
     |
     |
--------""",
"""
 +---+
 |   |
 O   |
/|   |
     |
     |
--------""",
"""
 +---+
 |   |
 O   |
/|\  |
     |
     |
--------""",
"""
 +---+
 |   |
 O   |
/|\  |
/    |
     |
--------""",
"""
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
--------"""
]

# Kelimeler listesi
kelimeler = [
    "Adelie Pengueni", "Afgan Tazısı", "Afrika Ağaç Kurbağası", "Afrika Altın Kedisi",
    "Afrika Balık Kartalı", "Afrika Boğa Kurbağası", "Afrika Çalı Fili", "Afrika gri papağanı",
    "Afrika Jakanası", "Afrika misk kedisi", "Afrika Orman Fili", "Afrika Pençeli Kurbağası",
    "Afrika Pengueni", "Afrika Şeker Kamışı Delici", "Afrika yaban köpeği", "Agama Kertenkele",
    "Agouti", "Ağaç Engereği (Bambu Engerek)", "Ağaç kırlangıcı", "Ağaç kurbağası",
    "Ağaç sarmaşığı", "Ağaç Yılanı", "Ağaçkakan", "Ağustos böceği", "Ahır örümceği",
    "Ahtapot", "Ak balıkçıl", "Ak Kuyruklu Kartal", "Ak Omuzlu Ev Güvesi", "Akbaba",
    "Akbaş", "Akciğer balığı", "Akita", "Akrep", "Akrep balığı", "Akşam Yarasası",
    "Akvaryum balığı", "Ala Geyik", "Alabai (Orta Asya Çoban)", "Alabalık", "Alaca baykuşu",
    "Alaca Gagalı Batağan", "Alaca şahin", "Alageyik", "Alaska Çoban Köpeği", "Alaska Kurdu",
    "Alaska Pollocku", "Albacore Ton Balığı", "Albatros", "Albino (Amelanistik) Mısır Yılanı",
    "Aldabra Dev Kaplumbağa", "Allosaurus", "Alman Çoban Köpeği", "Alman Hamam böceği",
    "Alman Pinscher", "Alman Spitz’i", "Alman Şeppiti", "Alman Wirehaired Pointer",
    "Alp Keçisi", "Alpaka", "Altı Gözlü Kum Örümcekleri", "Altın Alabalık", "Altın Çakal",
    "Altın Kaplumbağa Böceği", "Altın Kartal", "Altın köstebek", "Altın Pirene",
    "Altın Taçlı Uçan Tilki", "Amano Karidesi", "Amazon Kraliyet Sinekkapanı",
    "Amazon Nehri Yunusu (Pembe Yunus)", "Amazon papağanı", "Ambrosia Böceği",
    "Amerika papağanı", "amerikan buldogu", "Amerikan Cocker Spaniel", "Amerikan Cüce Keçisi",
    "Amerikan Eskimo köpeği", "Amerikan Hamam Böceği", "Amerikan Köpek Kenesi",
    "Amerikan Kurbağası", "Amerikan Kürek Balığı", "Amerikan Leopar Tazısı",
    "Amerikan Pit Bull Teriyeri", "Amerikan Pugabull’u", "Amerikan Su Spaniel",
    "Amerikan Tazısı", "Amerikan timsahı", "Amerikan Tüysüz Terrier", "Amerikan yılan balığı",
    "Amiral kelebek", "Amur leoparı", "Anadolu Çoban Köpeği", "Anahtar geyik", "Anakonda",
    "Anka kuşu Tavuğu", "Ankara Gelinciği", "Ankara Keçisi", "Anomalocaris",
    "Antarktika Ölçekli Solucan", "Antilop", "Appenzeller Köpek", "Arafura Yılanı",
    "Arap Kobrası", "Arap kurdu", "Arap tavşanı", "Arapayma", "Arı", "Arı Kuşu",
    "Asker Böceği", "Aslan"
] 

# Rastgele bir kelime seç
kelime = random.choice(kelimeler)

# Bulunan harflerin tutulacağı yer
bulunanharfler = []

# Yanlış bulunan harflerin tutulacağı yer
yanlisharfler = []

# Oyunun bitip bitmediğini kontrol etmek için bir değişken
oyunbitti = False

# Oyun döngüsü
while not oyunbitti:
    # Adam asmaca resmini göster
    print(resim[len(yanlisharfler)])

    # Kelimeyi göster, bulunmayan harfler yerine "_" koy
    for harf in kelime:
        if harf in bulunanharfler:
            print(harf, end=" ")
        else:
            print("_", end=" ")
    print()

    # Kullanıcıdan bir harf tahmini al
    tahmin = input("Bir harf tahmin edin: ").lower()

    # Tahminin geçerli olup olmadığını kontrol et
    if len(tahmin) != 1 or not tahmin.isalpha():
        print("Lütfen geçerli bir harf girin.")
        continue

    # Tahminin daha önce girilip girilmediğini kontrol et
    if tahmin in bulunanharfler or tahmin in yanlisharfler:
        print("Bu harfi zaten girdiniz.")
        continue

    # Tahminin kelime içinde olup olmadığını kontrol et
    if tahmin in kelime:
        # Tahmini bulunan harflere ekle
        bulunanharfler.append(tahmin)
        # Kelimenin tamamen bulunup bulunmadığını kontrol et
        if set(bulunanharfler) == set(kelime):
            # Oyunu kazandığını bildir ve döngüyü kır
            print("Tebrikler, kelimeyi buldunuz!")
            oyunbitti = True
    else:
        # Tahmini yanlış harflere ekle
        yanlisharfler.append(tahmin)
        # Yanlış tahmin sayısının 6'ya ulaşıp ulaşmadığını kontrol et
        if len(yanlisharfler) == 6:
            # Oyunu kaybettiğini bildir ve döngüyü kır
            print("Üzgünüm, oyunu kaybettiniz.")
            print("Kelime", kelime, "idi.")
            oyunbitti = True

# Oyun bittiğinde tekrar oynamak isteyip istemediğini sor
if input("Tekrar oynamak ister misiniz? (e/h): ").lower() == "e":
    # Oyunu yeniden başlat
    oyunbitti = False
    bulunanharfler = []
    yanlisharfler = []
    kelime = random.choice(kelimeler)
else:
    # Oyunu bitir
    print("Oyunu oynadığınız için teşekkürler. Görüşmek üzere!")
