# Copyright (C) 2013 Wesley Baugh
"""Detect watermark in images.
### Requires
- [Pillow](https://pypi.python.org/pypi/Pillow/2.0.0)
"""
import glob
import scipy
from classify import MultinomialNB
from PIL import Image
import pdb

TRAINING_POSITIVE = 'training-positive/*.jpg'
TRAINING_NEGATIVE = 'training-negative/*.jpg'
TEST_POSITIVE = 'test-positive/*.jpg'
TEST_NEGATIVE = 'test-negative/*.jpg'

# How many pixels to grab from the top-right of image.
CROP_WIDTH, CROP_HEIGHT = 100, 100
RESIZED = (16, 16)


def get_image_data(infile):
    image = Image.open(infile)
    width, height = image.size
    # left upper right lower
    box = width - CROP_WIDTH, 0, width, CROP_HEIGHT
    region = image.crop(box)
    resized = region.resize(RESIZED)
    data = resized.getdata()
    # Convert RGB to simple averaged value.
    data = [sum(pixel) / 3 for pixel in data]
    # Combine location and value.
    values = []
    for location, value in enumerate(data):
        values.extend([location] * value)
    return values


def main():
    watermark = MultinomialNB()
    # Training
    count = 0
    for infile in glob.glob(TRAINING_POSITIVE):
        data = get_image_data(infile)
        watermark.train((data, 'positive'))
        count += 1
        pdb.set_trace()
        print 'Training', count
    for infile in glob.glob(TRAINING_NEGATIVE):
        data = get_image_data(infile)
        watermark.train((data, 'negative'))
        count += 1
        print 'Training', count
    # Testing
    correct, total = 0, 0
    for infile in glob.glob(TEST_POSITIVE):
        data = get_image_data(infile)
        prediction = watermark.classify(data)
        if prediction.label == 'positive':
            correct += 1
        total += 1
        print 'Testing ({0} / {1})'.format(correct, total)
    for infile in glob.glob(TEST_NEGATIVE):
        data = get_image_data(infile)
        prediction = watermark.classify(data)
        if prediction.label == 'negative':
            correct += 1
        total += 1
        print 'Testing ({0} / {1})'.format(correct, total)
    print 'Got', correct, 'out of', total, 'correct'


if __name__ == '__main__':
    main()