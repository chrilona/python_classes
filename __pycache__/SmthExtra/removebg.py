import urllib.request
from rembg import remove 
from PIL import Image
input_path = "bakery.jpg"
out_path = remove(input_path)
input = Image.open(input_path)
output = remove(input)
output.save(out_path)