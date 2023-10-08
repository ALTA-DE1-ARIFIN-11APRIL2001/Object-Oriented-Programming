# # tulis solusi code disini
import math
class PengirimanBarang:
    def __init__(self, panjang, lebar, tinggi, berat):
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi
        self.berat = berat

    def hitung_harga(self):
        volume = self.panjang * self.lebar * self.tinggi

        berat_pembulatan = math.ceil(self.berat)

        if volume < 50 or berat_pembulatan < 1:
            harga = 5000
        else:
            harga = max(volume, berat_pembulatan * 1000) * 5000 // 1000

        return harga

panjang = float(input("Panjang (cm): "))
lebar = float(input("Lebar (cm): "))
tinggi = float(input("Tinggi (cm): "))
berat = float(input("Berat (kg): "))

pengiriman = PengirimanBarang(panjang, lebar, tinggi, berat)

harga = pengiriman.hitung_harga()

print("Harga: Rp", harga)
