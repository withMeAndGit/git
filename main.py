import io
import sys

import requests
import pygame
from PIL import Image

from config import *
#

if not STATIC_API:
    print('!! set STATIC_API')
    sys.exit()

params = {
    'apikey': STATIC_API,
    'll': input('cords: ').replace(' ', ','),
    'z': (str(usr)
          if 1 <= (usr := int(input('size: '))) <= 21
          else '1')
}

response = requests.get(url=STATIC_URL, params=params)
image_data = io.BytesIO(response.content)

if not response:
    print(f'{response.status_code}, {response.reason}')
    sys.exit()

with Image.open(image_data, mode='r') as img:
    size = img.size
image_data.seek(0)
#

pygame.init()
screen = pygame.display.set_mode(size)

map_image = pygame.image.load(image_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(map_image, (0, 0))
    pygame.display.flip()

pygame.quit()