class Telebe:
    tehsil_merkezi = "High Code"
    def __init__(self, ad, kurs, bal):
        self.ad = ad
        self.kurs = kurs
        self.bal = bal
        if bal < 0:
            raise ValueError("Bal 0 ile 100 arasinda olmalidir")
    def melumat_goster(self):
        print(f"Ad: {self.ad}")
        print(f"Kurs: {self.kurs}")
        print(f"Bal: {self.bal}")
    def bal_artir(self, miqdar):
        if miqdar <= 0:
            return False
        self.bal += miqdar
        if self.bal > 100:
            return False
        else:
            return True  
    def ugurludur(self):
        return self.bal >= 51
telebe1 = Telebe("Ayxan", "Python Backend", 45)
telebe2 = Telebe("Tural", "Python Backend", 90)
telebe1.melumat_goster()


print(telebe1.ugurludur())

print(telebe1.bal_artir(10))

print(telebe1.ugurludur())

print(telebe2.bal_artir(20))
print(telebe2.bal)

print(Telebe.tehsil_merkezi)

try:
    telebe = Telebe("Test", "Python Backend", -10)
except ValueError as xeta:
    print(f"Xeta: {xeta}")

