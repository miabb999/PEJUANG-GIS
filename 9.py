import shapefile 		# Mengimport modul shape file
w=shapefile.Writer() 	# Mendeklarasi variabel
w.shapeType 			# Menjalankan perintah dari pendeklarasian variabel

w.field("kolom1","C") 	# Membuat kolom dengan tipe data character
w.field("kolom2","C") 	# Membuat kolom dengan tipe data character

w.record("ngek","satu") # Mengisi record ke kolom yang sudah di buat tadi
w.record("crot","dua")  # Mengisi record ke kolom yang sudah di buat tadi
 
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2], [1,3]]],shapeType=shapefile.POLYLINE)  # Membuat polyline
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9], [1,6]]],shapeType=shapefile.POLYLINE)  # Membuat polyline
  
w.save("soal9")			# Untuk save menjadi shp file














 





