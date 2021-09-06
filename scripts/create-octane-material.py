import c4d
from c4d import gui
import os
# Script to generate Octane Universal materials based on PBR textures in a specified folder

ID_OCTANE_IMAGE_TEXTURE = 1029508
TEXTURE_TYPES = ["BaseColor", "Height", "Metallic", "Normal", "Roughness"]
TEXTURE_IDS = [c4d.OCT_MATERIAL_DIFFUSE_LINK, c4d.OCT_MATERIAL_BUMP_LINK, c4d.OCT_MAT_SPECULAR_MAP_LINK, c4d.OCT_MATERIAL_NORMAL_LINK, c4d.OCT_MATERIAL_ROUGHNESS_LINK]
PATH = "C:/Filepath/"

# Returns material names based on folder containing PBR textures
def getMaterialNames():
    fileNames = os.listdir(PATH)
    materialNames = []
    for name in fileNames:
        nameList = name.split('_')
        materialNames.append(nameList[0])
    return list(dict.fromkeys(materialNames))

# Main function
def main():
    doc = c4d.documents.GetActiveDocument()
    materialNames = getMaterialNames()
    
    for name in materialNames:
        c4d.CallCommand(1041569) # Create Octane Universal Material
        material = doc.GetActiveMaterial()
        
        for texType, texId in zip(TEXTURE_TYPES, TEXTURE_IDS):
            doc.StartUndo()
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, material)
            
            shader = c4d.BaseShader(ID_OCTANE_IMAGE_TEXTURE)
            material.InsertShader(shader)
            material[texId] = shader
            material[c4d.ID_BASELIST_NAME] = name
            filename = name + "_" + texType + ".png"
            shader[c4d.IMAGETEXTURE_FILE] = os.path.join(PATH, filename)
            shader[c4d.IMAGETEXTURE_MODE] = 0
            shader[c4d.IMAGETEXTURE_GAMMA] = 2.2
            shader[c4d.IMAGETEX_BORDER_MODE] = 0
            doc.InsertMaterial(material)
               
            doc.EndUndo()
            c4d.EventAdd()

# Execute main()
if __name__=='__main__':
    main()
    
    


