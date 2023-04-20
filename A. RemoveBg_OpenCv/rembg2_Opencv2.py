from rembg import remove
import cv2

input_path = './src/Kevin.jpg'
output_path = 'output2.png'

input = cv2.imread(input_path)
output = remove(input)
cv2.imwrite(output_path, output)
