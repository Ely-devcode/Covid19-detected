import os

print ('+-----------------------------------------+')
print ('|\\Selamat Datang di Aplikasi Sistem Pakar\\|')
print ('|\\     Deteksi Dini Risiko Covid19       \\|')
print ('+-----------------------------------------+')

nama = input("Nama\t:")
pilihan = input("Hallo "+nama+ ",\n Apakah anda ingin melakukan diagnosa ? (y/n)")

os.system("cls")

while pilihan == "y":
	print("\n Apakah merasakan gejala berikut?")
	print("1. Demam/Suhu Badan Tinggi")
	print("2. Batuk atau Pilek")
	print("3. Kesulitan Bernafas atau Sesak nafas")
	print("4. Nyeri Tenggorokan")
	msg1 = input("Jawab (y/n) : ")

	if msg1 == "y" :
		print('\n Apakah anda mempunyai riwayat berikut ini ? :')
		print('1. Memiliki riwayat kontak erat dengan penderita terkonfirmasi COVID-19 atau probabel COVID-19')
		print('2. Memiliki riwayat perjalanan atau tinggal diluar negeri yang melakukan penularan lokal')
		print('3. Memiliki riwayat perjalanan atau tinggal diarea penularan lokal di Indonesia')
		msg2 = input('Jawab (y/n) :')

		if msg2 == "y" :
			print('\n Hi, '+nama+' hasil awal diagnosa kamu adalah : ')
			print('Gejala awal covid19 mohon untuk segera ke dokter untuk pemeriksaan lebih lanjut')
		elif msg2 == "n" :
			print('\n Apakah anda juga merasakan gejala berikut ini ? :')
			print('1. Menggigil sedang sampai berat')
			print('2. Tubuh Kelelahan dan Lemas\n3. Lama penyakit kurang dari 14 hari')
			msg3 = input('Jawab (y/n) : ')

			if msg3 == "y":
				print('\n Hi, '+nama+' hasil awal diagnosa kamu adalah : ')
				print('Gejala flu dan lemahnya sistem imun tubuh minum obat flu dan vitamin C atau vitamin penambah sistem imun lainnya')
			elif msg3 == "n" :
				print('\n Hi, ' +nama+' anda sepertinya sedang banyak pikiran! mohon tenangkan pikiran anda dan perbanyak olahraga')
			else:
				print('\n Hi, ' +nama+ ' anda sepertinya tidak mau berobat')
		else:
			print('\n Hi, ' +nama+ ' anda sepertinya butuh jalan-jalan')
	elif msg1 == "n" :
		print('\n Hi, ' +nama+ ' anda sepertinya tidak mau berobat')
	else:
		print('\n Hi, ' +nama+ ' anda sepertinya butuh jalan-jalan')

	print ('+-----------------------------------------+')
	pilihan = input("Hallo " +nama+ ", \nApakah anda ingin melakukan diagnosa ? (y/n)")

	if pilihan == "y":
		os.system("clear")
		print ('+-----------------------------------------+')
		print ('|\\Selamat Datang di Aplikasi Sistem Pakar\\|')
		print ('|\\     Deteksi Dini Risiko Covid19       \\|')
		print ('+-----------------------------------------+')
	else:
		print()
		print ('+------------Terima Kasih-----------------+')
		print ('+-----------------------------------------+')
