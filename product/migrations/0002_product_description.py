# Generated by Django 3.2.11 on 2022-01-31 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
