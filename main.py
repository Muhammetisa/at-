import math
import random

def atis_sayisi_ve_hiz_bul():
    # Topun başlangıç hızı
    hiz_alt_sinir = 330
    hiz_ust_sinir = 1800
    ilk_hiz = (hiz_alt_sinir + hiz_ust_sinir) / 2

    # Hedef özellikleri
    uzaklik_mesafesi = 20000 + 200 * random.randint(-10, 10)
    genislik_baslangic = uzaklik_mesafesi
    genislik_bitis = uzaklik_mesafesi + 1000 + 100 * random.randint(-2, 2)

    # Hedefin önünde veya arkasında olma durumu
    hedef_onunde = False

    # Atış sayısı
    atis_sayisi = 0

    # Atış yapılacak yükseklik (deniz seviyesinden okul numarasının son 2 hanesi kadar yükseklik)
    top_konumu = [0, 0]  # Burayı kendi okul numaranızın son 2 hanesine göre ayarlayın

    while True:
        # Atış sayısını arttır
        atis_sayisi += 1

        # Atış yap
        hiz = ilk_hiz
        if hedef_onunde:
            hiz_alt_sinir = hiz
        else:
            hiz_ust_sinir = hiz
        hiz = (hiz_alt_sinir + hiz_ust_sinir) / 2

        # Hedefi vurup vuramadığını kontrol et
        vuruldu_mu, hedef_onunde = hedefi_vur(hiz, top_konumu, uzaklik_mesafesi, genislik_baslangic, genislik_bitis)

        # Eğer hedef vurulduysa veya hedef önünde veya arkasında değilse döngüden çık
        if vuruldu_mu or not hedef_onunde:
            break

    return atis_sayisi, hiz

def hedefi_vur(hiz, top_konumu, uzaklik_mesafesi, genislik_baslangic, genislik_bitis):
    # Fiziksel sabitler
    g = 9.81  # Yer çekimi ivmesi (m/s^2)

    # Atış açısı (radyan cinsinden)
    atis_acisi = math.radians(30)

    # Atışın süresi
    t_uclus = 2 * hiz * math.sin(atis_acisi) / g

    # Atışın menzili
    x_menzil = hiz * math.cos(atis_acisi) * t_uclus

    # Atışın yüksekliği
    yukseklik = hiz * math.sin(atis_acisi) * t_uclus - 0.5 * g * t_uclus ** 2

    # Atışın düştüğü yerin koordinatları
    dusus_yeri = [x_menzil, yukseklik + top_konumu[1]]

    # Hedefin konumu
    hedef_merkez = (genislik_baslangic + genislik_bitis) / 2

    # Eğer düşüş yeri, hedefin önünde ise
    if dusus_yeri[0] < hedef_merkez:
        hedef_onunde = True
    else:
        hedef_onunde = False

    # Eğer düşüş yeri hedefin içindeyse vuruş başarılıdır
    if genislik_baslangic <= dusus_yeri[0] <= genislik_bitis:
        return True, hedef_onunde
    else:
        return False, hedef_onunde

# Atış sayısı ve gerekli hızı bul
atis_sayisi, gereken_hiz = atis_sayisi_ve_hiz_bul()
print("Gerekli atış sayısı:", atis_sayisi)
print("Gerekli hız:", gereken_hiz)