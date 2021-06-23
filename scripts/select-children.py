import c4d
from c4d import gui
#Welcome to the world of Python

def selchildren(obj,next): # Scan obj hierarchy and select children
    while obj and obj != next:
        doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL,obj)
        obj.SetBit(c4d.BIT_ACTIVE)
        selchildren(obj.GetDown(),next)
        obj = obj.GetNext()
    return True

def main():
    try: obj = doc.GetActiveObjects(False)[0]
    except: return True # Nothing Selected
    
    doc.StartUndo()
    for obj in doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN):
        if selchildren(obj, obj.GetNext()):
            obj.DelBit(c4d.BIT_ACTIVE)
    doc.EndUndo()
    c4d.EventAdd()

if __name__=='__main__':
    main()
