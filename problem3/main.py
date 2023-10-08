# tulis solusi code disini
class Kalkulator:
    def __init__(self, angka1, angka2):
        self.angka1 = angka1
        self.angka2 = angka2

    def penjumlahan(self):
        hasil = self.angka1 + self.angka2
        return hasil

    def pengurangan(self):
        hasil = self.angka1 - self.angka2
        return hasil

    def perkalian(self):
        hasil = self.angka1 * self.angka2
        return hasil

    def pembagian(self):
        if self.angka2 == 0:
            return "Pembagian dengan nol tidak valid."
        hasil = self.angka1 / self.angka2
        return hasil

def main():
    kalkulator1 = Kalkulator(3, 4)
    kalkulator2 = Kalkulator(15, 4)
    kalkulator3 = Kalkulator(10, 10)
    kalkulator4 = Kalkulator(12, 3)

    print("Penjumlahan:", kalkulator1.penjumlahan())
    print("Pengurangan:", kalkulator2.pengurangan())
    print("Perkalian:", kalkulator3.perkalian())
    print("Pembagian:", kalkulator4.pembagian())

if __name__ == "__main__":
    main()
