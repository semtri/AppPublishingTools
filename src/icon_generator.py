# -*- coding: utf-8 -*-

import os
import sys
from PIL import Image

if __name__ == "__main__":   
    source = sys.argv[1]
    path = os.path.dirname(source)
    basename = os.path.basename(source)
    (base, ext) = os.path.splitext(source)
    
    print source, base, ext
    
    img = Image.open(source)
    sizes = [29, 32, 40, 48, 50, 57, 58, 60, 72, 76, 80, 87, 96, 100, 114, 120, 144, 152, 167, 180, 512]
    sizes.reverse()
    
    for size in sizes:
        print size
        img.resize((size, size), Image.ANTIALIAS).save(base + '_' + str(size) + '.png', quality=90)
