# Generated by Django 2.2.1 on 2019-09-05 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plot_viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plot',
            name='model_img_url1',
            field=models.CharField(default='', max_length=150),
        ),
    ]