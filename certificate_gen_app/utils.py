import os

from PIL import Image, ImageDraw, ImageFont
import requests

from django.conf import settings
from django.template.loader import render_to_string

from .models import Participant
from email.mime.image import MIMEImage
from django.core.mail import EmailMultiAlternatives

def send_mail_func(object):
    subject = 'Event | ITSA 2021-22'
    body_html = render_to_string('send_mail.html')

    from_email = settings.EMAIL_HOST_USER
    to_email = object.email

    msg = EmailMultiAlternatives(
        subject,
        body_html,
        from_email=from_email,
        to=[to_email]
    )

    msg.mixed_subtype = 'related'
    msg.attach_alternative(body_html, "text/html")
    file_path = 'static/images/certificate_dir/'+object.name + ".png"
    with open(file_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-ID', '<{name}>'.format(name=object.name + ".png"))
        img.add_header('Content-Disposition', 'inline', filename=object.name + ".png")
    msg.attach(img)
    msg.send()

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