import os
from PIL import Image

directory = os.environ['FACEPROJECTDIR'] 
directory += '/faces'

for file in os.listdir(directory):
  pass
  print(file)
  if file.endswith(".jpeg"):
    im = Image.open(os.path.join(directory, file))

    x, y = im.size

    if x < 80 or y < 80:
      os.remove(os.path.join(directory, file))
      continue
    
