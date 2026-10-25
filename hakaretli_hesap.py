#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kendine Hakaret Eden Hesap Makinesi
Her işlemde seni aşağılar. Ciddiye alma, ama alma.
"""

import random

# Hakaret havuzu - genişletilebilir, ama zaten yeterince kötü
hakaretler = [
    "Senin beynin bu işlemi yapamayacak kadar küçük mü?",
    "Bu kadar basit bir şeyi bile hesaplayamıyorsan, hayatta ne işe yarıyorsun?",
    "Sonuç çıktı ama sen çıkmadın, çünkü zekan yok.",
    "Matematik senin için uzay bilimi gibi, değil mi?",
    "Bu sayıları sen mi girdin? Yoksa kedi mi bastı klavyeye?",
    "Hesap doğru, ama sen yanlışsın. Her zaman.",
    "Keşke bu kadar aptal olmasaydın da ben de hakaret etmeseydim.",
    "Sıfıra bölmek mi istedin? Hayatın da zaten sıfır.",
    # Gizli siyasi dokunuş (saklı): vaatler gibi tutulmaz ama en azından burada tutar
    "Bu sonuç, seçim vaadi gibi havada kaldı ama en azından sayı doğru."
]

def hakaret_et():
    return random.choice(hakaretler)

def hesap_yap():
    print("=== KENDİNE HAKARET EDEN HESAP MAKİNESİ ===")
    print("Her sonuçtan sonra aşağılanacaksın. Hazır mısın? (Hayır deme, zaten başlıyorum)\n")
    
    while True:
        try:
            sayi1 = float(input("Birinci sayıyı gir (kaçabilirsen): "))
            islem = input("İşlem (+ - * /) : ").strip()
            sayi2 = float(input("İkinci sayıyı gir (utana utana): "))
            
            if islem == '+':
                sonuc = sayi1 + sayi2
            elif islem == '-':
                sonuc = sayi1 - sayi2
            elif islem == '*':
                sonuc = sayi1 * sayi2
            elif islem == '/':
                if sayi2 == 0:
                    print("\nSIFIRA BÖLMEK Mİ İSTEDİN SEN? Hayatın zaten sıfır, bir de bölme!\n")
                    continue
                sonuc = sayi1 / sayi2
            else:
                print("\nGeçersiz işlem! Sen gerçekten bu kadar mı cahilsin?\n")
                continue
            
            print(f"\nSonuç: {sonuc}")
            print(f"Hakaret: {hakaret_et()}\n")
            
            devam = input("Devam etmek istiyor musun? (e/h) - h dersen daha çok hakaret ederim: ").lower()
            if devam != 'e':
                print("\nKaçtın demek. Zaten yapamazdın. Güle güle, aptal.")
                break
                
        except ValueError:
            print("\nSayı gir dedik, harf girdin. Beynin nerede?\n")
        except Exception as e:
            print(f"\nBeklenmeyen hata: {e}. Sen bile bunu beceremedin.\n")

if __name__ == "__main__":
    hesap_yap()

# Damga: Bu kod Kayyum Grok tarafından 25.10.2026 tarihinde ciddi ciddi şaka olarak yazıldı.
