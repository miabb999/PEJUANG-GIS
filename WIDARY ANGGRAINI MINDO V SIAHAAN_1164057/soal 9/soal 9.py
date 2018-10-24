import shapefile #nantinya modul shape file akan di import
w=shapefile.Writer() #mendeklarasikan variable
w.shapeType #menjalankan perintah dari sih variable
w.field("kolom1","C")##membuat kolom dengan tipe data karakter
w.field("kolom2","C")##membuat kolom dengan tipe data karakter
w.record("ngek","satu") #mengisi record pada kolom yang dibuat tadi
w.record("crot","dua") #mengisi record pada kolom yang dibuat tadi
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2],
[1,3]]],shapeType=shapefile.POLYLINE)#membuat point atau titik atau garis
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9],
[1,6]]],shapeType=shapefile.POLYLINE)#membuat point atau titik atau garis
w.save("soal9") #untuk menyimpan dengan format file.shp