import rhinoscript
import rhinoscriptsyntax as rs

box = rs.GetBox()

if box: rs.AddBox(box)