# Generated by Django 2.2.7 on 2019-11-24 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0024_auto_20191123_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
