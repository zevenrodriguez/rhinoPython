import rhinoscript
import rhinoscriptsyntax as rs

#http://www.rhino3d.com/5/ironpython/index.html


point0 = [0,0,0]
point1 = [2,2,2]
point2 = [5,5,5]

pointsList = []

pointString = "0,0,0;1,1,1;2,2,2;"

for i in pointString:
	
	pointsList.append(i)
	


#pointsList = [point0,point1,point2]


rs.AddLine(pointTest,point2)
