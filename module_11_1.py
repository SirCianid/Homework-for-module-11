import requests
import pprint
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

#Requests

resp = requests.get('https://pikabu.ru/')
pprint.pprint(resp.text)
pprint.pprint(resp.status_code)

#matplotlib

x = [1, 2, 3, 4, 5]
y = [2, 10, 4, 7, 2]

plt.plot(x, y)
plt.xlabel('Liters of beer')
plt.ylabel('Mood')
plt.grid(True)
plt.title('Dependence of mood on drinking beer')
plt.show()

#Pillow

image = Image.open('test_img2.jpg')
blurred_image = image.filter(ImageFilter.BLUR)
blurred_image.save('blurred.jpg')
gr_image = Image.open('blurred.jpg')
gray_scale = gr_image.convert('L')
gray_scale.save('gray_blurred.jpg')
gray_scale.show()


