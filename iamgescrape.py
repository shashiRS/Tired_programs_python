import argparse
import json
import itertools
import logging
import re
import os
import uuid
import sys
from urllib2 import urlopen,Request
import csv
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageEnhance
import os, sys
import urllib, cStringIO
import csv
import pdb
FONT = 'DejaVuSansMono.ttf'

def configure_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(
        logging.Formatter('[%(asctime)s %(levelname)s %(module)s]: %(message)s'))
    logger.addHandler(handler)
    return logger

logger = configure_logging()
iurl=[]
REQUEST_HEADER = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}


def get_soup(url, header):
    response = urlopen(Request(url, headers=header))
    return BeautifulSoup(response, 'html.parser')

def get_query_url(query):
    return "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query

def extract_images_from_soup(soup):
    image_elements = soup.find_all("div", {"class": "rg_meta"})
    metadata_dicts = (json.loads(e.text) for e in image_elements)
    link_type_records = ((d["ou"], d["ity"]) for d in metadata_dicts)
    return link_type_records

def extract_images(query, num_images):
    url = get_query_url(query)
    logger.info("Souping")
    soup = get_soup(url, REQUEST_HEADER)
    logger.info("Extracting image urls")
    link_type_records = extract_images_from_soup(soup)
    return itertools.islice(link_type_records, num_images)

def get_raw_image(url):
    req = Request(url, headers=REQUEST_HEADER)
    resp = urlopen(req)
    return resp.read()

def save_image(raw_image, image_type, save_directory):
    extension = image_type if image_type else 'jpg'
    file_name = uuid.uuid4().hex
    save_path = os.path.join(save_directory, file_name)
    with open(save_path, 'wb') as image_file:
        image_file.write(raw_image)

def download_images_to_dir(images, save_directory, num_images):
    for i, (url, image_type) in enumerate(images):
        try:
            iurl.append(url)
            logger.info("Making request (%d/%d): %s", i, num_images, url)
            raw_image = get_raw_image(url)
            save_image(raw_image, image_type, save_directory)
            
        except Exception as e:
            logger.exception(e)

def run(query, save_directory, num_images=100):
    query = '+'.join(query.split())
    logger.info("Extracting image links")
    images = extract_images(query, num_images)
    logger.info("Downloading images")
    download_images_to_dir(images, save_directory, num_images)
    logger.info("Finished")
    with open('names1.csv', 'w') as csvfile:
        fieldnames = ['imageurls']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for ulrs in iurl:
            writer.writerow({'imageurls':ulrs})

def main():
    ull=[]
    with open('banglorefull.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            print row
            for r in row:
                ul.append(r)
    pdb.set_trace()
    keywords=raw_input("Enter Keyword:")
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default=keywords, type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=100, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default='/home/halk/Downloads/gg', type=str, help='save directory')
    args = parser.parse_args()
    run(args.search, args.directory, args.num_images)
    

def add_watermark(ur,index):
    try:
        file_url = cStringIO.StringIO(urllib.urlopen(ur).read())
        
        text="Bricks.in"
        out_file='WATERMARK'+str(index)+'.jpg'
        angle=23     
        opacity=0.25
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
        print("Water_Mark Bricks.in Apllied")
    except:
        pass
         
if __name__ == '__main__':
    main()
    ul=[]
    with open('names1.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            for r in row:
                ul.append(r)

    COUNT=0

    for i in ul:
        COUNT=COUNT+1
        add_watermark(i,COUNT)
