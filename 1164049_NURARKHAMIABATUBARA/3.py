import shapefile 				# Mengimport modul shape file
w=shapefile.Writer(shapeType=1) # Mendeklarasi variabel dengan shapetipenya adalah 1
w.shapeType 					# Menjalankan perintah pendeklarasian variabel
w.shapeType=3 					# Untuk menjalankan code diatasnya = 3
w.shapeType 					# Menjalankan perintah pendeklarasian variabel

w.field("kolom1","C") 			# Membuat kolom dengan tipe data character
w.field("kolom2","C") 			# Membuat kolom dengan tipe data character

w.record("ngek","satu") 		# Mengisi record ke kolom yang sudah di buat tadi dengan isi kolom 1 ngek dan kolom 2 satu
w.record("ngok","dua") 			# Mengisi record ke kolom yang sudah di buat tadi dengan isi kolom 2 ngek dan kolom 1 satu

w.point(1,1)     				# Membuat point/titik koordinat 2,2
w.point(2,2) 					# Membuat point/titik koordinat 2,2

w.save("soal3") 				# Untuk menyimpan nama file soal 3




