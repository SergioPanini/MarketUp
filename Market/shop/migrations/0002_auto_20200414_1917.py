# Generated by Django 3.0.2 on 2020-04-14 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Market',
        ),
        migrations.AddField(
            model_name='products',
            name='User',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.Users'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Markets',
        ),
    ]