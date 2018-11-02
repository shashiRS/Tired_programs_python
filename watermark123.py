from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys
import urllib, cStringIO
import csv
import pdb
FONT = 'DejaVuSansMono.ttf'
def add_watermark(ur,index):
    try:

        file_url = cStringIO.StringIO(urllib.urlopen(ur).read())
        text="Bricks.in"

        out_file='WATERMARKTEST'+str(index)+'.jpg'
        angle=23
        opacity=0.25
        pdb.set_trace()
        img = Image.open(file_url).convert('RGB')
        watermark = Image.new('RGBA', img.size, (0,0,0,0))
        size = 2
        n_font = ImageFont.truetype(FONT, size)
        n_width, n_height = n_font.getsize(text)
        while n_width+n_height < watermark.size[0]:
            size += 2
            n_font = ImageFont.truetype(FONT, size)
            n_width, n_height = n_font.getsize(text)
        draw = ImageDraw.Draw(watermark, 'RGBA')
        draw.text(((watermark.size[0] - n_width) / 2,
                  (watermark.size[1] - n_height) / 2),
                  text, font=n_font)
        watermark = watermark.rotate(angle,Image.BICUBIC)
        alpha = watermark.split()[3]
        alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
        watermark.putalpha(alpha)
        Image.composite(watermark, img, watermark).save(out_file, 'JPEG')
        pdb.set_trace()

        print("Finished")
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print ur
        print "Failed"
if __name__ == '__main__':
    ul=[]
    with open('names.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            for r in row:
                ul.append(r)

    COUNT=0

    for i in ul:
        COUNT=COUNT+1
        add_watermark(i,COUNT)

