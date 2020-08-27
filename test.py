# this script is used to test resize.py with any image
# it must be run inside the resize/ directory

import resize
import PIL.Image

# ydb
# url = 'https://i.scdn.co/image/ab67616d00004851988ede5e1276e758b5f9e577'

# graduation
# url = 'resize/test.png'

# xxx album
# url = 'https://i.scdn.co/image/ab67616d00004851806c160566580d6335d1f16c'

# #mbdtf
# url = 'https://i.scdn.co/image/ab67616d00004851d9194aa18fa4c9362b47464f'

grad = 'test.png'

paused = '../assets/paused.png'

img = PIL.Image.open(grad)
resize.resize(img)