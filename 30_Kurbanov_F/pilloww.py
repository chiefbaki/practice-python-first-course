import requests
from PIL.Image import Image

# image = requests.get('http://openweathermap.org/img/wn/10d@2x.png', stream=True)
# with open('weather_icons/10d.png', 'wb') as f:
#     f.write(image.content)

img = Image.new('RGB', (100,50))
img_01d = Image.open('weather_icons/01d.png')
img_01
