# tulis solusi code disiniclass BangunDatar:
class BangunDatar:
    def __init__(self):
        self.volume = 0

    def hitung_volume(self):
        pass

class Kubus(BangunDatar):
    def __init__(self, sisi):
        super().__init__()
        self.sisi = sisi

    def hitung_volume(self):
        self.volume = self.sisi ** 3
        return self.volume

class Balok(BangunDatar):
    def __init__(self, panjang, lebar, tinggi):
        super().__init__()
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def hitung_volume(self):
        self.volume = self.panjang * self.lebar * self.tinggi
        return self.volume

class Tabung(BangunDatar):
    def __init__(self, jari_jari, tinggi):
        super().__init__()
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def hitung_volume(self):
        self.volume = (22/7) * (self.jari_jari ** 2) * self.tinggi
        return self.volume

def main():
    kubus = Kubus(10)
    balok = Balok(3, 6, 10)
    tabung = Tabung(7, 10)

    print("Volume")
    print(f"Kubus : {kubus.hitung_volume()}")
    print(f"Balok : {balok.hitung_volume()}")
    print(f"Tabung : {tabung.hitung_volume()}")

if __name__ == "__main__":
    main()
