# Generated by Django 2.2.1 on 2019-06-10 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attachments', '0003_auto_20190610_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attachment',
            old_name='file',
            new_name='image',
        ),
    ]