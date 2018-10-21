import shapefile 								# Mengimport modul shape file
w=shapefile.Writer() 							# Mendeklarasi variabel
w.shapeType 									# Menjalankan perintah dari pendeklarasian variabe

w.field("kolom1","C") 							# Membuat kolom dengan tipe data character
w.field("kolom2","C") 							# Membuat kolom dengan tipe data character

w.record("ngek","satu")  						# Mengisi record ke kolom yang sudah di buat tadi
 
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) # Membuat polyline

w.save("soal5")									# Untuk save menjadi shp file



 





