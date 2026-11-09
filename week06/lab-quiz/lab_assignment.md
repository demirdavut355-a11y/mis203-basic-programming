branşlar = ("Yazılım", "Tasarım", "Pazarlama")
öğrenciler = [
    ["Kadir Demir".strip(), ["Yazılım", "Tasarım"]],
    ["Mehmethan Erduran".strip(), ["Pazarlama", "Yazılım"]],
    ["Davut Demir".strip(), ["Tasarım", "Pazarlama"]]

]
öğrenciler.insert(0, ["Nejat İşler".strip(), ["Başkan"]])
print(öğrenciler)
"Toplam Kayıtlı Öğrenci Sayısı: X"
print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(öğrenciler)}")
öğrenciler.remove(["Mehmethan Erduran".strip(), ["Pazarlama", "Yazılım"]])
son_ogrenci = öğrenciler.pop()
print(f"Sistemden en son çıkan öğrenci: {son_ogrenci[0]}")

öğrenciler.append(["Burak Tan".strip(), ["Tasarım"]])
print(öğrenciler)

sorted_öğrenciler = sorted(öğrenciler)
print(f"Alfabetik Sıralı Öğrenci Listesi: {sorted_öğrenciler}")
print(f"Orijinal Öğrenci Listesi: {öğrenciler}")

öğrenciler.sort()
print(f"Kalıcı Olarak Alfabetik Sıralı Öğrenci Listesi: {öğrenciler}")
