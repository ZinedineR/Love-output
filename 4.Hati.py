string = ""
bar = 1
x = 7

print ("Ini adalah Hati" + "\n")
atas_kiri = 0
while atas_kiri <= 3:
	string = string + " * "
	atas_kiri = atas_kiri + 1	
# Looping Spasi Atas
spasi = 0
while spasi <= 3:
	string = string + "   "
	spasi = spasi + 1
# Looping Kolom Bintang Sisi Kanan
atas_kanan = 0	
while atas_kanan <= 3:
	string = string + " * "
	atas_kanan = atas_kanan + 1
string = string + "\n\n"

# Looping Baris
while bar <= x:
	kol = bar
	# Looping Kolom Spasi Kosong
	while kol > 1:
		string = string + "   "
		kol = kol - 1
	# Looping Kolom Bintang Sisi Kiri	
	kiri = 1
	while kiri <= (x - bar):
		string = string + " * "
		kiri = kiri + 1	
	# Looping Kolom Bintang Sisi Kanan
	kanan = kiri	
	while kanan > 1:
		string = string + " * "
		kanan = kanan - 1

	string = string + "\n\n"
	bar = bar + 1
print (string)
