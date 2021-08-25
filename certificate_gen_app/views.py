from django.shortcuts import render, redirect
import pandas as pd
from .utils import *

from .form import TemplateForm
from .models import *




def index(request):
    temp_form = TemplateForm()
    template = Cert_Templates.objects.all()[0]
    temp_url = template.template_img.url
    participant = Participant.objects.all()
    if request.method == 'POST':
        url = request.POST.get("url")
        id = url.split('/')[-2]
        path = f"https://docs.google.com/spreadsheets/d/{id}/export?format=csv"
        df = pd.read_csv(path)
        for i in range(0, len(df)):
            data = df.loc[i].tolist()
            certificate_generator(request, name=data[0], temp_url=temp_url, email=data[1])
        return redirect('index')
    content = {'temp_form':temp_form, 'participant':participant}
    return render(request, 'index.html', content)


def add_template(request):
    temp_form = TemplateForm(request.POST, request.FILES)
    if temp_form.is_valid():
        temp_form.save()
        return redirect('index')