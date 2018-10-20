import shapefile 					# Mengimport modul shape file
w=shapefile.Writer(shapeType=1) 	# Mendeklarasi variabel dengan shapetipenya adalah 1
w.shapeType							# Menjalankan perintah dari pendeklarasian variabel 

w.field("kolom1","C") 				# Membuat kolom dengan tipe data character
w.field("kolom2","C") 				# Membuat kolom dengan tipe data character

w.record("ngek","satu") 			# Mengisi record ke kolom yang sudah di buat tadi
w.record("ngok","dua") 				# Mengisi record ke kolom yang sudah di buat tadi

w.point(1,1) 						# Membuat point/titik koordinat 1,1
w.point(2,2) 						# Membuat point/titik koordinat 2,2

w.save("soal2") 					# Untuk save menjadi shp file



