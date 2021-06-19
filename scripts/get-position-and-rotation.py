import c4d
import math
from c4d import gui
# Script to iterate through a tree of objects, and print out their Transform components
# Used to generate the list of Transforms for Decentraland objects, created by a Cloner in Cinema 4D

# Main function
def main():
    obj = doc.GetFirstObject().GetDown()
    name = 'stageLightingTransform'
    count = 0
    while obj:
        x = -obj.GetMg().off.x
        y = obj.GetMg().off.y
        z = -obj.GetMg().off.z
        h = math.degrees(obj.GetAbsRot().y)
        p = math.degrees(obj.GetAbsRot().z)
        b = math.degrees(obj.GetAbsRot().x)
        print('''const {}{} = new Transform({{\n    position: new Vector3({}, {}, {}),\n    scale: Vector3.One(),\n    rotation: Quaternion.Euler({}, {}, {})\n}})'''.format(name, count, x, y, z, h, p, b))
        obj = obj.GetNext()
        count += 1

    obj = doc.GetFirstObject().GetDown()
    count = 0
    while obj:
        print('{}{},'.format(name, count))
        obj = obj.GetNext()
        count +=1

# Execute main()
if __name__=='__main__':
    main()