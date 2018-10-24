import shapefile   #nantinya modul shape file akan di import
w=shapefile.Writer()    #mendeklarasikan variable
w.shapeType      #menjalankan perintah dari sih variable      
w.field("Nama Bidang","Bidang Ke")##membuat kolom dengan tipe data karakter
w.field("Nama Bidang","Bidang Ke") ##membuat kolom dengan tipe data karakter

w.record("Segitiga Sama sisi-sisi","satu")#mengisi record pada kolom yang dibuat tadi
w.record("Segitiga Sama sisi-sisi","dua")#mengisi record pada kolom yang dibuat tadi
w.record("Segitiga Sama sisi-sisi","tiga")#mengisi record pada kolom yang dibuat tadi
w.record("Segitiga Sama sisi-sisi","empat")#mengisi record pada kolom yang dibuat tadi
w.record("Segitiga Sama sisi-sisi","lima") #mengisi record pada kolom yang dibuat tadi
w.poly(parts=[[[-3,6],[-6,1],[-1,1],[-3,6]]],shapeType=shapefile.POLYGON) #membuat point atau titik atau garis
w.poly(parts=[[[3,6],[1,1], [6,1],[3,6]]],shapeType=shapefile.POLYGON) #membuat point atau titik atau garis
w.poly(parts=[[[3,-1],[1,-6],[6,-6],[3,-1]]],shapeType=shapefile.POLYGON) #membuat point atau titik atau garis
w.poly(parts=[[[-3,-1],[-1,-6],[-6,-6],[-3,-1]]],shapeType=shapefile.POLYGON) #membuat point atau titik atau garis
w.poly(parts=[[[-3,-8],[-6,-12],[-1,-12],[-3,-8]]],shapeType=shapefile.POLYGON) #membuat point atau titik atau garis
w.save("soal 10") #untuk menyimpan dengan format file.shp