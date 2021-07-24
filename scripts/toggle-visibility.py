import c4d
from c4d import gui
# Script to toggle visibility of selected object

# Main function
def main():
    obj = doc.GetActiveObject()
    
    if obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] == 1:
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 2
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 2
    else:
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1

    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()