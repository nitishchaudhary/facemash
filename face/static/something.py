import random
import os
path ="c:/Users/Nitish/Desktop/Projects/Facemash/face/static"
files = os.listdir(path)
d =random.choice(files)
print(d)