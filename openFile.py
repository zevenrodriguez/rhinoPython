import rhinoscriptsyntax as rs

file = open("test.txt")

inFile = file.readlines()
file.close()

print inFile
