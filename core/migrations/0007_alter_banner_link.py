# Generated by Django 5.0.3 on 2024-03-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_productreview_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
