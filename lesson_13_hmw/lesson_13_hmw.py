mehsullar={
    "laptop": 1800,
    "telefon": 1200,
    "monitor": 500,
    "mouse": 50
}


try:
    mehsul = input("Mehsul: ")
    miqdar = int(input("Miqdar: "))
    if miqdar <= 0:
        raise Exception("Miqdar 0-dan boyuk olmalidir")
    umumi_qiymet = mehsullar[mehsul] * miqdar
    
except KeyError:
    print("Bele bir mehsul movcud deyil")
except ValueError:
    print("Miqdar reqem olmalidir")
    
    
else:
    print("Sifaris ugurla yaradildi\n")
    print("\n")
    print("Mehsul:", mehsul)
    print("Miqdar:", miqdar)
    print("Umumi qiymet:", umumi_qiymet)
    
    with open("orders.txt","a", encoding="utf-8") as f:
        f.write(f"{mehsul},{miqdar},{umumi_qiymet}\n")
try:
    with open("orders.txt","r", encoding="utf-8") as file:
        print("---------Sifariş tarixçəsi----------\n")
        text = file.read()
        print(text)
except FileNotFoundError:
    print("Hələ heç bir sifariş tarixçəsi yoxdur")
        
finally:
    print("Sifariş əməliyyatı tamamlandı" )
