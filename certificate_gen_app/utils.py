
from django.templatetags.static import static
from PIL import Image, ImageDraw, ImageFont
import requests

from .models import Participant


def certificate_generator(request, name, temp_url, email):
    img_url = 'http://127.0.0.1:8000/static'+temp_url
    font_url = 'http://127.0.0.1:8000/static/images/font/GreatVibes-Regular.ttf'
    image = Image.open(requests.get(img_url, stream=True).raw)

    text_color = (187, 124, 6)
    font = ImageFont.truetype(requests.get(font_url, stream=True).raw, 100)

    draw = ImageDraw.Draw(image)
    text_width, text_height = draw.textsize(name, font=font)
    x_position_center = (image.width - text_width) / 2
    y_position_center = (image.height - text_height) / 2
    location = (x_position_center, y_position_center - 90)

    draw.text(location, name, fill=text_color, font=font)
    image.save('static/images/certificate_dir/'+name + ".png")

    Participant.objects.get_or_create(
        name=name,
        email=email,
        image='/certificate_dir/'+name+ ".png"
    )