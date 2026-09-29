import math

# ──────────────────────────────────────────────
#  Yardımcı Fonksiyonlar
# ──────────────────────────────────────────────

def sayi_al(mesaj: str) -> float:
    """Kullanıcıdan geçerli bir sayı alana kadar tekrar sorar."""
    while True:
        try:
            return float(input(mesaj))
        except ValueError:
            print("Hata: Lütfen geçerli bir sayı giriniz!")


def tam_sayi_al(mesaj: str) -> int:
    """Kullanıcıdan geçerli bir tam sayı alana kadar tekrar sorar."""
    while True:
        try:
            return int(input(mesaj))
        except ValueError:
            print("Hata: Lütfen geçerli bir tam sayı giriniz!")


def sonuc_yazdir(sonuc: float) -> None:
    """Sonucu düzgün formatta yazdırır (tam sayıysa ondalık göstermez)."""
    if sonuc == int(sonuc):
        print(f"İşleminizin sonucu: {int(sonuc)}")
    else:
        print(f"İşleminizin sonucu: {sonuc}")


def sonuc_derece_yazdir(sonuc: float) -> None:
    """Derece cinsinden sonucu yazdırır."""
    if sonuc == int(sonuc):
        print(f"İşleminizin sonucu: {int(sonuc)} derece")
    else:
        print(f"İşleminizin sonucu: {sonuc} derece")


def kayan_nokta_duzelt(deger: float) -> float:
    """Kayan nokta hassasiyet hatalarını düzeltir (ör: sin(180°) ≈ 1e-16 → 0)."""
    if math.isclose(deger, 0.0, abs_tol=1e-9):
        return 0.0
    if math.isclose(deger, 1.0, abs_tol=1e-9):
        return 1.0
    if math.isclose(deger, -1.0, abs_tol=1e-9):
        return -1.0
    return deger


# ──────────────────────────────────────────────
#  Basit Mod İşlemleri
# ──────────────────────────────────────────────

def toplama():
    x = sayi_al("Birinci sayıyı giriniz: ")
    y = sayi_al("İkinci sayıyı giriniz: ")
    sonuc_yazdir(x + y)


def cikarma():
    x = sayi_al("Birinci sayıyı giriniz: ")
    y = sayi_al("İkinci sayıyı giriniz: ")
    sonuc_yazdir(x - y)


def carpma():
    x = sayi_al("Birinci sayıyı giriniz: ")
    y = sayi_al("İkinci sayıyı giriniz: ")
    sonuc_yazdir(x * y)


def bolme():
    x = sayi_al("Birinci sayıyı giriniz: ")
    while True:
        y = sayi_al("İkinci sayıyı giriniz: ")
        if y == 0:
            print("Hata: Sıfıra bölme yapılamaz! Tekrar deneyin.")
        else:
            sonuc_yazdir(x / y)
            return


def basit_mod():
    """Basit mod menüsünü gösterir ve seçilen işlemi çalıştırır."""
    print("Seçtiğiniz mod: Basit Mod")

    islemler = {
        "+": toplama,
        "-": cikarma,
        "*": carpma,
        "/": bolme,
    }

    secim = input("Yapmak istediğiniz işlem nedir? [Toplama(+), Çıkarma(-), Çarpma(*), Bölme(/)]: ").strip()

    if secim in islemler:
        islemler[secim]()
    else:
        print("Hata: Lütfen geçerli bir işlem seçiniz!")


# ──────────────────────────────────────────────
#  Gelişmiş Mod İşlemleri
# ──────────────────────────────────────────────

def kuvvet_alma():
    x = sayi_al("Taban değerini giriniz: ")
    y = sayi_al("Kuvvet değerini giriniz: ")

    if x == 0 and y == 0:
        print("Sonuç tanımsızdır! (0^0)")
    else:
        sonuc_yazdir(math.pow(x, y))


def kok_alma():
    while True:
        x = sayi_al("Kökü alınacak sayıyı giriniz: ")
        if x < 0:
            print("Hata: Negatif sayının karekökü alınamaz! Tekrar deneyin.")
        else:
            sonuc_yazdir(math.sqrt(x))
            return


def logaritma():
    while True:
        x = sayi_al("Logaritması alınacak sayıyı giriniz (10 tabanında): ")
        if x <= 0:
            print("Hata: Sıfır veya negatif sayının logaritması alınamaz! Tekrar deneyin.")
        else:
            sonuc_yazdir(math.log10(x))
            return


# ── Trigonometri ──

def trig_sin():
    x = sayi_al("Derece cinsinden açı giriniz: ")
    sonuc_yazdir(kayan_nokta_duzelt(math.sin(math.radians(x))))


def trig_cos():
    x = sayi_al("Derece cinsinden açı giriniz: ")
    sonuc_yazdir(kayan_nokta_duzelt(math.cos(math.radians(x))))


def trig_tan():
    x = sayi_al("Derece cinsinden açı giriniz: ")
    radyan = math.radians(x)
    cos_degeri = math.cos(radyan)

    if math.isclose(cos_degeri, 0.0, abs_tol=1e-9):
        print("Hata: Tanjant bu açıda tanımsızdır!")
    else:
        sonuc_yazdir(kayan_nokta_duzelt(math.tan(radyan)))


def trig_cot():
    while True:
        x = sayi_al("Derece cinsinden açı giriniz: ")
        radyan = math.radians(x)
        sin_degeri = math.sin(radyan)
        cos_degeri = math.cos(radyan)

        if math.isclose(sin_degeri, 0.0, abs_tol=1e-9):
            print("Hata: Kotanjant bu açıda tanımsızdır! Tekrar deneyin.")
        else:
            sonuc = cos_degeri / sin_degeri
            sonuc_yazdir(kayan_nokta_duzelt(sonuc))
            return


def trig_asin():
    while True:
        x = sayi_al("Oran giriniz (-1 ile 1 arasında): ")
        if -1 <= x <= 1:
            sonuc_derece_yazdir(math.degrees(math.asin(x)))
            return
        else:
            print("Hata: Oran -1 ile 1 arasında olmalıdır!")


def trig_acos():
    while True:
        x = sayi_al("Oran giriniz (-1 ile 1 arasında): ")
        if -1 <= x <= 1:
            sonuc_derece_yazdir(math.degrees(math.acos(x)))
            return
        else:
            print("Hata: Oran -1 ile 1 arasında olmalıdır!")


def trig_atan():
    x = sayi_al("Oran giriniz: ")
    sonuc_derece_yazdir(math.degrees(math.atan(x)))


def trig_acot():
    x = sayi_al("Oran giriniz: ")
    if x == 0:
        sonuc_derece_yazdir(90.0)
    else:
        sonuc = math.degrees(math.atan(1 / x))
        if sonuc < 0:
            sonuc += 180
        sonuc_derece_yazdir(sonuc)


def trigonometri():
    """Trigonometri alt menüsünü gösterir."""
    trig_islemler = {
        1: ("Sin",  trig_sin),
        2: ("Cos",  trig_cos),
        3: ("Tan",  trig_tan),
        4: ("Cot",  trig_cot),
        5: ("Asin", trig_asin),
        6: ("Acos", trig_acos),
        7: ("Atan", trig_atan),
        8: ("Acot", trig_acot),
    }

    secim = tam_sayi_al(
        "Trigonometrik fonksiyon seçiniz\n"
        "  [Sin(1), Cos(2), Tan(3), Cot(4), Asin(5), Acos(6), Atan(7), Acot(8)]: "
    )

    if secim in trig_islemler:
        trig_islemler[secim][1]()
    else:
        print("Hata: Lütfen geçerli bir fonksiyon seçiniz!")


def gelismis_mod():
    """Gelişmiş mod menüsünü gösterir ve seçilen işlemi çalıştırır."""
    print("Seçtiğiniz mod: Gelişmiş Mod")

    islemler = {
        1: ("Kuvvet alma",  kuvvet_alma),
        2: ("Kök alma",     kok_alma),
        3: ("Logaritma",    logaritma),
        4: ("Trigonometri",  trigonometri),
    }

    secim = tam_sayi_al(
        "Yapmak istediğiniz işlem nedir?\n"
        "  [Kuvvet alma(1), Kök alma(2), Logaritma/10 tabanında/(3), Trigonometri(4)]: "
    )

    if secim in islemler:
        islemler[secim][1]()
    else:
        print("Hata: Lütfen geçerli bir işlem seçiniz!")


# ──────────────────────────────────────────────
#  Ana Döngü
# ──────────────────────────────────────────────

def main():
    modlar = {
        1: ("Basit Mod",    basit_mod),
        2: ("Gelişmiş Mod", gelismis_mod),
    }

    while True:
        secim = tam_sayi_al("\nLütfen bir mod seçiniz [Basit Mod(1), Gelişmiş Mod(2), Çıkış(3)]: ")

        if secim == 3:
            print("Hesap makinesi kapatılıyor....")
            break
        elif secim in modlar:
            modlar[secim][1]()
        else:
            print("Hata: Lütfen geçerli bir mod seçiniz!")


if __name__ == "__main__":
    main()
