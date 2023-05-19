import base64
from io import BytesIO

def converter_img_cover(image_path):
  with open(image_path, 'rb') as image_file:
    image_data = image_file.read()
    image_bytes = BytesIO(image_data)

  image_base64 = base64.b64encode(image_bytes.getvalue()).decode('utf-8')

  return image_base64