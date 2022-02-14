from PIL import Image, ImageFont, ImageDraw
import json
import random


def generate_valentine(from_inp, to_inp):
    with open("images/images.json") as images_file:
        images_raw = json.load(images_file)['images']

    with open("fonts/fonts.json") as fonts_file:
        fonts_raw = json.load(fonts_file)['fonts']

    fo = random.choice(fonts_raw)
    font_src = f"fonts/{fo['src']}"

    i = random.choice(images_raw)

    font = ImageFont.truetype(font_src, i["font_size"])

    im = Image.open(f"images/{i['image']}")
    print(im.format, im.size, im.mode)

    draw = ImageDraw.Draw(im)

    color = (i['color'][0], i['color'][1], i['color'][2])

    draw.text((i["from"][0], i["from"][1]), from_inp, color, font=font)
    draw.text((i["to"][0], i["to"][1]), to_inp, color, font=font)

    file_format = i['image'].split('.')[1]

    im.save(f"sample-out.{file_format}")

    return f"sample-out.{file_format}"
