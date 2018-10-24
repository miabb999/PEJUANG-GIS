import shapefile
w=shapefile.Writer() 
w.shapeType 

w.field("kolom1","C") 
w.field("kolom2","C") 


w.record("ngek","satu") 
w.record("crot","dua") 
w.record("crottt","duaa") 
 
 
w.poly(parts=[[[1,3],[5,3], [3,5],[1,3]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[-2,-2],[-6,-2], [-4,-4],[-2,-2]]],shapeType=shapefile.POLYLINE)

w.poly(parts=[[[-1,2],[-5,2], [-3,4],[-1,2]]],shapeType=shapefile.POLYLINE)
 
w.save("latihan10000")
