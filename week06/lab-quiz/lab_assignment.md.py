branslar = ("Yazilim", "Tasarim", "Pazarlama")

tum_ogrenciler = []
tum_ogrenciler.append(["Kadir Demir".strip(), ["Yazilim", "Tasarim"]])
tum_ogrenciler.append(["Mehmethan Erduran".strip(), ["Pazarlama", "Yazilim"]])
tum_ogrenciler.append(["Davut Demir".strip(), ["Tasarim", "Pazarlama"]])

tum_ogrenciler.insert(0, ["Nejat Isler".strip(), ["Baskan"]])
print(tum_ogrenciler)

print(f"Toplam Kayitli Ogrenci Sayisi: {len(tum_ogrenciler)}")

tum_ogrenciler.remove(["Davut Demir".strip(), ["Tasarim", "Pazarlama"]])

son_ogrenci = tum_ogrenciler.pop()
print(f"Sistemden en son cikan ogrenci: {son_ogrenci[0]}")

tum_ogrenciler.append(["Burak Tan".strip(), ["Tasarim"]])
print(tum_ogrenciler)

sorted_ogrenciler = sorted(tum_ogrenciler)
print(f"Alfabetik Sirali Ogrenci Listesi: {sorted_ogrenciler}")
print(f"Orijinal Ogrenci Listesi: {tum_ogrenciler}")

tum_ogrenciler.sort()
print(f"Kalici Olarak Alfabetik Sirali Ogrenci Listesi: {tum_ogrenciler}")
