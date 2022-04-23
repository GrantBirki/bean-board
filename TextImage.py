import os
from PIL import Image, ImageFont, ImageDraw
from urllib.request import urlopen
import textwrap
from werkzeug.utils import secure_filename


class TextImage(object):
	"""A helper class to convert text to a black background image with text wrapped on it"""

	def __init__(self, text, color, upload_dir):
		self.text = text
		self.color = color
		self.upload_dir = upload_dir

	def text_to_image(self):
		img = Image.new("RGB", (256, 128))
		size = 96
		truetype_url = 'https://github.com/googlefonts/roboto/blob/main/src/hinted/Roboto-Regular.ttf?raw=true'
		font = ImageFont.truetype(urlopen(truetype_url), size)

		while True:
			if font.getsize(self.text) < img.size or size == 12:
				break
			size -= 1
			font = ImageFont.truetype(urlopen(truetype_url), size)

		draw = ImageDraw.Draw(im=img)
		words = textwrap.fill(text=self.text, width=95, break_long_words=False)
		draw.text(xy=((img.size[0] / 2), img.size[1] / 2), text=words, font=font, fill=self.color, anchor='mm')
		filename = secure_filename("text_image.png")
		basedir = os.path.abspath(os.path.dirname(__file__))
		filepath = os.path.join(basedir, self.upload_dir, filename)
		img.save(filepath)
		return filepath, filename
