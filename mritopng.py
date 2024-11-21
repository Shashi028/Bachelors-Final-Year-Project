import SimpleITK as sitk
from PIL import Image 
import numpy as np

# Specify the path to your .mha file
file_path = 'path/to/your/file.mha'

#Read the .mha file
image = sitk.ReadImage(file_path)

# Convert SimpleITK image to a NumPy array for further processing if needed
numpy_array = sitk.GetArrayFromImage(image)

#Convert NumPy array to PIL Image
pil_image = Image.fromarray(np.uint8(numpy_array))

#Save as PNG or JPEG
pil_image.save('output.png')