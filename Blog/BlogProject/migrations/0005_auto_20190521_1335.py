# Generated by Django 2.1.7 on 2019-05-21 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogProject', '0004_auto_20190521_0908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name=100),
        ),
    ]
