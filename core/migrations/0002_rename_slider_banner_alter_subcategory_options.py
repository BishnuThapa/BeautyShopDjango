# Generated by Django 5.0.3 on 2024-03-07 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Slider',
            new_name='Banner',
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Sub Category', 'verbose_name_plural': 'Sub Categories'},
        ),
    ]