# Generated by Django 5.0.3 on 2024-03-11 05:13

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_banner_desctiption_alter_banner_sub_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='desctiption',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]