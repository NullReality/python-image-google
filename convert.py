import os
from PIL import Image

inputDir = os.getcwd() + '/images'
outputDir = '/opt/icons'

def convertAll():
    for filename in os.listdir(inputDir):
        
        if filename.startswith('.'):
            continue
        
        fileDir = os.path.join(inputDir, filename)
        
        with Image.open(fileDir) as im:
            im = im.rotate(270).resize((128, 128))
            if im.mode != 'RGB':
                im.convert('RGB')
            im.save((outputDir + filename), format='JPEG')
            