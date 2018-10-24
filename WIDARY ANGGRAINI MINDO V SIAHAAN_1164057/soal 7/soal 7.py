import shapefile #nantinya modul shape file akan di import
w=shapefile.Writer() #mendeklarasikan variable
w.shapeType #menjalankan perintah dari sih variable
w.field("kolom1","C")##membuat kolom dengan tipe data karakter
w.field("kolom2","C")##membuat kolom dengan tipe data karakter
w.record("ngek","satu")#mengisi record pada kolom yang dibuat tadi
w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE)#membuat point atau titik atau garis
w.save("soal7") #untuk menyimpan dengan format file.shp
