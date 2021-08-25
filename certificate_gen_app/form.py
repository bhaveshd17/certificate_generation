from django.forms import ModelForm
from .models import  *
class TemplateForm(ModelForm):
    class Meta:
        model=Cert_Templates
        fields="__all__"