# Generated by Django 3.0.2 on 2020-04-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20200414_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='img',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
