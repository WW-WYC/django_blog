# Generated by Django 3.1.5 on 2021-01-05 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='文章配图'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='visited',
            field=models.IntegerField(default=0, verbose_name='文章访问量'),
        ),
    ]