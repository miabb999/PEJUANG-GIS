import shapefile   	   	# Mengimport modul shape file
w=shapefile.Writer()    # Mendeklarasi variabel
w.shapeType             # Menjalankan perintah dari pendeklarasian variabel

w.field("Nama Bidang","Blackpink")		# Membuat kolom dengan tipe data character
w.field("Nama Bidang","Blackpink")  	# Membuat kolom dengan tipe data character

w.record("Segitiga Sama sisi","lisa")	  # Mengisi record ke kolom yang sudah di buat tadi
w.record("Segitiga Sama sisi","jisoo")	 # Mengisi record ke kolom yang sudah di buat tadi
w.record("Segitiga Sama sisi","jennie")	# Mengisi record ke kolom yang sudah di buat tadi
w.record("Segitiga Sama sisi","rose")  	# Mengisi record ke kolom yang sudah di buat tadi

w.poly(parts=[[[1,1],[5,1],[3,4],[1,1]]],shapeType=shapefile.POLYGON)	        # Membuat polygon
w.poly(parts=[[[1,-1],[5,-1], [3,-4],[1,-1]]],shapeType=shapefile.POLYGON)	   # Membuat polygon
w.poly(parts=[[[-6,-1],[-2,-1],[-4,-4],[-6,-1]]],shapeType=shapefile.POLYGON)	# Membuat polygon
w.poly(parts=[[[-6,1],[-2,1],[-4,4],[-6,1]]],shapeType=shapefile.POLYGON)	    # Membuat polygon

w.save("soal 10")	# Untuk save menjadi shp file















 





