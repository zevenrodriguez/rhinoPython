#This code takes in a string of point coordinates. Each point coord should be seperated by a semicolon
import rhinoscript
import rhinoscriptsyntax as rs

pointsList = []

pointString = "0,0,0;1,1,0;2,2,0;3,3,0;4,4,0;5,5,0;6,6,0;7,7,0;8,8,0;9,9,0"

pointsList = pointString.split(';')

for i in range(len(pointsList)):
	if i < (len(pointsList)-1):
		#print pointsList[i]
		rs.AddLine(pointsList[i],pointsList[i+1])
