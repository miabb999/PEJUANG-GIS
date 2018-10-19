import shapefile        #nantinya modul shape file akan di import
w=shapefile.Writer() #mendeklarasikan variable
w.shapeType             #menjalankan perintah dari sih variable
w.field("kolom1","C")   #membuat kolom dengan tipe data karakter
w.field("kolom2","C")   #membuat kolom dengan tipe data karakter
w.record("ngek","satu") #mengisi record pada kolom yang dibuat tadi
w.record("ngok","dua")  #mengisi record pada kolom yang dibuat tadi
w.point(1,1)    #membuat point atau titik
w.point(2,2)    #membuat point atau titik
w.save("soal1") #untuk menyimpan dengan format file.shp