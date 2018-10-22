import shapefile #nantinya modul shape file akan di import
w=shapefile.Writer() #mendeklarasikan variable
w.shapeType  #menjalankan perintah dari sih variable
w.field("kolom1","C") ##membuat kolom dengan tipe data karakter
w.field("kolom2","C")##membuat kolom dengan tipe data karakter
w.record("ngek","satu") #mengisi record pada kolom yang dibuat tadi
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]]) #membuat point atau titik atau garis
w.save("soal5") #untuk menyimpan dengan format file.shp
