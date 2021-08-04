import c4d
from c4d import gui
# Script to zero out points on the x-axis
# Useful for centering the seam when retopologizing

def main():
    obj = doc.GetActiveObject()
    points = obj.GetPointS()
    point_count = obj.GetPointCount()
    point_list = points.GetAll(point_count)
    
    for i in range(point_count):
        if point_list[i]:
            point_position = obj.GetPoint(i)
            point_position.x = 0
            obj.SetPoint(i, point_position)
            c4d.EventAdd()

if __name__=='__main__':
    main()