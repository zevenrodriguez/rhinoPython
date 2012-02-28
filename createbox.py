#import rhinoscript
#import rhinoscriptsyntax as rs

boxPointsList = []
boxList = []

box
boxes = 0

#layer = rs.StringBox("New layer name" )
#if layer: rs.AddLayer( layer )

#numberOfBoxes = rs.GetString("Number of boxes")
numberOfBoxes = 2
#print numberOfBoxes
#show grid
#

for boxes in range(numberOfBoxes):
	boxPattern = 0,0,0,0,2,0,2,2,0,2,0,0,0,0,2,0,2,2,2,2,2,2,0,2
	for i in boxPattern:
		boxTemp = i * boxes
		boxPointsList.append(boxTemp)
		#itterate throught box 
		#rs.AddBox(box)
	boxList.append(boxPointsList)
	boxList = []
del boxList[0]
print boxList
