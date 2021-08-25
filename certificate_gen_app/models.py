from django.db import models

class Cert_Templates(models.Model):
    template_img = models.ImageField(upload_to='certificate_templates/')
    def __str__(self):
        return str(self.id)

class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    image = models.ImageField(upload_to='certificate_directory')
    def __str__(self):
        return self.name

