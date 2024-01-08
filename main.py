#menyambung string
namaPertama = "Danisyah"
namaTerakhir = "Rizky"

namaLengkap = namaPertama + " " + namaTerakhir
print(namaLengkap)

#menghitung panjang string
panjang = len(namaLengkap)
print(panjang)

#mengecek apakah ada string di string
d = "D"
status = d in namaLengkap
print(status)

d = "d"
status = d not in namaLengkap
print(status)

#mengulang string
print("wk"*10)
print(10*"wk")

#indexing [] dimulai dari 0
print(namaLengkap[0], "adalah indexing dari namaLengkap")
print(namaLengkap[0:8])
print(namaLengkap[9:14])
print(namaLengkap[0:8:2]) #lompatan 2 huruf

#item paling kecil dan besar
print(min(namaLengkap))
print(max(namaLengkap))

#ASCII Code
ascii_code = ord("d")
print(str(ascii_code))

data = 112
print(chr(data))


#operator dalam bentuk method
data = "danisyah"
jumlah = data.count("a")
print(str(jumlah))