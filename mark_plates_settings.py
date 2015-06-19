from peewee import *
from os import listdir
from os import remove
from os.path import isfile, join
from PIL import Image as ImgLib


data_dir = "Train/"
xml_file_path = "/home/naz/Desktop/rects/"
mypath = xml_file_path + data_dir

xml_file = "training.xml"

img_ext = ".jpg"

stroke = 2




# Database settings
db = SqliteDatabase('mydb.db', threadlocals=True)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db

class Image(BaseModel):
    path = TextField()
    file = TextField(unique=True)
    width = IntegerField()
    height = IntegerField()
    x0 = IntegerField()
    y0 = IntegerField()
    x1 = IntegerField()
    y1 = IntegerField()
    x2 = IntegerField()
    y2 = IntegerField()
    x3 = IntegerField()
    y3 = IntegerField()


# todo tip "not"
if not Image.table_exists():
    db.create_tables([Image])


onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]



# Populate table with all images in folder using initial values
for file in onlyfiles:
    exists = Image.select().where(Image.file == file).exists()

    if not exists:
        size = ImgLib.open(mypath + file).size
        x0 = y0 = x1 = y1 = x2 = y2 = x3 = y3 = -1
        width = size[0]
        height = size[1]
        Image.create(path=mypath, file=file, width = width, height = height, x0=x0, y0=y0, x1=x1, y1=y1, x2=x2, y2=y2, x3=x3 ,y3=y3)





