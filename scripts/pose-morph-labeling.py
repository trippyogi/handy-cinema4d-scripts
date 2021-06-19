import c4d
from c4d import gui
# Script to add a list of new poses to an object with a Pose Morph Tag
# Especially useful when creating facial pose morphs for ARKit


BLEND_SHAPE_LOCATION_LIST = ["eyeBlinkLeft", "eyeLookDownLeft", "eyeLookInLeft", "eyeLookOutLeft", "eyeLookUpLeft", "eyeSquintLeft", "eyeWideLeft", "eyeBlinkRight", "eyeLookDownRight", "eyeLookInRight", "eyeLookOutRight", "eyeLookUpRight", "eyeSquintRight", "eyeWideRight", "jawForward", "jawLeft", "jawRight", "jawOpen", "mouthClose", "mouthFunnel", "mouthPucker", "mouthLeft", "mouthRight", "mouthSmileLeft", "mouthSmileRight", "mouthFrownLeft", "mouthFrownRight", "mouthDimpleLeft", "mouthDimpleRight", "mouthStretchLeft", "mouthStretchRight", "mouthRollLower", "mouthRollUpper", "mouthShrugLower", "mouthShrugUpper", "mouthPressLeft", "mouthPressRight", "mouthLowerDownLeft", "mouthLowerDownRight", "mouthUpperUpLeft", "mouthUpperUpRight", "browDownLeft", "browDownRight", "browInnerUp", "browOuterUpLeft", "browOuterUpRight", "cheekPuff", "cheekSquintLeft", "cheekSquintRight", "noseSneerLeft", "noseSneerRight", "tongueOut"]

# Main function
def main():
    targetObject = doc.GetActiveObject()

    corr = targetObject.GetDownLast() 
    if not targetObject : print('error')
    
    morphTag = targetObject.GetTag(c4d.Tposemorph)
    
    for shape in BLEND_SHAPE_LOCATION_LIST:
        print(shape)
        morph = morphTag.AddMorph()
        if morph is None:
            return
    
        morph.SetName(shape)
    
    # select latest morph
    count = morphTag.GetMorphCount()
    morphTag.SetActiveMorphIndex(count-1)
    
    # set "Target"
    morphTag[c4d.ID_CA_POSE_TARGET] = targetObject
    
    c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()