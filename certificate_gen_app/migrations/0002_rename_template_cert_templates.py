# Generated by Django 3.2.6 on 2021-08-24 17:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_gen_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Template',
            new_name='Cert_Templates',
        ),
    ]
