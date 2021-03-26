from urllib.request import urlretrieve
from PIL import Image


def iterate_until_last_frame(filename):
    im = Image.open(filename)
    i = 0
    try:
        while 1:
            im.seek(im.tell()+1)
            if i == 26:
                return im
            im.save("/tmp/frame"+str(i)+".png")
            i += 1
    except EOFError:
        pass


def get_last_frame(url):
    filename = 'result.png'

    _file = urlretrieve(url, 'file.gif')
    im = iterate_until_last_frame('file.gif')
    im.save(filename)
    return filename
