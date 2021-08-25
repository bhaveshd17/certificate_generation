# Generated by Django 3.2.6 on 2021-08-24 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate_gen_app', '0002_rename_template_cert_templates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('image', models.ImageField(upload_to='certificate_directory')),
            ],
        ),
    ]