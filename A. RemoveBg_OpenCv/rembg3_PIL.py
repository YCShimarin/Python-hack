from rembg import remove
from PIL import Image

input_path = './src/Kevin.jpg'
output_path = 'output3.png'

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
