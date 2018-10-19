import shapefile         # Mengimport modul shape file
w=shapefile.Writer() 	   # Mendeklarasi variabel
w.shapeType 			       # Menjalankan perintah dari pendeklarasian variabel

w.field("kolom1","C")    # Membuat kolom dengan tipe data character
w.field("kolom2","C")    # Membuat kolom dengan tipe data character

w.record("ngek","satu")  # Mengisi record ke kolom yang sudah di buat tadi
w.record("ngok","dua")   # Mengisi record ke kolom yang sudah di buat tadi

w.point(1,1) 			       # Membuat point/titik 
w.point(2,2) 		         # Membuat point/titik 

w.save("soal1") 		     # Untuk save menjadi shp file
